# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sistema.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableView, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1088, 644)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color: rgb(205,92,92);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menu = QFrame(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(0, 0))
        self.menu.setMaximumSize(QSize(0, 16777215))
        self.menu.setStyleSheet(u"QFrame{\n"
"background-color:rgb(0,0,0)\n"
"}")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.menu)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(self.menu)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: rgb(205,92,92);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(25)
        font.setBold(True)
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.btn_cad_prod = QPushButton(self.frame)
        self.btn_cad_prod.setObjectName(u"btn_cad_prod")
        self.btn_cad_prod.setMinimumSize(QSize(180, 40))
        font1 = QFont()
        font1.setFamilies([u"Ink Free"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.btn_cad_prod.setFont(font1)
        self.btn_cad_prod.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cad_prod.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(255,165,0);\n"
"border-radius:15px;\n"
"color:rgb(255,255,255);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(0,0,0);\n"
"border-radius:15px;\n"
"color:rgb(255,255,255);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icones/cadastrar produto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cad_prod.setIcon(icon)
        self.btn_cad_prod.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_cad_prod)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_estoque = QPushButton(self.frame)
        self.btn_estoque.setObjectName(u"btn_estoque")
        self.btn_estoque.setMinimumSize(QSize(180, 40))
        self.btn_estoque.setFont(font1)
        self.btn_estoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_estoque.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(188,143,143);\n"
"border-radius:15px;\n"
"color:rgb(255,255,255);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(0,0,0);\n"
"border-radius:15px;\n"
"color:rgb(255,255,255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icones/estoque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_estoque.setIcon(icon1)
        self.btn_estoque.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_estoque)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.btn_cad_user = QPushButton(self.frame)
        self.btn_cad_user.setObjectName(u"btn_cad_user")
        self.btn_cad_user.setMinimumSize(QSize(180, 40))
        self.btn_cad_user.setFont(font1)
        self.btn_cad_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cad_user.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(46,139,87);\n"
"border-radius:15px;\n"
"color:rgb(255,255,255);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(0,0,0);\n"
"border-radius:15px;\n"
"color:rgb(255,255,255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icones/cadastrar usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cad_user.setIcon(icon2)
        self.btn_cad_user.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_cad_user)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.btn_users = QPushButton(self.frame)
        self.btn_users.setObjectName(u"btn_users")
        self.btn_users.setMinimumSize(QSize(180, 40))
        self.btn_users.setFont(font1)
        self.btn_users.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_users.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(95,158,160);\n"
"border-radius:15px;\n"
"color:rgb(255,255,255);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(0,0,0);\n"
"border-radius:15px;\n"
"color:rgb(255,255,255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icones/usuarios.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_users.setIcon(icon3)
        self.btn_users.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_users)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.btn_sair = QPushButton(self.frame)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setMinimumSize(QSize(180, 40))
        self.btn_sair.setFont(font1)
        self.btn_sair.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sair.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(255,0,0);\n"
"border-radius:15px;\n"
"color:rgb(255,255,255);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(0,0,0);\n"
"border-radius:15px;\n"
"color:rgb(255,255,255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icones/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sair.setIcon(icon4)
        self.btn_sair.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_sair)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)


        self.horizontalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.menu)

        self.principal = QFrame(self.centralwidget)
        self.principal.setObjectName(u"principal")
        self.principal.setMinimumSize(QSize(0, 0))
        self.principal.setFrameShape(QFrame.StyledPanel)
        self.principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.principal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.principal)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_menu = QPushButton(self.frame_3)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu.setStyleSheet(u"border:none;")
        icon5 = QIcon()
        icon5.addFile(u"icones/principal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon5)
        self.btn_menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_menu, 0, Qt.AlignLeft)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.label.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.principal)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_4 = QVBoxLayout(self.pg_home)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.pg_home)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u"icones/armazenar.png"))

        self.verticalLayout_4.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.pg_home)
        self.pg_cad_prod = QWidget()
        self.pg_cad_prod.setObjectName(u"pg_cad_prod")
        self.horizontalLayout_11 = QHBoxLayout(self.pg_cad_prod)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_12 = QFrame(self.pg_cad_prod)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(100, 0))
        self.frame_12.setMaximumSize(QSize(100, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_12)

        self.frame_7 = QFrame(self.pg_cad_prod)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color:rgb(0,0,0)")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.frame_2 = QFrame(self.frame_7)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 200))
        self.frame_2.setMaximumSize(QSize(400, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(205,92,92);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_14.setFont(font3)

        self.verticalLayout_23.addWidget(self.label_14)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_12)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.verticalLayout_7.addWidget(self.label_9)

        self.txt_cod_prod = QLineEdit(self.frame_2)
        self.txt_cod_prod.setObjectName(u"txt_cod_prod")
        self.txt_cod_prod.setMinimumSize(QSize(200, 0))
        self.txt_cod_prod.setMaximumSize(QSize(16777215, 16777215))
        self.txt_cod_prod.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_7.addWidget(self.txt_cod_prod)


        self.verticalLayout_23.addLayout(self.verticalLayout_7)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.verticalLayout_8.addWidget(self.label_7)

        self.txt_desc_prod = QLineEdit(self.frame_2)
        self.txt_desc_prod.setObjectName(u"txt_desc_prod")
        self.txt_desc_prod.setMinimumSize(QSize(200, 0))
        self.txt_desc_prod.setMaximumSize(QSize(16777215, 16777215))
        self.txt_desc_prod.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_8.addWidget(self.txt_desc_prod)


        self.verticalLayout_23.addLayout(self.verticalLayout_8)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.verticalLayout_9.addWidget(self.label_8)

        self.txt_tipo_prod = QComboBox(self.frame_2)
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.addItem("")
        self.txt_tipo_prod.setObjectName(u"txt_tipo_prod")
        self.txt_tipo_prod.setMinimumSize(QSize(200, 0))
        self.txt_tipo_prod.setMaximumSize(QSize(16777215, 16777215))
        self.txt_tipo_prod.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_9.addWidget(self.txt_tipo_prod)


        self.verticalLayout_23.addLayout(self.verticalLayout_9)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_9)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.verticalLayout_12.addWidget(self.label_10)

        self.txt_cor_prod = QLineEdit(self.frame_2)
        self.txt_cor_prod.setObjectName(u"txt_cor_prod")
        self.txt_cor_prod.setMinimumSize(QSize(200, 0))
        self.txt_cor_prod.setMaximumSize(QSize(16777215, 16777215))
        self.txt_cor_prod.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_12.addWidget(self.txt_cor_prod)


        self.verticalLayout_23.addLayout(self.verticalLayout_12)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.verticalLayout_11.addWidget(self.label_13)

        self.txt_qntd_prod = QLineEdit(self.frame_2)
        self.txt_qntd_prod.setObjectName(u"txt_qntd_prod")
        self.txt_qntd_prod.setMinimumSize(QSize(200, 0))
        self.txt_qntd_prod.setMaximumSize(QSize(16777215, 16777215))
        self.txt_qntd_prod.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_11.addWidget(self.txt_qntd_prod)


        self.verticalLayout_23.addLayout(self.verticalLayout_11)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_11)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_12)

        self.txt_preco_prod = QLineEdit(self.frame_2)
        self.txt_preco_prod.setObjectName(u"txt_preco_prod")
        self.txt_preco_prod.setMinimumSize(QSize(200, 0))
        self.txt_preco_prod.setMaximumSize(QSize(16777215, 16777215))
        self.txt_preco_prod.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_10.addWidget(self.txt_preco_prod)


        self.verticalLayout_23.addLayout(self.verticalLayout_10)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_13)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_90 = QLabel(self.frame_2)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_90)

        self.calendario_prod = QCalendarWidget(self.frame_2)
        self.calendario_prod.setObjectName(u"calendario_prod")
        self.calendario_prod.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.calendario_prod.setGridVisible(True)
        self.calendario_prod.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendario_prod.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendario_prod.setNavigationBarVisible(True)
        self.calendario_prod.setDateEditEnabled(True)

        self.verticalLayout_6.addWidget(self.calendario_prod)


        self.verticalLayout_22.addLayout(self.verticalLayout_6)

        self.txt_data_prod = QDateEdit(self.frame_2)
        self.txt_data_prod.setObjectName(u"txt_data_prod")
        self.txt_data_prod.setMaximumSize(QSize(16777215, 16777215))
        self.txt_data_prod.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_22.addWidget(self.txt_data_prod)


        self.verticalLayout_23.addLayout(self.verticalLayout_22)


        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.pg_cad_prod)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color:rgb(0,0,0)")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.frame_5 = QFrame(self.frame_8)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 200))
        self.frame_5.setMaximumSize(QSize(400, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(205,92,92);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 50))
        self.label_15.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_15)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)

        self.verticalLayout_13.addWidget(self.label_16)

        self.txt_nome_forn = QLineEdit(self.frame_5)
        self.txt_nome_forn.setObjectName(u"txt_nome_forn")
        self.txt_nome_forn.setMinimumSize(QSize(200, 0))
        self.txt_nome_forn.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_13.addWidget(self.txt_nome_forn)


        self.verticalLayout_5.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)

        self.verticalLayout_14.addWidget(self.label_17)

        self.txt_end_forn = QLineEdit(self.frame_5)
        self.txt_end_forn.setObjectName(u"txt_end_forn")
        self.txt_end_forn.setMinimumSize(QSize(200, 0))
        self.txt_end_forn.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_14.addWidget(self.txt_end_forn)


        self.verticalLayout_5.addLayout(self.verticalLayout_14)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)

        self.verticalLayout_16.addWidget(self.label_19)

        self.txt_cidade_forn = QLineEdit(self.frame_5)
        self.txt_cidade_forn.setObjectName(u"txt_cidade_forn")
        self.txt_cidade_forn.setMinimumSize(QSize(200, 0))
        self.txt_cidade_forn.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_16.addWidget(self.txt_cidade_forn)


        self.verticalLayout_5.addLayout(self.verticalLayout_16)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.verticalLayout_15.addWidget(self.label_18)

        self.txt_bairro_forn = QLineEdit(self.frame_5)
        self.txt_bairro_forn.setObjectName(u"txt_bairro_forn")
        self.txt_bairro_forn.setMinimumSize(QSize(200, 0))
        self.txt_bairro_forn.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_15.addWidget(self.txt_bairro_forn)


        self.verticalLayout_5.addLayout(self.verticalLayout_15)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.combobox = QLabel(self.frame_5)
        self.combobox.setObjectName(u"combobox")
        self.combobox.setFont(font3)

        self.verticalLayout_18.addWidget(self.combobox)

        self.txt_uf_forn = QComboBox(self.frame_5)
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.addItem("")
        self.txt_uf_forn.setObjectName(u"txt_uf_forn")
        self.txt_uf_forn.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_18.addWidget(self.txt_uf_forn)


        self.verticalLayout_5.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_22 = QLabel(self.frame_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)

        self.verticalLayout_19.addWidget(self.label_22)

        self.txt_cep_forn = QLineEdit(self.frame_5)
        self.txt_cep_forn.setObjectName(u"txt_cep_forn")
        self.txt_cep_forn.setMinimumSize(QSize(200, 0))
        self.txt_cep_forn.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_19.addWidget(self.txt_cep_forn)


        self.verticalLayout_5.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_23 = QLabel(self.frame_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)

        self.verticalLayout_20.addWidget(self.label_23)

        self.txt_cnpj_forn = QLineEdit(self.frame_5)
        self.txt_cnpj_forn.setObjectName(u"txt_cnpj_forn")
        self.txt_cnpj_forn.setMinimumSize(QSize(200, 0))
        self.txt_cnpj_forn.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_20.addWidget(self.txt_cnpj_forn)


        self.verticalLayout_5.addLayout(self.verticalLayout_20)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)

        self.verticalLayout_17.addWidget(self.label_20)

        self.txt_tel_forn = QLineEdit(self.frame_5)
        self.txt_tel_forn.setObjectName(u"txt_tel_forn")
        self.txt_tel_forn.setMinimumSize(QSize(200, 0))
        self.txt_tel_forn.setStyleSheet(u"background-color:rgb(240,255,240)")

        self.verticalLayout_17.addWidget(self.txt_tel_forn)


        self.verticalLayout_5.addLayout(self.verticalLayout_17)


        self.gridLayout_6.addWidget(self.frame_5, 0, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_8)

        self.frame_11 = QFrame(self.pg_cad_prod)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(140, 50))
        self.frame_11.setMaximumSize(QSize(140, 50))
        self.frame_11.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_11)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(2, 2, 2, 2)
        self.frame_9 = QFrame(self.frame_11)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(205,92,92);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_9)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.btn_salvar_prod = QPushButton(self.frame_9)
        self.btn_salvar_prod.setObjectName(u"btn_salvar_prod")
        self.btn_salvar_prod.setMinimumSize(QSize(120, 32))
        self.btn_salvar_prod.setMaximumSize(QSize(120, 32))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.btn_salvar_prod.setFont(font4)
        self.btn_salvar_prod.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_prod.setLayoutDirection(Qt.LeftToRight)
        self.btn_salvar_prod.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(176,224,230);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icones/salvar (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar_prod.setIcon(icon6)
        self.btn_salvar_prod.setIconSize(QSize(32, 32))

        self.verticalLayout_25.addWidget(self.btn_salvar_prod)


        self.verticalLayout_24.addWidget(self.frame_9)


        self.horizontalLayout_11.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.pg_cad_prod)
        self.pg_estoque = QWidget()
        self.pg_estoque.setObjectName(u"pg_estoque")
        self.verticalLayout_40 = QVBoxLayout(self.pg_estoque)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.frame_10 = QFrame(self.pg_estoque)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_10)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.tabWidget = QTabWidget(self.frame_10)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_4 = QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_18 = QFrame(self.tab)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: rgb(0,0,0)")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_18)
        self.verticalLayout_44.setSpacing(2)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_44.setContentsMargins(2, 2, 2, 2)
        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 45))
        self.frame_20.setStyleSheet(u"background-color: rgb(205,92,92);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_20)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_11 = QLabel(self.frame_20)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_46.addWidget(self.label_11, 0, Qt.AlignHCenter)


        self.verticalLayout_44.addWidget(self.frame_20)

        self.tw_estoque = QTableWidget(self.frame_18)
        if (self.tw_estoque.columnCount() < 7):
            self.tw_estoque.setColumnCount(7)
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(11)
        font5.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.tw_estoque.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        self.tw_estoque.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        self.tw_estoque.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.tw_estoque.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tw_estoque.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font5);
        self.tw_estoque.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font5);
        self.tw_estoque.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.tw_estoque.setStyleSheet(u"\n"
"background-color: rgb(205,92,92);\n"
"\n"
"")
        self.tw_estoque.setFrameShape(QFrame.StyledPanel)
        self.tw_estoque.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.tw_estoque)


        self.verticalLayout_42.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.tab)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background-color:rgb(0,0,0)")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_19)
        self.verticalLayout_43.setSpacing(2)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_43.setContentsMargins(2, 2, 2, 2)
        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 45))
        self.frame_21.setStyleSheet(u"background-color: rgb(205,92,92);")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_21)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_21 = QLabel(self.frame_21)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_45.addWidget(self.label_21, 0, Qt.AlignHCenter)


        self.verticalLayout_43.addWidget(self.frame_21)

        self.tw_fornecedores = QTableWidget(self.frame_19)
        if (self.tw_fornecedores.columnCount() < 8):
            self.tw_fornecedores.setColumnCount(8)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font5);
        self.tw_fornecedores.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font5);
        self.tw_fornecedores.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font5);
        self.tw_fornecedores.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font5);
        self.tw_fornecedores.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font5);
        self.tw_fornecedores.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font5);
        self.tw_fornecedores.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font5);
        self.tw_fornecedores.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font5);
        self.tw_fornecedores.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        self.tw_fornecedores.setObjectName(u"tw_fornecedores")
        font6 = QFont()
        font6.setPointSize(9)
        self.tw_fornecedores.setFont(font6)
        self.tw_fornecedores.setStyleSheet(u"\n"
"background-color: rgb(205,92,92);\n"
"")

        self.verticalLayout_43.addWidget(self.tw_fornecedores)


        self.verticalLayout_42.addWidget(self.frame_19)


        self.horizontalLayout_4.addLayout(self.verticalLayout_42)

        self.frame_6 = QFrame(self.tab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(200, 0))
        self.frame_6.setSizeIncrement(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_21.addWidget(self.label_24, 0, Qt.AlignHCenter)

        self.frame_32 = QFrame(self.frame_6)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(200, 160))
        self.frame_32.setMaximumSize(QSize(200, 160))
        self.frame_32.setStyleSheet(u"background-color: rgb(0,0,0)")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.frame_36 = QFrame(self.frame_32)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"background-color: rgb(205,92,92);")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_36)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.btn_relatorio_tw_estoque = QPushButton(self.frame_36)
        self.btn_relatorio_tw_estoque.setObjectName(u"btn_relatorio_tw_estoque")
        self.btn_relatorio_tw_estoque.setMinimumSize(QSize(120, 40))
        self.btn_relatorio_tw_estoque.setFont(font4)
        self.btn_relatorio_tw_estoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorio_tw_estoque.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(0,100,0);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icones/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_relatorio_tw_estoque.setIcon(icon7)
        self.btn_relatorio_tw_estoque.setIconSize(QSize(32, 32))

        self.verticalLayout_64.addWidget(self.btn_relatorio_tw_estoque)

        self.btn_alterar_tw_estoque = QPushButton(self.frame_36)
        self.btn_alterar_tw_estoque.setObjectName(u"btn_alterar_tw_estoque")
        self.btn_alterar_tw_estoque.setMinimumSize(QSize(120, 40))
        self.btn_alterar_tw_estoque.setFont(font4)
        self.btn_alterar_tw_estoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_tw_estoque.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(255,140,0);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icones/alterar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar_tw_estoque.setIcon(icon8)
        self.btn_alterar_tw_estoque.setIconSize(QSize(32, 32))

        self.verticalLayout_64.addWidget(self.btn_alterar_tw_estoque)

        self.btn_excluir_tw_estoque = QPushButton(self.frame_36)
        self.btn_excluir_tw_estoque.setObjectName(u"btn_excluir_tw_estoque")
        self.btn_excluir_tw_estoque.setMinimumSize(QSize(120, 40))
        self.btn_excluir_tw_estoque.setFont(font4)
        self.btn_excluir_tw_estoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_tw_estoque.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(139,0,0);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"icones/excluir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir_tw_estoque.setIcon(icon9)
        self.btn_excluir_tw_estoque.setIconSize(QSize(32, 32))

        self.verticalLayout_64.addWidget(self.btn_excluir_tw_estoque)


        self.horizontalLayout_14.addWidget(self.frame_36)


        self.verticalLayout_21.addWidget(self.frame_32)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_16)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_14)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_15)

        self.label_25 = QLabel(self.frame_6)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_21.addWidget(self.label_25, 0, Qt.AlignHCenter)

        self.frame_22 = QFrame(self.frame_6)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(200, 160))
        self.frame_22.setMaximumSize(QSize(200, 160))
        self.frame_22.setStyleSheet(u"background-color: rgb(0,0,0)")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"background-color: rgb(205,92,92);")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_23)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.btn_relatorio_tw_fornecedores = QPushButton(self.frame_23)
        self.btn_relatorio_tw_fornecedores.setObjectName(u"btn_relatorio_tw_fornecedores")
        self.btn_relatorio_tw_fornecedores.setMinimumSize(QSize(120, 40))
        self.btn_relatorio_tw_fornecedores.setFont(font4)
        self.btn_relatorio_tw_fornecedores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorio_tw_fornecedores.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(0,100,0);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}")
        self.btn_relatorio_tw_fornecedores.setIcon(icon7)
        self.btn_relatorio_tw_fornecedores.setIconSize(QSize(32, 32))

        self.verticalLayout_47.addWidget(self.btn_relatorio_tw_fornecedores)

        self.btn_alterar_tw_fornecedores = QPushButton(self.frame_23)
        self.btn_alterar_tw_fornecedores.setObjectName(u"btn_alterar_tw_fornecedores")
        self.btn_alterar_tw_fornecedores.setMinimumSize(QSize(120, 40))
        self.btn_alterar_tw_fornecedores.setFont(font4)
        self.btn_alterar_tw_fornecedores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_tw_fornecedores.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(255,140,0);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}")
        self.btn_alterar_tw_fornecedores.setIcon(icon8)
        self.btn_alterar_tw_fornecedores.setIconSize(QSize(32, 32))

        self.verticalLayout_47.addWidget(self.btn_alterar_tw_fornecedores)

        self.btn_excluir_tw_fornecedores = QPushButton(self.frame_23)
        self.btn_excluir_tw_fornecedores.setObjectName(u"btn_excluir_tw_fornecedores")
        self.btn_excluir_tw_fornecedores.setMinimumSize(QSize(120, 40))
        self.btn_excluir_tw_fornecedores.setFont(font4)
        self.btn_excluir_tw_fornecedores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_tw_fornecedores.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(139,0,0);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}")
        self.btn_excluir_tw_fornecedores.setIcon(icon9)
        self.btn_excluir_tw_fornecedores.setIconSize(QSize(32, 32))

        self.verticalLayout_47.addWidget(self.btn_excluir_tw_fornecedores)


        self.horizontalLayout_5.addWidget(self.frame_23)


        self.verticalLayout_21.addWidget(self.frame_22)


        self.horizontalLayout_4.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_48 = QVBoxLayout(self.tab_2)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_25 = QFrame(self.tab_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_25)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(2, 2, 2, 2)
        self.txt_pesquisa_prod = QLineEdit(self.frame_25)
        self.txt_pesquisa_prod.setObjectName(u"txt_pesquisa_prod")
        self.txt_pesquisa_prod.setMinimumSize(QSize(0, 30))
        self.txt_pesquisa_prod.setMaximumSize(QSize(16777215, 30))
        self.txt_pesquisa_prod.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.txt_pesquisa_prod.setAlignment(Qt.AlignCenter)

        self.verticalLayout_49.addWidget(self.txt_pesquisa_prod)


        self.verticalLayout_48.addWidget(self.frame_25)

        self.frame_24 = QFrame(self.tab_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_24)
        self.verticalLayout_50.setSpacing(2)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_50.setContentsMargins(2, 2, 2, 2)
        self.tv_pesquisa_prod = QTableView(self.frame_24)
        self.tv_pesquisa_prod.setObjectName(u"tv_pesquisa_prod")
        self.tv_pesquisa_prod.setStyleSheet(u"\n"
"background-color: rgb(205,92,92);\n"
"\n"
"")

        self.verticalLayout_50.addWidget(self.tv_pesquisa_prod)


        self.verticalLayout_48.addWidget(self.frame_24)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_41.addWidget(self.tabWidget)


        self.verticalLayout_40.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.pg_estoque)
        self.pg_cad_user = QWidget()
        self.pg_cad_user.setObjectName(u"pg_cad_user")
        self.horizontalLayout_6 = QHBoxLayout(self.pg_cad_user)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_26 = QFrame(self.pg_cad_user)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_26)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(2, 2, 2, 2)
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"\n"
"background-color: rgb(205,92,92);\n"
"\n"
"")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_27)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_42 = QLabel(self.frame_27)
        self.label_42.setObjectName(u"label_42")
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(20)
        font7.setBold(True)
        font7.setItalic(True)
        self.label_42.setFont(font7)

        self.verticalLayout_52.addWidget(self.label_42, 0, Qt.AlignHCenter)

        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_43 = QLabel(self.frame_27)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font5)

        self.verticalLayout_57.addWidget(self.label_43)

        self.txt_nome_user = QLineEdit(self.frame_27)
        self.txt_nome_user.setObjectName(u"txt_nome_user")
        self.txt_nome_user.setMinimumSize(QSize(0, 0))
        self.txt_nome_user.setMaximumSize(QSize(16777215, 16777215))
        self.txt_nome_user.setLayoutDirection(Qt.LeftToRight)
        self.txt_nome_user.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_nome_user.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txt_nome_user.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.verticalLayout_57.addWidget(self.txt_nome_user)


        self.verticalLayout_52.addLayout(self.verticalLayout_57)

        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_44 = QLabel(self.frame_27)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font5)

        self.verticalLayout_56.addWidget(self.label_44)

        self.txt_user_user = QLineEdit(self.frame_27)
        self.txt_user_user.setObjectName(u"txt_user_user")
        self.txt_user_user.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_56.addWidget(self.txt_user_user)


        self.verticalLayout_52.addLayout(self.verticalLayout_56)

        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_45 = QLabel(self.frame_27)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font5)

        self.verticalLayout_55.addWidget(self.label_45)

        self.txt_senha_user = QLineEdit(self.frame_27)
        self.txt_senha_user.setObjectName(u"txt_senha_user")
        self.txt_senha_user.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_senha_user.setEchoMode(QLineEdit.Password)

        self.verticalLayout_55.addWidget(self.txt_senha_user)


        self.verticalLayout_52.addLayout(self.verticalLayout_55)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.label_46 = QLabel(self.frame_27)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font5)

        self.verticalLayout_54.addWidget(self.label_46)

        self.txt_senha2_user = QLineEdit(self.frame_27)
        self.txt_senha2_user.setObjectName(u"txt_senha2_user")
        self.txt_senha2_user.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_senha2_user.setEchoMode(QLineEdit.Password)

        self.verticalLayout_54.addWidget(self.txt_senha2_user)


        self.verticalLayout_52.addLayout(self.verticalLayout_54)

        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_50 = QLabel(self.frame_27)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font5)

        self.verticalLayout_53.addWidget(self.label_50)

        self.txt_perfil_user = QComboBox(self.frame_27)
        self.txt_perfil_user.addItem("")
        self.txt_perfil_user.addItem("")
        self.txt_perfil_user.setObjectName(u"txt_perfil_user")
        self.txt_perfil_user.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_53.addWidget(self.txt_perfil_user)


        self.verticalLayout_52.addLayout(self.verticalLayout_53)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_48 = QLabel(self.frame_27)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_12.addWidget(self.label_48)

        self.btn_cadastro_user = QPushButton(self.frame_27)
        self.btn_cadastro_user.setObjectName(u"btn_cadastro_user")
        self.btn_cadastro_user.setMinimumSize(QSize(130, 40))
        self.btn_cadastro_user.setMaximumSize(QSize(130, 16777215))
        self.btn_cadastro_user.setFont(font4)
        self.btn_cadastro_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastro_user.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(176,224,230);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"icones/novo_user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastro_user.setIcon(icon10)
        self.btn_cadastro_user.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.btn_cadastro_user)

        self.label_49 = QLabel(self.frame_27)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_12.addWidget(self.label_49)


        self.verticalLayout_52.addLayout(self.horizontalLayout_12)


        self.verticalLayout_51.addWidget(self.frame_27)


        self.horizontalLayout_6.addWidget(self.frame_26)

        self.stackedWidget.addWidget(self.pg_cad_user)
        self.pg_users = QWidget()
        self.pg_users.setObjectName(u"pg_users")
        self.verticalLayout_58 = QVBoxLayout(self.pg_users)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.frame_28 = QFrame(self.pg_users)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_62 = QVBoxLayout()
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, -1)
        self.frame_33 = QFrame(self.frame_28)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(406, 0))
        self.frame_33.setMaximumSize(QSize(406, 16777215))
        self.frame_33.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_33)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(2, 2, 2, 2)
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"\n"
"background-color: rgb(205,92,92);\n"
"\n"
"")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_47 = QLabel(self.frame_34)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_47, 0, Qt.AlignHCenter)


        self.verticalLayout_63.addWidget(self.frame_34)


        self.verticalLayout_62.addWidget(self.frame_33, 0, Qt.AlignHCenter)

        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(406, 0))
        self.frame_30.setMaximumSize(QSize(406, 16777215))
        self.frame_30.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_30)
        self.verticalLayout_60.setSpacing(2)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, 0)
        self.tw_users = QTableWidget(self.frame_30)
        if (self.tw_users.columnCount() < 4):
            self.tw_users.setColumnCount(4)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font5);
        self.tw_users.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font5);
        self.tw_users.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font5);
        self.tw_users.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font5);
        self.tw_users.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        self.tw_users.setObjectName(u"tw_users")
        self.tw_users.setMinimumSize(QSize(0, 0))
        self.tw_users.setMaximumSize(QSize(16777215, 16777215))
        self.tw_users.setStyleSheet(u"\n"
"background-color: rgb(205,92,92);\n"
"\n"
"")

        self.horizontalLayout_9.addWidget(self.tw_users)


        self.verticalLayout_60.addLayout(self.horizontalLayout_9)


        self.verticalLayout_62.addWidget(self.frame_30, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addLayout(self.verticalLayout_62)

        self.frame_31 = QFrame(self.frame_28)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(200, 160))
        self.frame_31.setMaximumSize(QSize(200, 160))
        self.frame_31.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.frame_29 = QFrame(self.frame_31)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"\n"
"background-color: rgb(205,92,92);\n"
"\n"
"")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_29)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.btn_alterar_user = QPushButton(self.frame_29)
        self.btn_alterar_user.setObjectName(u"btn_alterar_user")
        self.btn_alterar_user.setMinimumSize(QSize(140, 40))
        self.btn_alterar_user.setFont(font4)
        self.btn_alterar_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_user.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(218,165,32);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"icones/alterar_user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar_user.setIcon(icon11)
        self.btn_alterar_user.setIconSize(QSize(32, 32))

        self.verticalLayout_61.addWidget(self.btn_alterar_user)

        self.btn_excluir_user = QPushButton(self.frame_29)
        self.btn_excluir_user.setObjectName(u"btn_excluir_user")
        self.btn_excluir_user.setMinimumSize(QSize(140, 40))
        self.btn_excluir_user.setFont(font4)
        self.btn_excluir_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_user.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(178,34,34);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"icones/excluir_user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir_user.setIcon(icon12)
        self.btn_excluir_user.setIconSize(QSize(32, 32))

        self.verticalLayout_61.addWidget(self.btn_excluir_user)


        self.horizontalLayout_7.addWidget(self.frame_29)


        self.horizontalLayout_10.addWidget(self.frame_31, 0, Qt.AlignTop)


        self.verticalLayout_58.addWidget(self.frame_28)

        self.stackedWidget.addWidget(self.pg_users)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.btn_cad_prod.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Produto", None))
        self.btn_estoque.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.btn_cad_user.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.btn_users.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.btn_sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.btn_menu.setText("")
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema Controle de Estoque", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Dados Produto", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o Produto:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.txt_tipo_prod.setItemText(0, "")
        self.txt_tipo_prod.setItemText(1, QCoreApplication.translate("MainWindow", u"Camisa", None))
        self.txt_tipo_prod.setItemText(2, QCoreApplication.translate("MainWindow", u"Camiseta", None))
        self.txt_tipo_prod.setItemText(3, QCoreApplication.translate("MainWindow", u"Blusa", None))
        self.txt_tipo_prod.setItemText(4, QCoreApplication.translate("MainWindow", u"Short Masculino", None))
        self.txt_tipo_prod.setItemText(5, QCoreApplication.translate("MainWindow", u"Short Feminino", None))
        self.txt_tipo_prod.setItemText(6, QCoreApplication.translate("MainWindow", u"Bermuda Masculina", None))
        self.txt_tipo_prod.setItemText(7, QCoreApplication.translate("MainWindow", u"Bermuda Feminina", None))
        self.txt_tipo_prod.setItemText(8, QCoreApplication.translate("MainWindow", u"Short Jeans Masculino", None))
        self.txt_tipo_prod.setItemText(9, QCoreApplication.translate("MainWindow", u"Short Jeans Feminino", None))
        self.txt_tipo_prod.setItemText(10, QCoreApplication.translate("MainWindow", u"Bermuda Jeans Masculina", None))
        self.txt_tipo_prod.setItemText(11, QCoreApplication.translate("MainWindow", u"Bermuda Jeans Feminina", None))
        self.txt_tipo_prod.setItemText(12, QCoreApplication.translate("MainWindow", u"Cal\u00e7a Masculina", None))
        self.txt_tipo_prod.setItemText(13, QCoreApplication.translate("MainWindow", u"Cal\u00e7a Feminina", None))
        self.txt_tipo_prod.setItemText(14, QCoreApplication.translate("MainWindow", u"Cal\u00e7a Jeans Masculina", None))
        self.txt_tipo_prod.setItemText(15, QCoreApplication.translate("MainWindow", u"Cal\u00e7a Jeans Feminina", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Cor:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Quantidade no Estoque:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o:", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Data da Compra:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Dados Fornecedor", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Cidade:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Bairro:", None))
        self.combobox.setText(QCoreApplication.translate("MainWindow", u"UF:", None))
        self.txt_uf_forn.setItemText(0, "")
        self.txt_uf_forn.setItemText(1, QCoreApplication.translate("MainWindow", u"Acre (AC)", None))
        self.txt_uf_forn.setItemText(2, QCoreApplication.translate("MainWindow", u"Alagoas (AL)", None))
        self.txt_uf_forn.setItemText(3, QCoreApplication.translate("MainWindow", u"Amap\u00e1 (AP)", None))
        self.txt_uf_forn.setItemText(4, QCoreApplication.translate("MainWindow", u"Amazonas (AM)", None))
        self.txt_uf_forn.setItemText(5, QCoreApplication.translate("MainWindow", u"Bahia (BA)", None))
        self.txt_uf_forn.setItemText(6, QCoreApplication.translate("MainWindow", u"Cear\u00e1 (CE)", None))
        self.txt_uf_forn.setItemText(7, QCoreApplication.translate("MainWindow", u"Distrito Federal (DF)", None))
        self.txt_uf_forn.setItemText(8, QCoreApplication.translate("MainWindow", u"Esp\u00edrito Santo (ES)", None))
        self.txt_uf_forn.setItemText(9, QCoreApplication.translate("MainWindow", u"Go\u00edas (GO)", None))
        self.txt_uf_forn.setItemText(10, QCoreApplication.translate("MainWindow", u"Maranh\u00e3o (MA)", None))
        self.txt_uf_forn.setItemText(11, QCoreApplication.translate("MainWindow", u"Mato Grosso (MT)", None))
        self.txt_uf_forn.setItemText(12, QCoreApplication.translate("MainWindow", u"Mato Grosso do Sul (MS)", None))
        self.txt_uf_forn.setItemText(13, QCoreApplication.translate("MainWindow", u"Minas Gerais (MG)", None))
        self.txt_uf_forn.setItemText(14, QCoreApplication.translate("MainWindow", u"Par\u00e1 (PA)", None))
        self.txt_uf_forn.setItemText(15, QCoreApplication.translate("MainWindow", u"Para\u00edba (PB)", None))
        self.txt_uf_forn.setItemText(16, QCoreApplication.translate("MainWindow", u"Paran\u00e1 (PR)", None))
        self.txt_uf_forn.setItemText(17, QCoreApplication.translate("MainWindow", u"Pernambuco (PE)", None))
        self.txt_uf_forn.setItemText(18, QCoreApplication.translate("MainWindow", u"Piau\u00ed (PI)", None))
        self.txt_uf_forn.setItemText(19, QCoreApplication.translate("MainWindow", u"Rio de Janeiro (RJ)", None))
        self.txt_uf_forn.setItemText(20, QCoreApplication.translate("MainWindow", u"Rio Grande do Norte (RN)", None))
        self.txt_uf_forn.setItemText(21, QCoreApplication.translate("MainWindow", u"Rio Grande do Sul (RS)", None))
        self.txt_uf_forn.setItemText(22, QCoreApplication.translate("MainWindow", u"Rond\u00f4nia (RO)", None))
        self.txt_uf_forn.setItemText(23, QCoreApplication.translate("MainWindow", u"Roraima (RR)", None))
        self.txt_uf_forn.setItemText(24, QCoreApplication.translate("MainWindow", u"Santa Catarina (SC)", None))
        self.txt_uf_forn.setItemText(25, QCoreApplication.translate("MainWindow", u"S\u00e3o Paulo (SP)", None))
        self.txt_uf_forn.setItemText(26, QCoreApplication.translate("MainWindow", u"Sergipe (SE)", None))
        self.txt_uf_forn.setItemText(27, QCoreApplication.translate("MainWindow", u"Tocantins (TO)", None))

        self.label_22.setText(QCoreApplication.translate("MainWindow", u"CEP:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"CNPJ:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.btn_salvar_prod.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Estoque</span></p></body></html>", None))
        ___qtablewidgetitem = self.tw_estoque.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.tw_estoque.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o ", None));
        ___qtablewidgetitem2 = self.tw_estoque.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem3 = self.tw_estoque.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cor", None));
        ___qtablewidgetitem4 = self.tw_estoque.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem5 = self.tw_estoque.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem6 = self.tw_estoque.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Data Compra", None));
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Fornecedores</span></p></body></html>", None))
        ___qtablewidgetitem7 = self.tw_fornecedores.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem8 = self.tw_fornecedores.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem9 = self.tw_fornecedores.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Cidade", None));
        ___qtablewidgetitem10 = self.tw_fornecedores.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem11 = self.tw_fornecedores.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem12 = self.tw_fornecedores.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem13 = self.tw_fornecedores.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem14 = self.tw_fornecedores.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Estoque</span></p></body></html>", None))
        self.btn_relatorio_tw_estoque.setText(QCoreApplication.translate("MainWindow", u"Gerar Relat\u00f3rio", None))
        self.btn_alterar_tw_estoque.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_tw_estoque.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Fornecedores</span></p></body></html>", None))
        self.btn_relatorio_tw_fornecedores.setText(QCoreApplication.translate("MainWindow", u"Gerar Relat\u00f3rio", None))
        self.btn_alterar_tw_fornecedores.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_tw_fornecedores.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Estoque / Fornecedores", None))
        self.txt_pesquisa_prod.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Perfil:", None))
        self.txt_perfil_user.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.txt_perfil_user.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_48.setText("")
        self.btn_cadastro_user.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_49.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        ___qtablewidgetitem15 = self.tw_users.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem16 = self.tw_users.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem17 = self.tw_users.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtablewidgetitem18 = self.tw_users.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Perfil", None));
        self.btn_alterar_user.setText(QCoreApplication.translate("MainWindow", u"Alterar Usu\u00e1rio", None))
        self.btn_excluir_user.setText(QCoreApplication.translate("MainWindow", u"Excluir Usu\u00e1rio", None))
    # retranslateUi

