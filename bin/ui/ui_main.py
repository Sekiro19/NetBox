# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(972, 572)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.styleSheet = QFrame(self.centralwidget)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"/*_______________Styles______________*/\n"
"#topFrame {background-color: rgb(77, 77, 77);}\n"
"#leftFrame {background-color: rgba(103, 103, 103, 255);}\n"
"#bottomFrame {background-color: rgb(77, 77, 77);}\n"
"#pageChat {background-color: rgb(82, 86, 95);}\n"
"#leftFrame .QPushButton {\n"
"	background-color: transparent;\n"
"	border-bottom: 1px solid rgb(136, 136, 136);\n"
"	border-top: 1px solid rgb(136, 136, 136);\n"
"}\n"
"#leftFrame .QPushButton:hover {\n"
"	background-color: rgb(93, 93, 93);\n"
"}\n"
"#leftFrame .QPushButton:checked {\n"
"	background-color: rgb(52, 116, 208);\n"
"	border: none;\n"
"}\n"
"#pageChat_chatFrame.QFrame {\n"
"	background-color: rgb(54, 57, 63);\n"
"	border-radius: 10px;\n"
"}\n"
"#pageChat_chatActionsFrame.QFrame {\n"
"	background-color: rgb(47, 49, 54);\n"
"}\n"
"#chatPage_msgBoxFrame.QFrame {\n"
"	background-color: rgb(64, 68, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"/*_______________Fixed_Styles______________*/\n"
"/*QLineEdit*/\n"
"QLineEdit {\n"
"	border: 2px solid rgb(103"
                        ", 103, 103);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(47, 48, 50);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 2px solid rgb(189, 255, 0);\n"
"	background-color: rgb(14, 14, 15);\n"
"}\n"
"/*QPushButton*/\n"
"\n"
"/*QScrollBar*/\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 255, 0);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"    background: transparent;\n"
"	width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
""
                        "	border: none;\n"
"    background: transparent;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 4px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 255, 0);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: transparent;\n"
"     height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    backg"
                        "round: transparent;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"/*QTabWidget*/\n"
"QTabWidget::pane { \n"
"	top:-1px;\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"	border: none;\n"
"	top:-1px; \n"
"}\n"
"QTabBar::tab {\n"
"	background-color: transparent;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"	width: 150px; height: 30px;\n"
" }\n"
"QTabBar::tab:selected {\n"
"	border-top: 2px solid  rgb(189, 255, 0);\n"
" }\n"
"/*QComboBox*/\n"
"QComboBox{\n"
"	background-color: rgb(47, 48, 50);\n"
"	color: rgb(230, 230, 230);\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"	border: 2px solid rgb(103, 103, 103);\n"
"	border-radius: 5px"
                        ";\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	color: rgb(230, 230, 230);\n"
"	border: 2px solid rgb(189, 255, 0);\n"
"	background-color: rgb(14, 14, 15);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/images/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(230, 230, 230);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"QProgressBar {\n"
"    background: rgb(112, 118, 130);\n"
"	color: rgb(233, 12, 89);\n"
"	font: 7pt \"Roboto\";\n"
"	text-align: right;\n"
"    border-radius: 4px;\n"
"	margin-right: 20px;\n"
"}\n"
"QP"
                        "rogressBar::chunk {\n"
"    background-color: rgb(189, 255, 0);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QLabel {\n"
"	border-radius: 5px;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/*QPlainTextEdit*/\n"
"QPlainTextEdit {\n"
"	font: 10pt \"Terminal\";\n"
"	border: 2px solid rgb(103, 103, 103);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(47, 48, 50);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 2px solid rgb(189, 255, 0);\n"
"	background-color: rgb(14, 14, 15);\n"
"}\n"
"/*QListWidget*/\n"
"QListWidget {\n"
"	font: 10pt \"Terminal\";\n"
"	border: 2px solid rgb(103, 103, 103);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(47, 48, 50);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
""
                        "}\n"
"QListWidget:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 2px solid rgb(189, 255, 0);\n"
"	background-color: rgb(14, 14, 15);\n"
"}")
        self.styleSheet.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topFrame = QFrame(self.styleSheet)
        self.topFrame.setObjectName(u"topFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topFrame.sizePolicy().hasHeightForWidth())
        self.topFrame.setSizePolicy(sizePolicy)
        self.topFrame.setMinimumSize(QSize(0, 60))
        self.topFrame.setMaximumSize(QSize(16777215, 60))
        self.topFrame.setStyleSheet(u"")
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.topFrame)
        self.logo.setObjectName(u"logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        self.logo.setMinimumSize(QSize(110, 0))
        self.logo.setMaximumSize(QSize(110, 16777215))
        self.logo.setPixmap(QPixmap(u":/images/images/icons/logo.svg"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.logo)

        self.appNameFrame = QFrame(self.topFrame)
        self.appNameFrame.setObjectName(u"appNameFrame")
        self.verticalLayout_4 = QVBoxLayout(self.appNameFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(self.appNameFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 16pt \"Roboto\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.appNameFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(182, 182, 182);\n"
"font: 10pt \"Roboto\";")

        self.verticalLayout_4.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.appNameFrame)

        self.frame_3 = QFrame(self.topFrame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(200, 0))
        self.frame_3.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.topFrame)

        self.containerFrame = QFrame(self.styleSheet)
        self.containerFrame.setObjectName(u"containerFrame")
        self.horizontalLayout = QHBoxLayout(self.containerFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftFrame = QFrame(self.containerFrame)
        self.leftFrame.setObjectName(u"leftFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftFrame.sizePolicy().hasHeightForWidth())
        self.leftFrame.setSizePolicy(sizePolicy2)
        self.leftFrame.setMinimumSize(QSize(110, 0))
        self.leftFrame.setMaximumSize(QSize(110, 16777215))
        self.leftFrame.setAutoFillBackground(False)
        self.leftFrame.setStyleSheet(u"")
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.vbox5 = QVBoxLayout(self.leftFrame)
        self.vbox5.setSpacing(0)
        self.vbox5.setObjectName(u"vbox5")
        self.vbox5.setContentsMargins(0, 0, 0, 0)
        self.btnPageChat = QPushButton(self.leftFrame)
        self.btnPageChat.setObjectName(u"btnPageChat")
        self.btnPageChat.setMaximumSize(QSize(16777215, 100))
        self.btnPageChat.setStyleSheet(u"image: url(:/images/images/img/server.png);")
        self.btnPageChat.setCheckable(True)
        self.btnPageChat.setChecked(True)

        self.vbox5.addWidget(self.btnPageChat)

        self.btnPage2 = QPushButton(self.leftFrame)
        self.btnPage2.setObjectName(u"btnPage2")
        self.btnPage2.setMaximumSize(QSize(16777215, 100))
        self.btnPage2.setStyleSheet(u"image: url(:/images/images/img/x.webp);")
        self.btnPage2.setCheckable(True)
        self.btnPage2.setChecked(False)

        self.vbox5.addWidget(self.btnPage2)

        self.btnPage3 = QPushButton(self.leftFrame)
        self.btnPage3.setObjectName(u"btnPage3")
        self.btnPage3.setMaximumSize(QSize(16777215, 100))
        self.btnPage3.setStyleSheet(u"image: url(:/images/images/img/x.webp);")
        self.btnPage3.setCheckable(True)
        self.btnPage3.setChecked(False)

        self.vbox5.addWidget(self.btnPage3)


        self.horizontalLayout.addWidget(self.leftFrame)

        self.midFrame = QFrame(self.containerFrame)
        self.midFrame.setObjectName(u"midFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.midFrame.sizePolicy().hasHeightForWidth())
        self.midFrame.setSizePolicy(sizePolicy3)
        self.verticalLayout_3 = QVBoxLayout(self.midFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.midFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageChat = QWidget()
        self.pageChat.setObjectName(u"pageChat")
        self.pageChat.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.pageChat)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.pageChat)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pageChat_chatFrame = QFrame(self.frame)
        self.pageChat_chatFrame.setObjectName(u"pageChat_chatFrame")
        self.pageChat_chatFrame.setStyleSheet(u"")
        self.pageChat_chatFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.pageChat_chatFrame)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.chatPage_Header = QFrame(self.pageChat_chatFrame)
        self.chatPage_Header.setObjectName(u"chatPage_Header")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.chatPage_Header.sizePolicy().hasHeightForWidth())
        self.chatPage_Header.setSizePolicy(sizePolicy4)
        self.chatPage_Header.setMinimumSize(QSize(0, 15))
        self.chatPage_Header.setMaximumSize(QSize(16777215, 15))
        self.horizontalLayout_6 = QHBoxLayout(self.chatPage_Header)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.chatPage_Label_ConnStatue = QLabel(self.chatPage_Header)
        self.chatPage_Label_ConnStatue.setObjectName(u"chatPage_Label_ConnStatue")
        self.chatPage_Label_ConnStatue.setStyleSheet(u"QLabel {\n"
"	border-radius: 5px;\n"
"	font: 600 italic 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"	text-align: left;\n"
"	padding-left: 30px;\n"
"	\n"
"	background-image: url(:/images/images/icons/icon_offline.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"}")

        self.horizontalLayout_6.addWidget(self.chatPage_Label_ConnStatue)


        self.verticalLayout_5.addWidget(self.chatPage_Header)

        self.scrollArea_chatMain = QScrollArea(self.pageChat_chatFrame)
        self.scrollArea_chatMain.setObjectName(u"scrollArea_chatMain")
        sizePolicy3.setHeightForWidth(self.scrollArea_chatMain.sizePolicy().hasHeightForWidth())
        self.scrollArea_chatMain.setSizePolicy(sizePolicy3)
        self.scrollArea_chatMain.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.scrollArea_chatMain.setFrameShape(QFrame.NoFrame)
        self.scrollArea_chatMain.setFrameShadow(QFrame.Plain)
        self.scrollArea_chatMain.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_chatMain.setWidgetResizable(True)
        self.scrollArea_chatMain.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.scroll_chat = QWidget()
        self.scroll_chat.setObjectName(u"scroll_chat")
        self.scroll_chat.setGeometry(QRect(0, 0, 526, 334))
        self.scroll_chat.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.scroll_chat)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.vbox_chat = QVBoxLayout()
        self.vbox_chat.setSpacing(0)
        self.vbox_chat.setObjectName(u"vbox_chat")
        self.chat_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vbox_chat.addItem(self.chat_verticalSpacer)


        self.verticalLayout_8.addLayout(self.vbox_chat)

        self.scrollArea_chatMain.setWidget(self.scroll_chat)

        self.verticalLayout_5.addWidget(self.scrollArea_chatMain)

        self.line = QFrame(self.pageChat_chatFrame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border-top: 1px solid rgb(93, 93, 93);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_5.addWidget(self.line)

        self.scrollArea_fileReady = QScrollArea(self.pageChat_chatFrame)
        self.scrollArea_fileReady.setObjectName(u"scrollArea_fileReady")
        sizePolicy3.setHeightForWidth(self.scrollArea_fileReady.sizePolicy().hasHeightForWidth())
        self.scrollArea_fileReady.setSizePolicy(sizePolicy3)
        self.scrollArea_fileReady.setMinimumSize(QSize(0, 0))
        self.scrollArea_fileReady.setMaximumSize(QSize(16777215, 0))
        self.scrollArea_fileReady.setStyleSheet(u"background-color: Transparent;")
        self.scrollArea_fileReady.setFrameShape(QFrame.NoFrame)
        self.scrollArea_fileReady.setFrameShadow(QFrame.Plain)
        self.scrollArea_fileReady.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_fileReady.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 526, 40))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(64, 68, 75);\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.hBox_fileReady = QHBoxLayout()
        self.hBox_fileReady.setSpacing(15)
        self.hBox_fileReady.setObjectName(u"hBox_fileReady")
        self.hBox_fileReady.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hBox_fileReady.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addLayout(self.hBox_fileReady)

        self.scrollArea_fileReady.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_5.addWidget(self.scrollArea_fileReady)

        self.chatPage_msgFrame = QFrame(self.pageChat_chatFrame)
        self.chatPage_msgFrame.setObjectName(u"chatPage_msgFrame")
        sizePolicy4.setHeightForWidth(self.chatPage_msgFrame.sizePolicy().hasHeightForWidth())
        self.chatPage_msgFrame.setSizePolicy(sizePolicy4)
        self.chatPage_msgFrame.setMinimumSize(QSize(0, 60))
        self.chatPage_msgFrame.setMaximumSize(QSize(16777215, 60))
        self.chatPage_msgFrame.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.chatPage_msgFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 9)
        self.chatPage_msgBoxFrame = QFrame(self.chatPage_msgFrame)
        self.chatPage_msgBoxFrame.setObjectName(u"chatPage_msgBoxFrame")
        self.chatPage_msgBoxFrame.setMaximumSize(QSize(16777215, 16777205))
        self.chatPage_msgBoxFrame.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.chatPage_msgBoxFrame)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 7, 6, 6)
        self.chatPage_btn_sendFile = QPushButton(self.chatPage_msgBoxFrame)
        self.chatPage_btn_sendFile.setObjectName(u"chatPage_btn_sendFile")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.chatPage_btn_sendFile.sizePolicy().hasHeightForWidth())
        self.chatPage_btn_sendFile.setSizePolicy(sizePolicy5)
        self.chatPage_btn_sendFile.setMinimumSize(QSize(30, 30))
        self.chatPage_btn_sendFile.setMaximumSize(QSize(30, 30))
        self.chatPage_btn_sendFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.chatPage_btn_sendFile.setStyleSheet(u"QPushButton {\n"
"	border-radius: 15px;\n"
"	background-color:  transparent;\n"
"	background-repeat: no-reperat;\n"
"	image: url(:/images/images/icons/msgAddFile.png);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(103, 110, 121);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:  rgb(85, 90, 99);\n"
"}")

        self.horizontalLayout_5.addWidget(self.chatPage_btn_sendFile, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.chatPage_msgPlanEdit = QPlainTextEdit(self.chatPage_msgBoxFrame)
        self.chatPage_msgPlanEdit.setObjectName(u"chatPage_msgPlanEdit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.chatPage_msgPlanEdit.sizePolicy().hasHeightForWidth())
        self.chatPage_msgPlanEdit.setSizePolicy(sizePolicy6)
        self.chatPage_msgPlanEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: Transparent;\n"
"	border: none;\n"
"	color: rgb(241, 241, 241);\n"
"	\n"
"	font: 11pt \"Roboto\";\n"
"}")
        self.chatPage_msgPlanEdit.setFrameShape(QFrame.NoFrame)
        self.chatPage_msgPlanEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.chatPage_msgPlanEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.chatPage_msgPlanEdit.setTabChangesFocus(False)
        self.chatPage_msgPlanEdit.setOverwriteMode(False)
        self.chatPage_msgPlanEdit.setMaximumBlockCount(0)

        self.horizontalLayout_5.addWidget(self.chatPage_msgPlanEdit)

        self.chatPage_btn_sendMsg = QPushButton(self.chatPage_msgBoxFrame)
        self.chatPage_btn_sendMsg.setObjectName(u"chatPage_btn_sendMsg")
        sizePolicy5.setHeightForWidth(self.chatPage_btn_sendMsg.sizePolicy().hasHeightForWidth())
        self.chatPage_btn_sendMsg.setSizePolicy(sizePolicy5)
        self.chatPage_btn_sendMsg.setMinimumSize(QSize(30, 30))
        self.chatPage_btn_sendMsg.setMaximumSize(QSize(30, 30))
        self.chatPage_btn_sendMsg.setCursor(QCursor(Qt.PointingHandCursor))
        self.chatPage_btn_sendMsg.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:  transparent;\n"
"	background-repeat: no-reperat;\n"
"	image: url(:/images/images/icons/icons8-send-24hover.png);\n"
"}\n"
"QPushButton:pressed {\n"
"	image: url(:/images/images/icons/icons8-send-24.png);\n"
"}")

        self.horizontalLayout_5.addWidget(self.chatPage_btn_sendMsg, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.chatPage_msgBoxFrame)


        self.verticalLayout_5.addWidget(self.chatPage_msgFrame)


        self.horizontalLayout_4.addWidget(self.pageChat_chatFrame)


        self.horizontalLayout_3.addWidget(self.frame)

        self.pageChat_chatActionsFrame = QFrame(self.pageChat)
        self.pageChat_chatActionsFrame.setObjectName(u"pageChat_chatActionsFrame")
        sizePolicy3.setHeightForWidth(self.pageChat_chatActionsFrame.sizePolicy().hasHeightForWidth())
        self.pageChat_chatActionsFrame.setSizePolicy(sizePolicy3)
        self.pageChat_chatActionsFrame.setMinimumSize(QSize(300, 0))
        self.pageChat_chatActionsFrame.setMaximumSize(QSize(300, 16777215))
        self.pageChat_chatActionsFrame.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.pageChat_chatActionsFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.pageChat_chatActionsFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.chatPage_ClientPage = QWidget()
        self.chatPage_ClientPage.setObjectName(u"chatPage_ClientPage")
        self.chatPage_ClientPage.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.chatPage_ClientPage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.chatPage_OptionsScrollArea = QScrollArea(self.chatPage_ClientPage)
        self.chatPage_OptionsScrollArea.setObjectName(u"chatPage_OptionsScrollArea")
        self.chatPage_OptionsScrollArea.setStyleSheet(u"background-color: rgb(54, 57, 63);")
        self.chatPage_OptionsScrollArea.setFrameShape(QFrame.NoFrame)
        self.chatPage_OptionsScrollArea.setFrameShadow(QFrame.Plain)
        self.chatPage_OptionsScrollArea.setLineWidth(0)
        self.chatPage_OptionsScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.chatPage_OptionsScrollArea.setWidgetResizable(True)
        self.chatPage_OptionsFrame = QWidget()
        self.chatPage_OptionsFrame.setObjectName(u"chatPage_OptionsFrame")
        self.chatPage_OptionsFrame.setGeometry(QRect(0, 0, 300, 441))
        self.chatPage_OptionsFrame.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.chatPage_OptionsFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.chatPage_lineEdit_userName = QLineEdit(self.chatPage_OptionsFrame)
        self.chatPage_lineEdit_userName.setObjectName(u"chatPage_lineEdit_userName")
        sizePolicy3.setHeightForWidth(self.chatPage_lineEdit_userName.sizePolicy().hasHeightForWidth())
        self.chatPage_lineEdit_userName.setSizePolicy(sizePolicy3)
        self.chatPage_lineEdit_userName.setMinimumSize(QSize(0, 30))
        self.chatPage_lineEdit_userName.setMaximumSize(QSize(16777215, 30))
        self.chatPage_lineEdit_userName.setStyleSheet(u"")
        self.chatPage_lineEdit_userName.setMaxLength(30)
        self.chatPage_lineEdit_userName.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.chatPage_lineEdit_userName.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.chatPage_lineEdit_userName, 5, 0, 1, 3, Qt.AlignTop)

        self.label_6 = QLabel(self.chatPage_OptionsFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setStyleSheet(u"QLabel {\n"
"	border-radius: 5px;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 2, Qt.AlignTop)

        self.chatPage_btn_Connect = QPushButton(self.chatPage_OptionsFrame)
        self.chatPage_btn_Connect.setObjectName(u"chatPage_btn_Connect")
        self.chatPage_btn_Connect.setMinimumSize(QSize(0, 35))
        self.chatPage_btn_Connect.setMaximumSize(QSize(16777215, 35))
        self.chatPage_btn_Connect.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(92, 108, 255);\n"
"	border-radius: 5px;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"	border-left: 2px solid  rgb(233, 12, 89); /*rgb(189, 255, 0);*/\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(71, 82, 196);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(60, 69, 165);\n"
"}")
        self.chatPage_btn_Connect.setIconSize(QSize(24, 24))
        self.chatPage_btn_Connect.setCheckable(False)
        self.chatPage_btn_Connect.setAutoRepeat(False)
        self.chatPage_btn_Connect.setAutoExclusive(False)
        self.chatPage_btn_Connect.setFlat(False)

        self.gridLayout.addWidget(self.chatPage_btn_Connect, 0, 0, 2, 4)

        self.label_5 = QLabel(self.chatPage_OptionsFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setStyleSheet(u"QLabel {\n"
"	border-radius: 5px;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.label_5, 2, 3, 1, 1, Qt.AlignTop)

        self.chatPage_lineEdit_Ip = QLineEdit(self.chatPage_OptionsFrame)
        self.chatPage_lineEdit_Ip.setObjectName(u"chatPage_lineEdit_Ip")
        self.chatPage_lineEdit_Ip.setMinimumSize(QSize(0, 30))
        self.chatPage_lineEdit_Ip.setMaximumSize(QSize(16777215, 30))
        self.chatPage_lineEdit_Ip.setStyleSheet(u"")
        self.chatPage_lineEdit_Ip.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.chatPage_lineEdit_Ip, 3, 0, 1, 3, Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 2, 1, 1)

        self.chatPage_ChangePicFrame = QFrame(self.chatPage_OptionsFrame)
        self.chatPage_ChangePicFrame.setObjectName(u"chatPage_ChangePicFrame")
        self.chatPage_ChangePicFrame.setMinimumSize(QSize(40, 60))
        self.chatPage_ChangePicFrame.setMaximumSize(QSize(40, 60))
        self.chatPage_ChangePicFrame.setFrameShape(QFrame.StyledPanel)
        self.chatPage_ChangePicFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.chatPage_ChangePicFrame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.chatPage_Label_pic = QLabel(self.chatPage_ChangePicFrame)
        self.chatPage_Label_pic.setObjectName(u"chatPage_Label_pic")
        self.chatPage_Label_pic.setStyleSheet(u"")
        self.chatPage_Label_pic.setPixmap(QPixmap(u":/images/images/img/rand_1.jpg"))
        self.chatPage_Label_pic.setScaledContents(True)

        self.verticalLayout_9.addWidget(self.chatPage_Label_pic)

        self.chatPage_BtnChangePicture = QPushButton(self.chatPage_ChangePicFrame)
        self.chatPage_BtnChangePicture.setObjectName(u"chatPage_BtnChangePicture")
        self.chatPage_BtnChangePicture.setMinimumSize(QSize(0, 20))
        self.chatPage_BtnChangePicture.setMaximumSize(QSize(16777215, 20))
        self.chatPage_BtnChangePicture.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(82, 89, 96);\n"
"	border-bottom-right-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	font: 700 7pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(68, 73, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(61, 66, 71);\n"
"}")

        self.verticalLayout_9.addWidget(self.chatPage_BtnChangePicture)


        self.gridLayout.addWidget(self.chatPage_ChangePicFrame, 4, 3, 2, 1, Qt.AlignHCenter)

        self.label_4 = QLabel(self.chatPage_OptionsFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setStyleSheet(u"QLabel {\n"
"	border-radius: 5px;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 2)

        self.chatPage_lineEdit_Port = QLineEdit(self.chatPage_OptionsFrame)
        self.chatPage_lineEdit_Port.setObjectName(u"chatPage_lineEdit_Port")
        self.chatPage_lineEdit_Port.setMinimumSize(QSize(100, 30))
        self.chatPage_lineEdit_Port.setMaximumSize(QSize(100, 30))
        self.chatPage_lineEdit_Port.setStyleSheet(u"")
        self.chatPage_lineEdit_Port.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.chatPage_lineEdit_Port, 3, 3, 1, 1, Qt.AlignTop)

        self.chatPage_OptionsScrollArea.setWidget(self.chatPage_OptionsFrame)

        self.verticalLayout_10.addWidget(self.chatPage_OptionsScrollArea)

        self.tabWidget.addTab(self.chatPage_ClientPage, "")
        self.chatPage_ServerPage = QWidget()
        self.chatPage_ServerPage.setObjectName(u"chatPage_ServerPage")
        self.verticalLayout_12 = QVBoxLayout(self.chatPage_ServerPage)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.chatPage_OptionsScrollArea_2 = QScrollArea(self.chatPage_ServerPage)
        self.chatPage_OptionsScrollArea_2.setObjectName(u"chatPage_OptionsScrollArea_2")
        self.chatPage_OptionsScrollArea_2.setStyleSheet(u"background-color: rgb(54, 57, 63);")
        self.chatPage_OptionsScrollArea_2.setFrameShape(QFrame.NoFrame)
        self.chatPage_OptionsScrollArea_2.setFrameShadow(QFrame.Plain)
        self.chatPage_OptionsScrollArea_2.setLineWidth(0)
        self.chatPage_OptionsScrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.chatPage_OptionsScrollArea_2.setWidgetResizable(True)
        self.chatPage_OptionsFrame_2 = QWidget()
        self.chatPage_OptionsFrame_2.setObjectName(u"chatPage_OptionsFrame_2")
        self.chatPage_OptionsFrame_2.setGeometry(QRect(0, 0, 298, 748))
        self.chatPage_OptionsFrame_2.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.chatPage_OptionsFrame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_3 = QLabel(self.chatPage_OptionsFrame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label_10 = QLabel(self.chatPage_OptionsFrame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.label_10)


        self.gridLayout_2.addLayout(self.horizontalLayout_10, 6, 2, 1, 1)

        self.chatPage_fileSizeTraffic = QSlider(self.chatPage_OptionsFrame_2)
        self.chatPage_fileSizeTraffic.setObjectName(u"chatPage_fileSizeTraffic")
        sizePolicy3.setHeightForWidth(self.chatPage_fileSizeTraffic.sizePolicy().hasHeightForWidth())
        self.chatPage_fileSizeTraffic.setSizePolicy(sizePolicy3)
        self.chatPage_fileSizeTraffic.setStyleSheet(u"")
        self.chatPage_fileSizeTraffic.setMinimum(0)
        self.chatPage_fileSizeTraffic.setMaximum(1024)
        self.chatPage_fileSizeTraffic.setSingleStep(1)
        self.chatPage_fileSizeTraffic.setPageStep(10)
        self.chatPage_fileSizeTraffic.setValue(0)
        self.chatPage_fileSizeTraffic.setOrientation(Qt.Horizontal)
        self.chatPage_fileSizeTraffic.setInvertedAppearance(False)
        self.chatPage_fileSizeTraffic.setInvertedControls(False)

        self.gridLayout_2.addWidget(self.chatPage_fileSizeTraffic, 6, 1, 1, 1)

        self.chatPage_lineEdit_cmd = QPlainTextEdit(self.chatPage_OptionsFrame_2)
        self.chatPage_lineEdit_cmd.setObjectName(u"chatPage_lineEdit_cmd")
        self.chatPage_lineEdit_cmd.setMinimumSize(QSize(274, 130))
        self.chatPage_lineEdit_cmd.setMaximumSize(QSize(274, 130))
        self.chatPage_lineEdit_cmd.setFrameShape(QFrame.NoFrame)
        self.chatPage_lineEdit_cmd.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.chatPage_lineEdit_cmd, 13, 1, 1, 2)

        self.chatPage_btn_Host = QPushButton(self.chatPage_OptionsFrame_2)
        self.chatPage_btn_Host.setObjectName(u"chatPage_btn_Host")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.chatPage_btn_Host.sizePolicy().hasHeightForWidth())
        self.chatPage_btn_Host.setSizePolicy(sizePolicy7)
        self.chatPage_btn_Host.setMinimumSize(QSize(0, 35))
        self.chatPage_btn_Host.setMaximumSize(QSize(274, 35))
        self.chatPage_btn_Host.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(92, 108, 255);\n"
"	border-radius: 5px;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"	border-left: 2px solid  rgb(233, 12, 89);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(71, 82, 196);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(60, 69, 165);\n"
"}")
        self.chatPage_btn_Host.setIconSize(QSize(24, 24))
        self.chatPage_btn_Host.setCheckable(False)
        self.chatPage_btn_Host.setChecked(False)
        self.chatPage_btn_Host.setAutoRepeat(False)
        self.chatPage_btn_Host.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.chatPage_btn_Host, 0, 1, 1, 3)

        self.chatPage_listWidget_hostClients = QListWidget(self.chatPage_OptionsFrame_2)
        self.chatPage_listWidget_hostClients.setObjectName(u"chatPage_listWidget_hostClients")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.chatPage_listWidget_hostClients.sizePolicy().hasHeightForWidth())
        self.chatPage_listWidget_hostClients.setSizePolicy(sizePolicy8)
        self.chatPage_listWidget_hostClients.setMinimumSize(QSize(274, 130))
        self.chatPage_listWidget_hostClients.setMaximumSize(QSize(274, 130))
        self.chatPage_listWidget_hostClients.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 10pt \"Terminal\";")
        self.chatPage_listWidget_hostClients.setSpacing(2)

        self.gridLayout_2.addWidget(self.chatPage_listWidget_hostClients, 8, 1, 1, 3)

        self.listWidget_2 = QListWidget(self.chatPage_OptionsFrame_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setMinimumSize(QSize(274, 130))
        self.listWidget_2.setMaximumSize(QSize(274, 130))
        self.listWidget_2.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 10pt \"Terminal\";")
        self.listWidget_2.setFlow(QListView.TopToBottom)
        self.listWidget_2.setProperty("isWrapping", False)
        self.listWidget_2.setResizeMode(QListView.Fixed)
        self.listWidget_2.setLayoutMode(QListView.SinglePass)
        self.listWidget_2.setSpacing(2)

        self.gridLayout_2.addWidget(self.listWidget_2, 11, 1, 1, 3)

        self.label_13 = QLabel(self.chatPage_OptionsFrame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 20))
        self.label_13.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_13, 7, 1, 1, 1)

        self.label_14 = QLabel(self.chatPage_OptionsFrame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 20))
        self.label_14.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_14, 12, 1, 1, 1)

        self.label_12 = QLabel(self.chatPage_OptionsFrame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))
        self.label_12.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_12, 10, 1, 1, 3)

        self.chatPage_lineEdit_HostPort = QLineEdit(self.chatPage_OptionsFrame_2)
        self.chatPage_lineEdit_HostPort.setObjectName(u"chatPage_lineEdit_HostPort")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.chatPage_lineEdit_HostPort.sizePolicy().hasHeightForWidth())
        self.chatPage_lineEdit_HostPort.setSizePolicy(sizePolicy9)
        self.chatPage_lineEdit_HostPort.setMinimumSize(QSize(70, 30))
        self.chatPage_lineEdit_HostPort.setMaximumSize(QSize(70, 30))
        self.chatPage_lineEdit_HostPort.setStyleSheet(u"")
        self.chatPage_lineEdit_HostPort.setEchoMode(QLineEdit.Normal)
        self.chatPage_lineEdit_HostPort.setReadOnly(True)
        self.chatPage_lineEdit_HostPort.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.chatPage_lineEdit_HostPort, 2, 2, 1, 1)

        self.chatPage_cbox_HostType = QComboBox(self.chatPage_OptionsFrame_2)
        self.chatPage_cbox_HostType.addItem("")
        self.chatPage_cbox_HostType.addItem("")
        self.chatPage_cbox_HostType.setObjectName(u"chatPage_cbox_HostType")
        self.chatPage_cbox_HostType.setMinimumSize(QSize(274, 0))
        self.chatPage_cbox_HostType.setMaximumSize(QSize(274, 16777215))
        self.chatPage_cbox_HostType.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.chatPage_cbox_HostType, 4, 1, 1, 3)

        self.label_15 = QLabel(self.chatPage_OptionsFrame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_15, 3, 1, 1, 1)

        self.chatPage_btn_execCmd = QPushButton(self.chatPage_OptionsFrame_2)
        self.chatPage_btn_execCmd.setObjectName(u"chatPage_btn_execCmd")
        sizePolicy7.setHeightForWidth(self.chatPage_btn_execCmd.sizePolicy().hasHeightForWidth())
        self.chatPage_btn_execCmd.setSizePolicy(sizePolicy7)
        self.chatPage_btn_execCmd.setMinimumSize(QSize(0, 35))
        self.chatPage_btn_execCmd.setMaximumSize(QSize(274, 35))
        self.chatPage_btn_execCmd.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(92, 108, 255);\n"
"	border-radius: 5px;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"	border-left: 2px solid  rgb(233, 12, 89); /*rgb(189, 255, 0);*/\n"
"	text-align: left;\n"
"	padding-left: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(71, 82, 196);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(60, 69, 165);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/images/icons/cil-terminal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chatPage_btn_execCmd.setIcon(icon)
        self.chatPage_btn_execCmd.setIconSize(QSize(24, 24))
        self.chatPage_btn_execCmd.setCheckable(False)
        self.chatPage_btn_execCmd.setChecked(False)
        self.chatPage_btn_execCmd.setAutoRepeat(False)
        self.chatPage_btn_execCmd.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.chatPage_btn_execCmd, 14, 1, 1, 1)

        self.label_7 = QLabel(self.chatPage_OptionsFrame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)

        self.label_9 = QLabel(self.chatPage_OptionsFrame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))
        self.label_9.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_9, 5, 1, 1, 1)

        self.label_8 = QLabel(self.chatPage_OptionsFrame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 20))
        self.label_8.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)

        self.chatPage_lineEdit_Ip_server = QLineEdit(self.chatPage_OptionsFrame_2)
        self.chatPage_lineEdit_Ip_server.setObjectName(u"chatPage_lineEdit_Ip_server")
        self.chatPage_lineEdit_Ip_server.setMinimumSize(QSize(0, 30))
        self.chatPage_lineEdit_Ip_server.setMaximumSize(QSize(16777215, 30))
        self.chatPage_lineEdit_Ip_server.setStyleSheet(u"")
        self.chatPage_lineEdit_Ip_server.setReadOnly(True)
        self.chatPage_lineEdit_Ip_server.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.chatPage_lineEdit_Ip_server, 2, 1, 1, 1)

        self.chatPage_OptionsScrollArea_2.setWidget(self.chatPage_OptionsFrame_2)

        self.verticalLayout_12.addWidget(self.chatPage_OptionsScrollArea_2)

        self.tabWidget.addTab(self.chatPage_ServerPage, "")

        self.horizontalLayout_7.addWidget(self.tabWidget)


        self.horizontalLayout_3.addWidget(self.pageChat_chatActionsFrame)

        self.stackedWidget.addWidget(self.pageChat)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.stackedWidget.addWidget(self.page3)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.bottomFrame = QFrame(self.midFrame)
        self.bottomFrame.setObjectName(u"bottomFrame")
        sizePolicy.setHeightForWidth(self.bottomFrame.sizePolicy().hasHeightForWidth())
        self.bottomFrame.setSizePolicy(sizePolicy)
        self.bottomFrame.setMinimumSize(QSize(0, 40))
        self.bottomFrame.setMaximumSize(QSize(16777215, 40))
        self.bottomFrame.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.bottomFrame_checkBox_cpuToggle = QRadioButton(self.bottomFrame)
        self.bottomFrame_checkBox_cpuToggle.setObjectName(u"bottomFrame_checkBox_cpuToggle")
        self.bottomFrame_checkBox_cpuToggle.setMaximumSize(QSize(21, 21))
        self.bottomFrame_checkBox_cpuToggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.bottomFrame_checkBox_cpuToggle.setStyleSheet(u"QRadioButton::indicator {\n"
"    border: 2px solid rgb(103, 103, 103);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid rgb(141, 141, 141);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(186, 251, 0);\n"
"}")

        self.horizontalLayout_11.addWidget(self.bottomFrame_checkBox_cpuToggle)

        self.label_11 = QLabel(self.bottomFrame)
        self.label_11.setObjectName(u"label_11")
        sizePolicy5.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy5)
        self.label_11.setMaximumSize(QSize(16777215, 20))
        self.label_11.setStyleSheet(u"")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.chatPage_CPUprogressBar = QProgressBar(self.bottomFrame)
        self.chatPage_CPUprogressBar.setObjectName(u"chatPage_CPUprogressBar")
        sizePolicy9.setHeightForWidth(self.chatPage_CPUprogressBar.sizePolicy().hasHeightForWidth())
        self.chatPage_CPUprogressBar.setSizePolicy(sizePolicy9)
        self.chatPage_CPUprogressBar.setMinimumSize(QSize(225, 8))
        self.chatPage_CPUprogressBar.setMaximumSize(QSize(225, 8))
        self.chatPage_CPUprogressBar.setStyleSheet(u"")
        self.chatPage_CPUprogressBar.setMinimum(0)
        self.chatPage_CPUprogressBar.setMaximum(100)
        self.chatPage_CPUprogressBar.setValue(0)
        self.chatPage_CPUprogressBar.setTextVisible(True)
        self.chatPage_CPUprogressBar.setInvertedAppearance(False)
        self.chatPage_CPUprogressBar.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_11.addWidget(self.chatPage_CPUprogressBar)


        self.verticalLayout_3.addWidget(self.bottomFrame)


        self.horizontalLayout.addWidget(self.midFrame)


        self.verticalLayout_2.addWidget(self.containerFrame)


        self.verticalLayout.addWidget(self.styleSheet)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.chatPage_fileSizeTraffic.valueChanged.connect(self.label_3.setNum)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Net Box", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"v1.0.0 (64-bit)", None))
        self.btnPageChat.setText("")
        self.btnPage2.setText("")
        self.btnPage3.setText("")
        self.chatPage_Label_ConnStatue.setText(QCoreApplication.translate("MainWindow", u"Offline", None))
#if QT_CONFIG(tooltip)
        self.chatPage_btn_sendFile.setToolTip(QCoreApplication.translate("MainWindow", u"add file", None))
#endif // QT_CONFIG(tooltip)
        self.chatPage_btn_sendFile.setText("")
#if QT_CONFIG(tooltip)
        self.chatPage_msgPlanEdit.setToolTip(QCoreApplication.translate("MainWindow", u"send:ctrl+enter", None))
#endif // QT_CONFIG(tooltip)
        self.chatPage_msgPlanEdit.setPlainText("")
        self.chatPage_msgPlanEdit.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.chatPage_btn_sendMsg.setToolTip(QCoreApplication.translate("MainWindow", u"ctrl+enter", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.chatPage_btn_sendMsg.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.chatPage_btn_sendMsg.setText("")
#if QT_CONFIG(shortcut)
        self.chatPage_btn_sendMsg.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.chatPage_lineEdit_userName.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.chatPage_lineEdit_userName.setInputMask("")
        self.chatPage_lineEdit_userName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"cool name bro", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.chatPage_btn_Connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.chatPage_lineEdit_Ip.setInputMask("")
        self.chatPage_lineEdit_Ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.chatPage_Label_pic.setText("")
#if QT_CONFIG(tooltip)
        self.chatPage_BtnChangePicture.setToolTip(QCoreApplication.translate("MainWindow", u"generate image from your user name", None))
#endif // QT_CONFIG(tooltip)
        self.chatPage_BtnChangePicture.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"User name", None))
        self.chatPage_lineEdit_Port.setInputMask("")
        self.chatPage_lineEdit_Port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PORT", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chatPage_ClientPage), QCoreApplication.translate("MainWindow", u"Client", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"MB", None))
        self.chatPage_lineEdit_cmd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"->", None))
        self.chatPage_btn_Host.setText(QCoreApplication.translate("MainWindow", u"Host Server", None))

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_2.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"->TimeOut<clientId><Min>", None));
        ___qlistwidgetitem1 = self.listWidget_2.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"->IpBan<clientId>", None));
        ___qlistwidgetitem2 = self.listWidget_2.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"->PS<clientId><cmd/ps1>", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled)

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Execute command", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Available commands", None))
        self.chatPage_lineEdit_HostPort.setInputMask("")
        self.chatPage_lineEdit_HostPort.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PORT", None))
        self.chatPage_cbox_HostType.setItemText(0, QCoreApplication.translate("MainWindow", u"LAN", None))
        self.chatPage_cbox_HostType.setItemText(1, QCoreApplication.translate("MainWindow", u"WAN", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Host type", None))
        self.chatPage_btn_execCmd.setText(QCoreApplication.translate("MainWindow", u"Exec", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Maximum file size traffic", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.chatPage_lineEdit_Ip_server.setInputMask("")
        self.chatPage_lineEdit_Ip_server.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chatPage_ServerPage), QCoreApplication.translate("MainWindow", u"Server", None))
#if QT_CONFIG(tooltip)
        self.bottomFrame_checkBox_cpuToggle.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle CpuUsage", None))
#endif // QT_CONFIG(tooltip)
        self.bottomFrame_checkBox_cpuToggle.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.chatPage_CPUprogressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
    # retranslateUi

