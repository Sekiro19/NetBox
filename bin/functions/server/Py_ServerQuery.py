import datetime
import random
import re
import selectors
import pickle
# debugging exceptions: [Class](function)->error message
import time
from builtins import bytearray

import numpy as np
import pandas as pd


class QueryServer:
    def __init__(self, parent, sock, address):
        self.server = parent
        self.clientSocket = sock
        self.clientAddress = address
        self.clientInfo = None  # None for now
        self.clientId = self.createId()
        # maximum size of bytes that can be received per call
        self.BUFFER_SIZE = 4096
        # main data access points
        self.sendBuffer = bytearray()
        self.recvBuffer = bytearray()
        # the first bytes we read are the querySize they help us know the query limits bcz we are reading from a stream of bytes -> QueryQueryQuery...
        self.querySize = None
        self.query = None
        self.echoMode = False

    def createQuery(self, isCmd: bool = False, isCmdResult: bool = False, **kwargs):
        kwargs['isCmd'] = isCmd
        kwargs['isCmdResult'] = isCmdResult
        queryBytes = pickle.dumps(kwargs)
        querySizeBytes = pickle.dumps(len(queryBytes))
        self.sendBuffer = querySizeBytes + queryBytes
        # Set selector to listen for write events, we're done reading.
        self.server.sel.modify(self.clientSocket, selectors.EVENT_WRITE, self)

    def sendIt(self):
        try:
            sent = self.clientSocket.send(self.sendBuffer)
            self.sendBuffer = self.sendBuffer[sent:]
        except BlockingIOError:
            pass  # Resource temporarily unavailable (errno EWOULDBLOCK)
        except OSError:  # expecting [WinError 10054] (client forcibly closed connection)
            raise OSError(f"[QueryServer](sendIt)->Connection was forcibly closed by the client")  # the event loop will close connection

    def writeQuery(self):
        if self.sendBuffer:
            if self.echoMode:
                self.echo()
            else:
                self.sendIt()
        if not self.sendBuffer:
            # Set selector to listen for read events, we're done writing.
            self.server.sel.modify(self.clientSocket, selectors.EVENT_READ, self)

    def getQuery(self):
        self.recvBuffer = self.recvBuffer[:self.querySize]
        self.query = pickle.loads(self.recvBuffer)  # bytes to -> python obj (dict)
        # buffer drained (readyUp for new query)
        self.recvBuffer = self.recvBuffer[self.querySize:]
        self.querySize = None
        self.processQuery()

    def getQuerySize(self):
        querySizeBytes = self.recvBuffer.split(b'.', 1)[0] + b'.'
        self.recvBuffer = self.recvBuffer[len(querySizeBytes):]
        self.querySize = pickle.loads(querySizeBytes)

    def recvIt(self):
        try:  # receive and fragment all chunks
            chunk = self.clientSocket.recv(self.BUFFER_SIZE)
            if chunk:
                self.recvBuffer.extend(chunk)  # append to recvBufferByteArray
            else:  # no data client closed connection
                self.closeConn()
        except BlockingIOError:
            pass  # Resource temporarily unavailable (errno EWOULDBLOCK)
        except OSError:  # expecting [WinError 10054] (client forcibly closed connection)
            raise OSError(
                f"[QueryServer](recvIt)->Connection was forcibly closed by the client")  # the event loop will close connection

    def readQuery(self):
        self.recvIt()
        if self.recvBuffer:
            if self.querySize is None:
                self.getQuerySize()
            if self.querySize is not None:  # we don't put else here so the statement gets checked
                if len(self.recvBuffer) >= self.querySize:
                    self.getQuery()

    def handleClient(self, mask: int):
        if mask & selectors.EVENT_READ:  # If socket is ready for reading, then mask & selectors.EVENT_READ is True (bitwise)
            self.readQuery()
        if mask & selectors.EVENT_WRITE:  # If socket is ready for writing, then mask & selectors.EVENT_WRITE is True (bitwise)
            self.writeQuery()

    def closeConn(self):
        # client closed connection so he is no longer monitored
        self.server.sel.unregister(self.clientSocket)
        self.clientSocket.close()
        self.server.signals.clientDisconnected.emit((self.clientId, self.clientInfo['clientName']))

    def echo(self):
        clients = list(self.server.sel.get_map().values())
        for key in clients:
            if key.data:  # echo to all sockets except server socket
                try:
                    key.fileobj.sendall(self.sendBuffer)
                except BlockingIOError:
                    pass  # Resource temporarily unavailable (errno EWOULDBLOCK)
                except OSError:  # expecting [WinError 10054] (client forcibly closed connection)
                    raise OSError(f"[QueryServer](echo)->Connection was forcibly closed by the client")  # the event loop will close connection
        self.sendBuffer = bytearray()  # we used "sendall()" so the buffer should be empty

    def storeFiles(self) -> dict:
        filesIdDict = dict()
        for fileName, fileContent in self.query['filesData'].items():
            fileId = self.createFileId()
            filesIdDict[fileName] = fileId, len(fileContent)
            self.server.filesStorage = self.server.filesStorage = pd.concat([self.server.filesStorage,
                                                                             pd.DataFrame(
                                                                                 [[fileId, fileName, fileContent]],
                                                                                 columns=['fileId', 'fileName',
                                                                                          'fileContent'])],
                                                                            ignore_index=True)
        return filesIdDict

    def createId(self) -> str:
        clientId = f"{random.randrange(100, 999)}.{random.randrange(100, 999)}.{random.randrange(100, 999)}"
        clientIdsList = [key.data.clientId for key in self.server.sel.get_map().values() if key.data]
        if clientId in clientIdsList:
            self.createId()
        else:
            return clientId

    def createFileId(self) -> int:
        fileId = random.randrange(100, 999)
        if np.any(fileId == self.server.filesStorage['fileId']):
            self.createFileId()
        else:
            return fileId

    def processQuery(self):
        self.echoMode = False
        if self.query["isCmd"]:  # is command -> ProcessCommand
            if self.query['cmd'].startswith("->sendFile"):
                self.sendFile()
            if self.query['cmd'].startswith("->info"):  # insert client info (name, ...)
                self.insertInfo()
        elif self.query["isCmdResult"]:
            self.server.signals.psResult.emit(self.query["result"])
            
        else:  # chatMessage -> echo to all
            self.echoMode = True
            if self.query['contentType'] == 'msg/files':
                filesIdDict = self.storeFiles()
                self.query['filesData'] = filesIdDict
            self.query['clientName'] = self.clientInfo['clientName']
            self.query['clientImg'] = self.clientInfo['clientImg']
            self.query['queryDateTime'] = datetime.datetime.now()
            self.createQuery(**self.query)
            self.server.queryStorage = pd.concat([self.server.queryStorage, pd.Series([self.query], dtype=object)])  # store the query
        self.query = None

    #### client command methods ####
    def sendFile(self):
        fileId = re.findall(pattern=r"<(\d+)>", string=self.query['cmd'])[0]
        output = self.server.filesStorage[self.server.filesStorage['fileId'] == int(fileId)].iloc[0, [1, 2]].to_numpy()
        self.createQuery(isCmd=False, isCmdResult=True, cmd=self.query['cmd'], result=output)

    def insertInfo(self):
        self.clientInfo = self.query['info']
        self.server.signals.clientConnected.emit((self.clientId, self.clientInfo['clientName']))  # signal for the host that a client connected
        # send client previous messages if there is any
        self.createQuery(isCmd=False, isCmdResult=True, cmd='->info', result=(self.server.allowedFileSize, self.server.queryStorage))
