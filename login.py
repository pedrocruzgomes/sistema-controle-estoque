# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(611, 581)
        Login.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color: rgb(205,92,92);\n"
"}")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 60, 491, 461))
        self.frame.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color: rgb(240,128,128);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(190, 390, 110, 30))
        self.btn_login.setMinimumSize(QSize(110, 30))
        self.btn_login.setMaximumSize(QSize(110, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton::hover{\n"
"border-radius:15px;\n"
"background-color:rgb(205,92,92);\n"
"color:rgb(255,255,255);\n"
"}\n"
"QPushButton{\n"
"border-radius:15px;\n"
"background-color:rgb(0,0,0);\n"
"color:rgb(255,255,255);\n"
"}\n"
"")
        self.txt_senha = QLineEdit(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(160, 300, 171, 25))
        self.txt_senha.setMinimumSize(QSize(0, 25))
        self.txt_senha.setMaximumSize(QSize(16777215, 16777215))
        self.txt_senha.setStyleSheet(u"background-color:rgb(255,255,255)")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)
        self.txt_senha.setReadOnly(False)
        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(160, 230, 171, 25))
        self.txt_user.setMinimumSize(QSize(0, 25))
        self.txt_user.setMaximumSize(QSize(16777215, 25))
        self.txt_user.setLayoutDirection(Qt.LeftToRight)
        self.txt_user.setStyleSheet(u"background-color:rgb(255,255,255)")
        self.txt_user.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 20, 191, 181))
        self.label.setPixmap(QPixmap(u"icones/login.png"))
        self.label.setScaledContents(True)
        self.label.raise_()
        self.btn_login.raise_()
        self.txt_senha.raise_()
        self.txt_user.raise_()
        QWidget.setTabOrder(self.txt_user, self.txt_senha)
        QWidget.setTabOrder(self.txt_senha, self.btn_login)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.txt_user.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.label.setText("")
    # retranslateUi

