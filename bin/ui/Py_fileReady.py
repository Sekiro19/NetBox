# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_fileReady.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_FileReady(QWidget):
    def setupUi(self, FileReady):
        if not FileReady.objectName():
            FileReady.setObjectName(u"FileReady")
        FileReady.resize(216, 40)
        FileReady.setMinimumSize(QSize(0, 40))
        FileReady.setMaximumSize(QSize(16777215, 40))
        self.verticalLayout = QVBoxLayout(FileReady)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(FileReady)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(47, 49, 54);\n"
"	border-radius: 10px;\n"
"	color: rgb(211, 214, 253);\n"
"	font: 11pt \"Roboto\";\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_fileName = QLabel(self.frame)
        self.label_fileName.setObjectName(u"label_fileName")

        self.horizontalLayout_2.addWidget(self.label_fileName)

        self.btn_binFile = QPushButton(self.frame)
        self.btn_binFile.setObjectName(u"btn_binFile")
        self.btn_binFile.setMinimumSize(QSize(25, 25))
        self.btn_binFile.setMaximumSize(QSize(25, 25))
        self.btn_binFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_binFile.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/images/images/icons/icons8-trash-bin-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_binFile.setIcon(icon)
        self.btn_binFile.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.btn_binFile)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(FileReady)

        QMetaObject.connectSlotsByName(FileReady)
    # setupUi

    def retranslateUi(self, FileReady):
        FileReady.setWindowTitle(QCoreApplication.translate("FileReady", u"Frame", None))
        self.label_fileName.setText(QCoreApplication.translate("FileReady", u"TextFile.txt", None))
        self.btn_binFile.setText("")
    # retranslateUi

