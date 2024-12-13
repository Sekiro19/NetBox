# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_chatMsg.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPlainTextEdit, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_ChatMsg(QWidget):
    def setupUi(self, ChatMsg):
        if not ChatMsg.objectName():
            ChatMsg.setObjectName(u"ChatMsg")
        ChatMsg.resize(437, 139)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChatMsg.sizePolicy().hasHeightForWidth())
        ChatMsg.setSizePolicy(sizePolicy)
        ChatMsg.setMinimumSize(QSize(0, 0))
        ChatMsg.setMaximumSize(QSize(16777215, 16777215))
        ChatMsg.setStyleSheet(u"background-color: transparent;")
        self.verticalLayout = QVBoxLayout(ChatMsg)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(ChatMsg)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setBaseSize(QSize(0, 0))
        self.frame.setStyleSheet(u"#frame {\n"
"	background-color: rgb(54, 57, 63);\n"
"	border-radius: 10px;\n"
"}\n"
"#frame:hover {\n"
"	background-color: rgb(47, 49, 54)\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.vBoxMain = QVBoxLayout()
        self.vBoxMain.setSpacing(0)
        self.vBoxMain.setObjectName(u"vBoxMain")
        self.hBoxTop = QHBoxLayout()
        self.hBoxTop.setSpacing(10)
        self.hBoxTop.setObjectName(u"hBoxTop")
        self.label_img = QLabel(self.frame)
        self.label_img.setObjectName(u"label_img")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_img.sizePolicy().hasHeightForWidth())
        self.label_img.setSizePolicy(sizePolicy1)
        self.label_img.setMinimumSize(QSize(40, 40))
        self.label_img.setMaximumSize(QSize(40, 40))
        self.label_img.setStyleSheet(u"background-color: transparent;")
        self.label_img.setPixmap(QPixmap(u":/images/images/img/rand_1.jpg"))
        self.label_img.setScaledContents(True)

        self.hBoxTop.addWidget(self.label_img)

        self.label_UserName = QLabel(self.frame)
        self.label_UserName.setObjectName(u"label_UserName")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_UserName.sizePolicy().hasHeightForWidth())
        self.label_UserName.setSizePolicy(sizePolicy2)
        self.label_UserName.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: Transparent;\n"
"	font: 700 11pt \"Roboto\";\n"
"}")
        self.label_UserName.setWordWrap(True)

        self.hBoxTop.addWidget(self.label_UserName)

        self.label_date = QLabel(self.frame)
        self.label_date.setObjectName(u"label_date")
        sizePolicy2.setHeightForWidth(self.label_date.sizePolicy().hasHeightForWidth())
        self.label_date.setSizePolicy(sizePolicy2)
        self.label_date.setStyleSheet(u"QLabel {\n"
"	background-color: Transparent;\n"
"	color: rgb(156, 156, 156);\n"
"	font: 8pt \"Roboto\";\n"
"}")
        self.label_date.setWordWrap(True)

        self.hBoxTop.addWidget(self.label_date)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hBoxTop.addItem(self.horizontalSpacer)


        self.vBoxMain.addLayout(self.hBoxTop)

        self.vBox_bottom = QVBoxLayout()
        self.vBox_bottom.setSpacing(6)
        self.vBox_bottom.setObjectName(u"vBox_bottom")
        self.vBox_bottom.setContentsMargins(40, -1, -1, -1)
        self.msgContentPlanEdit = QPlainTextEdit(self.frame)
        self.msgContentPlanEdit.setObjectName(u"msgContentPlanEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.msgContentPlanEdit.sizePolicy().hasHeightForWidth())
        self.msgContentPlanEdit.setSizePolicy(sizePolicy3)
        self.msgContentPlanEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: Transparent;\n"
"	border: none;\n"
"	color: rgb(241, 241, 241);\n"
"	\n"
"	font: 11pt \"Roboto\";\n"
"}")
        self.msgContentPlanEdit.setFrameShape(QFrame.NoFrame)
        self.msgContentPlanEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.msgContentPlanEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.msgContentPlanEdit.setReadOnly(True)
        self.msgContentPlanEdit.setTabStopDistance(81.000000000000000)

        self.vBox_bottom.addWidget(self.msgContentPlanEdit)

        self.scrollArea_files = QScrollArea(self.frame)
        self.scrollArea_files.setObjectName(u"scrollArea_files")
        sizePolicy.setHeightForWidth(self.scrollArea_files.sizePolicy().hasHeightForWidth())
        self.scrollArea_files.setSizePolicy(sizePolicy)
        self.scrollArea_files.setMinimumSize(QSize(0, 0))
        self.scrollArea_files.setMaximumSize(QSize(16777215, 0))
        self.scrollArea_files.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(64, 68, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.scrollArea_files.setFrameShape(QFrame.NoFrame)
        self.scrollArea_files.setFrameShadow(QFrame.Plain)
        self.scrollArea_files.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_files.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 376, 40))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"background-color: Transparent;")
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.hBox_files = QHBoxLayout()
        self.hBox_files.setSpacing(15)
        self.hBox_files.setObjectName(u"hBox_files")
        self.hBox_files.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hBox_files.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.hBox_files)

        self.scrollArea_files.setWidget(self.scrollAreaWidgetContents_3)

        self.vBox_bottom.addWidget(self.scrollArea_files)


        self.vBoxMain.addLayout(self.vBox_bottom)


        self.verticalLayout_2.addLayout(self.vBoxMain)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(ChatMsg)

        QMetaObject.connectSlotsByName(ChatMsg)
    # setupUi

    def retranslateUi(self, ChatMsg):
        ChatMsg.setWindowTitle(QCoreApplication.translate("ChatMsg", u"Frame", None))
        self.label_img.setText("")
        self.label_UserName.setText(QCoreApplication.translate("ChatMsg", u"Sekiro", None))
        self.label_date.setText(QCoreApplication.translate("ChatMsg", u"Today at 00:20", None))
        self.msgContentPlanEdit.setPlainText("")
    # retranslateUi

