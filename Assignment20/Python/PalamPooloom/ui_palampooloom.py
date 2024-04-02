# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'palampooloom.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(429, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color:rgb(99, 99, 99);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(110, 410, 91, 91))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(25)
        self.back.setFont(font)
        self.back.setStyleSheet(u"background-color: rgb(6, 20, 53);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.front = QPushButton(self.centralwidget)
        self.front.setObjectName(u"front")
        self.front.setGeometry(QRect(220, 410, 91, 91))
        self.front.setFont(font)
        self.front.setStyleSheet(u"background-color: rgb(6, 20, 53);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.player = QLineEdit(self.centralwidget)
        self.player.setObjectName(u"player")
        self.player.setGeometry(QRect(110, 280, 201, 111))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(60)
        font1.setBold(False)
        self.player.setFont(font1)
        self.player.setStyleSheet(u"background-color: rgb(6, 20, 53);\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.player.setMaxLength(2)
        self.player.setAlignment(Qt.AlignCenter)
        self.computer2 = QLineEdit(self.centralwidget)
        self.computer2.setObjectName(u"computer2")
        self.computer2.setGeometry(QRect(220, 80, 181, 111))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(60)
        self.computer2.setFont(font2)
        self.computer2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.computer2.setMaxLength(2)
        self.computer2.setAlignment(Qt.AlignCenter)
        self.computer1 = QLineEdit(self.centralwidget)
        self.computer1.setObjectName(u"computer1")
        self.computer1.setGeometry(QRect(20, 80, 181, 111))
        self.computer1.setFont(font2)
        self.computer1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.computer1.setMaxLength(2)
        self.computer1.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.player_score = QLineEdit(self.centralwidget)
        self.player_score.setObjectName(u"player_score")
        self.player_score.setGeometry(QRect(10, 300, 91, 61))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(30)
        font3.setBold(True)
        font3.setUnderline(True)
        self.player_score.setFont(font3)
        self.player_score.setStyleSheet(u"color: rgb(6, 20, 53);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.player_score.setMaxLength(1)
        self.player_score.setAlignment(Qt.AlignCenter)
        self.scoreC2 = QLineEdit(self.centralwidget)
        self.scoreC2.setObjectName(u"scoreC2")
        self.scoreC2.setGeometry(QRect(270, 10, 91, 61))
        self.scoreC2.setFont(font3)
        self.scoreC2.setStyleSheet(u"color: rgb(rgb(0, 0, 0));\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.scoreC2.setMaxLength(1)
        self.scoreC2.setAlignment(Qt.AlignCenter)
        self.win = QLineEdit(self.centralwidget)
        self.win.setObjectName(u"win")
        self.win.setGeometry(QRect(10, 230, 411, 41))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.win.setFont(font4)
        self.win.setStyleSheet(u"background-color: rgb(227, 151, 0);\n"
"border-top-right-radius: 20px;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;")
        self.win.setMaxLength(15)
        self.win.setAlignment(Qt.AlignCenter)
        self.scoreC1 = QLineEdit(self.centralwidget)
        self.scoreC1.setObjectName(u"scoreC1")
        self.scoreC1.setGeometry(QRect(60, 10, 91, 61))
        self.scoreC1.setFont(font3)
        self.scoreC1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.scoreC1.setMaxLength(1)
        self.scoreC1.setAlignment(Qt.AlignCenter)
        self.name1 = QLineEdit(self.centralwidget)
        self.name1.setObjectName(u"name1")
        self.name1.setGeometry(QRect(50, 200, 113, 21))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.name1.setFont(font5)
        self.name1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.name1.setAlignment(Qt.AlignCenter)
        self.name2 = QLineEdit(self.centralwidget)
        self.name2.setObjectName(u"name2")
        self.name2.setGeometry(QRect(250, 200, 113, 21))
        self.name2.setFont(font5)
        self.name2.setStyleSheet(u"color: rgb(0,0, 0);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.name2.setAlignment(Qt.AlignCenter)
        self.name = QLineEdit(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(320, 320, 71, 31))
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(True)
        self.name.setFont(font6)
        self.name.setStyleSheet(u"color: rgb(6, 20, 53);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.name.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 429, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Palam Pulum Plish", None))
        self.back.setText("")
        self.front.setText("")
        self.player.setText("")
        self.computer2.setText("")
        self.computer1.setText("")
        self.player_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.scoreC2.setInputMask("")
        self.scoreC2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.win.setText("")
        self.scoreC1.setInputMask("")
        self.scoreC1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.name1.setText(QCoreApplication.translate("MainWindow", u"Computer 1", None))
        self.name2.setText(QCoreApplication.translate("MainWindow", u"Computer 2", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"Player", None))
    # retranslateUi

