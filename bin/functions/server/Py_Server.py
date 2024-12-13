import datetime
import pickle
import re
import socket
import selectors
import threading
import time
import traceback

import numpy as np
import pandas as pd

from .Py_ServerQuery import QueryServer
from PySide6.QtCore import QObject, Signal

# telnet 127.0.0.1 9999
# debugging exceptions: [Class](function)->error message
class Server:
    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # IPV4|TCP
        self.ADDRESS = ("ip", 0000)  # we will change this later of course
        self.alive = False
        self.signals = ServerSignals()
        self.filesStorage = pd.DataFrame(data=None, columns=['fileId', 'fileName', 'fileContent'])
        self.queryStorage = pd.Series(dtype=object)
        self.clientStatue = pd.DataFrame(data=None, columns=['datetime', 'clientIp', 'statue', 'jailTime'])
        self.allowedFileSize = 0

    def execCmd(self, cmd: str) -> bool:  # this method is ugly to look at i know
        # making sure that the command is correct
        cmdInfo = re.findall(pattern=r"<(.+?)>", string=cmd)  # getting the args of the command "<everything between>"
        print(cmdInfo)
        try:
            client = self.getQueryById(cmdInfo[0])  # getting the query class obj of the client by his clientId
        except IndexError:  # handling typo errors
            return False
        if client:  # process command
            if cmd.startswith("->ipban"):
                self.banClient(client)
            if cmd.startswith("->timeout"):
                try:
                    jailTime = float(cmdInfo[1])
                    self.timeOutClient(client, jailTime)
                except ValueError or IndexError:  # handling typo errors
                    return False
            if cmd.startswith("->ps"):
                try:
                    self.sendPScmd(client, psCmd=cmdInfo[1])
                except IndexError:
                    return False
            return True
        return False  # if we got to this line and we didn't execute the command then return False

    ########## server commands methods
    def banClient(self, client: QueryServer):
        ip = client.clientAddress[0]
        self.clientStatue[self.clientStatue["clientIp"] == ip] = datetime.datetime.now(), ip, 'banned', np.nan
        infoQuery = self.cookQuery(isCmd=False, isCmdResult=True, cmd='->banned')
        client.clientSocket.sendall(infoQuery)
        client.closeConn()

    def timeOutClient(self, client: QueryServer, jailTime: float):
        ip = client.clientAddress[0]
        self.clientStatue[self.clientStatue["clientIp"] == ip] = datetime.datetime.now(), ip, 'timedOut', jailTime
        infoQuery = self.cookQuery(isCmd=False, isCmdResult=True, cmd=f'->timedOut for {jailTime} min')
        client.clientSocket.sendall(infoQuery)
        client.closeConn()

    def sendPScmd(self, client: QueryServer, psCmd: str):
        infoQuery = self.cookQuery(isCmd=True, isCmdResult=False, cmd='->ps', psCmd=psCmd)
        client.clientSocket.sendall(infoQuery)

    def getQueryById(self, clientId):
        for key in self.sel.get_map().values():
            if key.data:
                return key.data if key.data.clientId == clientId else None
    #########################################
    def fireWall(self, ip: str) -> bool:
        mask = self.clientStatue["clientIp"] == ip
        if np.any(mask):
            clientInfo = self.clientStatue[mask]
            if np.any(clientInfo.loc[0, 'statue'] == 'clear'):
                return True
            if np.any(clientInfo.loc[0, 'statue'] == 'banned'):
                return False
            if np.any(clientInfo.loc[0, 'statue'] == 'timedOut'):
                timeFree = clientInfo.loc[0, 'datetime'] + datetime.timedelta(minutes=clientInfo.loc[0, 'jailTime'])
                now = datetime.datetime.now()
                if now > timeFree:
                    self.clientStatue[mask] = now, ip, 'clear', np.nan
                    return True
                else:
                    return False
        else:
            self.clientStatue = pd.concat([self.clientStatue, pd.DataFrame([[datetime.datetime.now(), ip, 'clear']], columns=['datetime', 'clientIp', 'statue'])], ignore_index=True)
            return True

    def acceptConn(self, request):
        try:
            clientSocket, clientAddress = request.accept()
        except socket.error as err:
            # print(traceback.format_exc())
            print('[Server](acceptConn)->', err)
        else:
            if self.fireWall(clientAddress[0]):  # check client if it's banned or timedOut
                query = QueryServer(self, clientSocket, clientAddress)  # Query is a custom class that help us handle data between endpoints more efficiently
                self.sel.register(clientSocket, events=selectors.EVENT_READ, data=query)  # register the clientSocket to be monitored
            else:
                clientSocket.close()

    def startEventLoop(self):
        while self.alive:
            events = self.sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:  # new client: accept
                    self.acceptConn(key.fileobj)
                else:  # old client: handle
                    query = key.data
                    try:
                        query.handleClient(mask)  # handle I/O
                    except Exception as err:  # catch any exceptions raised by QueryClass (event loop should never stop running!)
                        print(traceback.format_exc())
                        print(err)
                        # very important to close connection with the socket that raised the error (cleanUp)
                        # and this will kick any rats trying to join the server
                        query.closeConn()
        self.alive = False

    def start(self):
        try:
            self.serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # IPV4|TCP
            self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Avoid .bind() exception: OSError: Address already in use
            self.serverSocket.bind(self.ADDRESS)
            self.serverSocket.listen()
            self.serverSocket.setblocking(False)
            self.sel.register(self.serverSocket, events=selectors.EVENT_READ, data=None)  # register the serverSocket to be monitored
            self.alive = True
        except socket.error as err:
            print('[Server](start)->', err)
            self.alive = False

    @staticmethod
    def cookQuery(**kwargs):  # send query outside the class
        queryBytes = pickle.dumps(kwargs)
        querySizeBytes = pickle.dumps(len(queryBytes))
        return querySizeBytes + queryBytes

    def stop(self):
        if self.alive:  # just for safety
            query = self.cookQuery(isCmd=True, isCmdResult=False, cmd='->hostLeft')
            clients = list(self.sel.get_map().values())
            for key in clients:
                if key.data:
                    key.fileobj.sendall(query)

            # kill server / kick all
            self.alive = False
            self.sel.unregister(self.serverSocket)
            self.serverSocket.close()
            # cleanUp
            self.sel.close()
            self.sel = selectors.DefaultSelector()

class ServerSignals(QObject):
    clientConnected = Signal(tuple)
    clientDisconnected = Signal(tuple)
    psResult = Signal(str)


if __name__ == '__main__':
    server = Server()
    server.start()
    server.startEventLoop()
