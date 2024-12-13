# importing modules
import datetime
import os
import sys
import time
from functools import partial
from matplotlib import widgets
import psutil
import requests

from bin import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.threadPool = QThreadPool()
        self.functions = Functions(self)
        self.imgService = ImgService()
        self.cpuUsage = False  # this is just a toggle so we know that the proggressBar is running or not
        self.readyFiles = dict()  # store selected files and object
        self.img = None  # i forgot why i put this
        # events
        self.ui.btnPageChat.clicked.connect(lambda: self.btnAction(self.ui.btnPageChat, self.ui.pageChat))
        self.ui.btnPage2.clicked.connect(lambda: self.btnAction(self.ui.btnPage2, self.ui.page2))
        self.ui.btnPage3.clicked.connect(lambda: self.btnAction(self.ui.btnPage3, self.ui.page3))
        self.ui.chatPage_msgPlanEdit.textChanged.connect(self.chatTextEditAction)
        self.ui.chatPage_btn_sendFile.clicked.connect(self.readyFile)
        self.ui.chatPage_BtnChangePicture.clicked.connect(self.generateImg)
        self.ui.bottomFrame_checkBox_cpuToggle.pressed.connect(self.cpuToggle)
        # server interaction events
        self.ui.chatPage_btn_Connect.clicked.connect(self.functions.clientConnTrigger)
        self.ui.chatPage_btn_Host.clicked.connect(self.functions.serverConnTrigger)
        self.ui.chatPage_btn_sendMsg.clicked.connect(self.sendQuery)
        self.ui.chatPage_btn_execCmd.clicked.connect(self.functions.sendCommand)
        # show window bcz it's hidden by default
        self.show()
    ################################ UiFunctions ###############################

    def downloadFile(self, fileName: str, fileContent: bytes):
        fileDir = QFileDialog.getExistingDirectory(parent=self, caption="Select a folder to save your file")
        if fileDir:
            with open(fileDir + "\\" + fileName, mode="wb") as file:
                file.write(fileContent)

    def chatMessage(self, msg: str, files: dict, clientName: str, msgDateTime: datetime.datetime, clientImg: bytes):
        msgFrame = Ui_ChatMsg()
        msgFrame.setupUi(msgFrame)
        msgFrame.label_UserName.setText(clientName)
        msgFrame.label_date.setText(msgDateTime.strftime("%d/%m/%Y %H:%M"))
        img = QPixmap()
        img.loadFromData(clientImg)
        msgFrame.label_img.setPixmap(img)
        msgFrame.msgContentPlanEdit.setPlainText(msg)
        size = round(len(msg) / 100) * 20 + 100 + msg.count('\n') * 20
        # check for files ready to be sent
        if files:
            size += 70
            for fileName, fileInfo in files.items():
                fileFrame = Ui_FileDownload()
                fileFrame.setupUi(fileFrame)
                fileFrame.label_fileName.setText(fileName)
                fileFrame.btn_downloadFile.clicked.connect(partial(self.functions.getFile, fileInfo, fileFrame.fileProgressBar))  # map the signals with "partial" <-- from functools import partial
                msgFrame.hBox_files.addWidget(fileFrame)
                msgFrame.scrollArea_files.setMaximumHeight(60)
                msgFrame.scrollArea_files.setMinimumHeight(60)
            if msg == '':
                msgFrame.msgContentPlanEdit.setMaximumHeight(0)
                msgFrame.msgContentPlanEdit.setMinimumHeight(0)
                size -= 30

        msgFrame.setMaximumHeight(size)
        self.ui.vbox_chat.addWidget(msgFrame, alignment=Qt.AlignBottom)
        # scroll to the bottom
        vsb = self.ui.scrollArea_chatMain.verticalScrollBar()
        vsb.rangeChanged.connect(lambda: vsb.setValue(vsb.maximum()))

    def destroyMessages(self):
        vSpacer = self.ui.chat_verticalSpacer
        while self.ui.vbox_chat.count():
            child = self.ui.vbox_chat.takeAt(0)
            if child.widget():
                child.widget().setParent(None)        
        self.ui.vbox_chat.addSpacerItem(vSpacer)  # idk why the spacer obj keeps getting destroyed even tho he can't pass the if statement

    def clientListActions(self, clientId, clientName, action: str = 'add'):
        if action == 'add':
            self.ui.chatPage_listWidget_hostClients.addItem(f"[{clientId}]:{clientName}")
        else:
            items = self.ui.chatPage_listWidget_hostClients.findItems(f"[{clientId}]:{clientName}", Qt.MatchExactly)
            self.ui.chatPage_listWidget_hostClients.takeItem(self.ui.chatPage_listWidget_hostClients.row(items[0]))

    def generateImg(self):
        if self.ui.chatPage_lineEdit_userName.text().strip() == '':
            self.ui.chatPage_lineEdit_userName.setStyleSheet("border: 2px solid rgb(233, 12, 89);")
        else:
            self.ui.chatPage_lineEdit_userName.setStyleSheet("")
            img = QImage()
            imgUrl = self.imgService.generate_img(value=self.ui.chatPage_lineEdit_userName.text().strip())
            newWorker = Worker(requests.get, 0, imgUrl)
            self.threadPool.start(newWorker)
            newWorker.signals.results.connect(
                lambda req: (img.loadFromData(req.content), self.ui.chatPage_Label_pic.setPixmap(QPixmap(img))))
            newWorker.signals.error.connect(lambda: self.printMsgToChat(
                f"[{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}]:You need internet connection to generate an image from your user name"))

    def setClientImg(self):
        img = self.ui.chatPage_Label_pic.pixmap()
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        self.img = buffer.data()
        buffer.close()

    def printMsgToChat(self, textMsg: str, colorRgb: str='rgb(233, 12, 89)'):
        labelMsg = QLabel()
        labelMsg.setObjectName('appMsg')
        labelMsg.setStyleSheet('QLabel {font: italic 10pt "Roboto"; color: '+colorRgb+';}')
        labelMsg.setText(textMsg)
        # labelMsg.setAlignment(Qt.AlignHCenter)
        self.ui.vbox_chat.addWidget(labelMsg, alignment=Qt.AlignBottom)
        # scroll to the bottom
        vsb = self.ui.scrollArea_chatMain.verticalScrollBar()
        vsb.rangeChanged.connect(lambda: vsb.setValue(vsb.maximum()))

    def clientConnStyles(self, connected: bool):
        if connected:
            self.ui.chatPage_Label_ConnStatue.setText('Online')
            self.ui.chatPage_Label_ConnStatue.setStyleSheet(
                self.ui.chatPage_Label_ConnStatue.styleSheet().replace('icon_offline.svg', 'icon_online.svg'))
            self.ui.chatPage_btn_Connect.setText('Disconnect')
            self.ui.chatPage_btn_Connect.setStyleSheet(
                self.ui.chatPage_btn_Connect.styleSheet().replace('rgb(233, 12, 89)', 'rgb(189, 255, 0)'))
            self.ui.chatPage_lineEdit_Port.setStyleSheet("")
            self.ui.chatPage_lineEdit_Port.setReadOnly(True)
            self.ui.chatPage_lineEdit_Ip.setStyleSheet("")
            self.ui.chatPage_lineEdit_Ip.setReadOnly(True)
            self.ui.chatPage_lineEdit_userName.setStyleSheet("")
            self.ui.chatPage_lineEdit_userName.setReadOnly(True)
            self.ui.chatPage_BtnChangePicture.setEnabled(False)
        else:
            self.ui.chatPage_Label_ConnStatue.setText('Offline')
            self.ui.chatPage_Label_ConnStatue.setStyleSheet(
                self.ui.chatPage_Label_ConnStatue.styleSheet().replace('icon_online.svg', 'icon_offline.svg'))
            self.ui.chatPage_btn_Connect.setText('Connect')
            self.ui.chatPage_btn_Connect.setStyleSheet(
                self.ui.chatPage_btn_Connect.styleSheet().replace('rgb(189, 255, 0)', 'rgb(233, 12, 89)'))
            self.ui.chatPage_lineEdit_Port.setReadOnly(False)
            self.ui.chatPage_lineEdit_Ip.setReadOnly(False)
            self.ui.chatPage_lineEdit_userName.setReadOnly(False)
            self.ui.chatPage_BtnChangePicture.setEnabled(True)

    def serverConnStyles(self, started: bool):
        if started:
            self.ui.chatPage_btn_Host.setText('Hosting...')
            self.ui.chatPage_btn_Host.setStyleSheet(
                self.ui.chatPage_btn_Host.styleSheet().replace('rgb(233, 12, 89)', 'rgb(189, 255, 0)'))
            self.ui.chatPage_cbox_HostType.setEnabled(False)
            self.ui.chatPage_fileSizeTraffic.setEnabled(False)
        else:
            self.ui.chatPage_btn_Host.setText('Host Server')
            self.ui.chatPage_btn_Host.setStyleSheet(
                self.ui.chatPage_btn_Host.styleSheet().replace('rgb(189, 255, 0)', 'rgb(233, 12, 89)'))
            self.ui.chatPage_cbox_HostType.setEnabled(True)
            self.ui.chatPage_listWidget_hostClients.clear()
            self.ui.chatPage_fileSizeTraffic.setEnabled(True)

    @staticmethod
    def connectBtnAnimations(animation: QMovie, btn: QPushButton, start: bool):
        animation.frameChanged.connect(lambda: btn.setIcon(animation.currentPixmap()))
        if start:
            btn.setEnabled(False)
            animation.start()
        else:
            btn.setEnabled(True)
            animation.stop()
            btn.setIcon(QIcon())
            del animation

    def sendQuery(self):
        if self.functions.client.alive:  # send if he is connected
            textMsg = self.ui.chatPage_msgPlanEdit.toPlainText().strip()
            if self.readyFiles or textMsg:
                query = dict()
                query['contentType'] = 'msg'
                query['msgEncoding'] = 'utf-8'
                query['msgBytes'] = textMsg.encode('utf-8')

                if self.readyFiles:
                    files = dict()
                    for fileDir in self.readyFiles.values():  # store ready files->{'image.png': b'\x89PNG\x00...'}
                        with open(fileDir, mode='rb') as file:
                            files[os.path.basename(fileDir)] = file.read()
                    query['contentType'] = 'msg/files'
                    query['filesData'] = files
                self.functions.client.createQuery(isCmd=False, isCmdResult=False, **query)
            # reset
            self.ui.chatPage_msgPlanEdit.setPlainText('')
            self.ui.scrollArea_fileReady.setMaximumHeight(0)
            for obj in self.readyFiles.keys():  # destroy fileFrames
                obj.deleteLater()
            self.readyFiles = dict()  # delete fileFrames and fileDir

    def readyFile(self):
        if self.functions.client.alive:
            fileList = self.fileDialog(caption="Select your files", fileFilter="anyFile (*)", multiple=True)
            for fileDir in fileList:
                if os.path.getsize(fileDir) / 1024**2 < self.functions.allowedFileSize:  # check if fileSize is allowed by host
                    fileFrame = Ui_FileReady()
                    fileFrame.setupUi(fileFrame)
                    self.ui.scrollArea_fileReady.setMaximumHeight(70)
                    fileFrame.label_fileName.setText(os.path.basename(fileDir))
                    self.readyFiles[fileFrame] = fileDir  # save the parent with the fileDir to a dict
                    fileFrame.btn_binFile.clicked.connect(partial(self.destroyReadyFile,
                                                                fileFrame))  # map the signals with "partial" <-- from functools import partial
                    self.ui.hBox_fileReady.addWidget(fileFrame)
                else:
                    QMessageBox.information(self,
                                            f"File size is too big",
                                            f"Host did not allow files bigger than {self.functions.allowedFileSize} MB \n this file is out -> {os.path.basename(fileDir)}",
                                            QMessageBox.Ok)

    def destroyReadyFile(self, obj: Qt.Widget):
        obj.deleteLater()
        self.readyFiles.pop(obj)
        if not self.readyFiles:
            self.ui.scrollArea_fileReady.setMaximumHeight(0)

    def fileDialog(self, caption: str, fileFilter: str, multiple: bool = False) -> str:
        if multiple:
            fileList = QFileDialog.getOpenFileNames(parent=self,
                                                    caption=caption,
                                                    filter=fileFilter)[0]
            return fileList
        else:
            selectedFile = QFileDialog.getOpenFileName(parent=self,
                                                       caption=caption,
                                                       filter=fileFilter)[0]
            return selectedFile

    def chatTextEditAction(self):
        # big brain stuff you wouldn't understand
        size = 40 + self.ui.chatPage_msgPlanEdit.document().lineCount() * 20  # 40 + lineCount * 20 = x <- height needed
        if size > 180:
            size = 180
        self.ui.chatPage_msgFrame.setMaximumHeight(size)
        if self.ui.chatPage_msgPlanEdit.document().lineCount() >= 9:  # show the scroll bar when we hit 9 lines
            self.ui.chatPage_msgPlanEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        else:
            self.ui.chatPage_msgPlanEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def btnAction(self, btn: QPushButton, page: QWidget):
        self.ui.stackedWidget.setCurrentWidget(page)
        self.ui.btnPageChat.setChecked(False)
        self.ui.btnPage2.setChecked(False)
        self.ui.btnPage3.setChecked(False)
        btn.setChecked(True)

    def cpuToggle(self):
        if self.ui.bottomFrame_checkBox_cpuToggle.isChecked():
            self.cpuUsage = False
        else:
            self.cpuUsage = True
            cpuWorker = Worker(self.startCpuProgressBar)
            self.threadPool.start(cpuWorker)
    def startCpuProgressBar(self):
        while self.cpuUsage:    
            time.sleep(1)  # refresh time
            self.ui.chatPage_CPUprogressBar.setValue(psutil.cpu_percent())
        self.ui.chatPage_CPUprogressBar.setValue(0)

    def setDropShadow(self, frame: QFrame):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 80))
        frame.setFrameShadow(QFrame.Raised)
        frame.setGraphicsEffect(shadow)

    def closeEvent(self, event: QCloseEvent) -> None:  # handle close window
        msg = QMessageBox.question(self,
                                   "Window close",
                                   "Are you sure you want to close the window ?",
                                   QMessageBox.Yes, QMessageBox.No)
        if msg == QMessageBox.Yes:
            # stop all long running threads
            # so the threads dose not stay running in background when the window is destroyed
            self.functions.server.stop()
            self.functions.client.disconnect()
            # wait until all threads are stopped (it's like a sec or two)
            while self.functions.threadPool.activeThreadCount() and self.threadPool.activeThreadCount():
                pass
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication()
    app.setApplicationName('Net-Box')
    app.setApplicationVersion('v1.0.0 (64-bit)')
    app.setWindowIcon(QIcon(r'images\icons\icon.ico'))
    window = MainWindow()
    sys.exit(app.exec())
