# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_fileDownload.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_FileDownload(QWidget):
    def setupUi(self, FileDownload):
        if not FileDownload.objectName():
            FileDownload.setObjectName(u"FileDownload")
        FileDownload.resize(387, 40)
        FileDownload.setMinimumSize(QSize(0, 40))
        FileDownload.setMaximumSize(QSize(16777215, 40))
        self.verticalLayout_3 = QVBoxLayout(FileDownload)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(FileDownload)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(47, 49, 54);\n"
"	border-radius: 10px;\n"
"	color: rgb(211, 214, 253);\n"
"	font: 11pt \"Roboto\";\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_fileName = QLabel(self.frame)
        self.label_fileName.setObjectName(u"label_fileName")

        self.horizontalLayout_2.addWidget(self.label_fileName)

        self.btn_downloadFile = QPushButton(self.frame)
        self.btn_downloadFile.setObjectName(u"btn_downloadFile")
        self.btn_downloadFile.setMinimumSize(QSize(25, 25))
        self.btn_downloadFile.setMaximumSize(QSize(25, 25))
        self.btn_downloadFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_downloadFile.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	background-color:  transparent;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(103, 110, 121);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:  rgb(85, 90, 99);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/images/icons/icons8-download-24 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_downloadFile.setIcon(icon)
        self.btn_downloadFile.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.btn_downloadFile)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.fileProgressBar = QProgressBar(self.frame)
        self.fileProgressBar.setObjectName(u"fileProgressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fileProgressBar.sizePolicy().hasHeightForWidth())
        self.fileProgressBar.setSizePolicy(sizePolicy1)
        self.fileProgressBar.setMinimumSize(QSize(0, 2))
        self.fileProgressBar.setMaximumSize(QSize(16777215, 2))
        self.fileProgressBar.setStyleSheet(u"QProgressBar {\n"
"    background: rgb(112, 118, 130);\n"
"	color: rgb(233, 12, 89);\n"
"	font: 7pt \"Roboto\";\n"
"	text-align: right;\n"
"    border-radius: 4px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(189, 255, 0);\n"
"    border-radius: 3px;\n"
"}")
        self.fileProgressBar.setMinimum(0)
        self.fileProgressBar.setMaximum(100)
        self.fileProgressBar.setValue(0)
        self.fileProgressBar.setTextVisible(False)
        self.fileProgressBar.setInvertedAppearance(False)
        self.fileProgressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_4.addWidget(self.fileProgressBar)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.retranslateUi(FileDownload)

        QMetaObject.connectSlotsByName(FileDownload)
    # setupUi

    def retranslateUi(self, FileDownload):
        FileDownload.setWindowTitle(QCoreApplication.translate("FileDownload", u"Frame", None))
        self.label_fileName.setText(QCoreApplication.translate("FileDownload", u"TextFile.txt", None))
        self.btn_downloadFile.setText("")
        self.fileProgressBar.setFormat(QCoreApplication.translate("FileDownload", u"%p%", None))
    # retranslateUi

