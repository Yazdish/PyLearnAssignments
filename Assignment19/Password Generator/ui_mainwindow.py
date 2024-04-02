# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(384, 210)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.extra = QRadioButton(self.centralwidget)
        self.extra.setObjectName(u"extra")

        self.gridLayout.addWidget(self.extra, 2, 0, 1, 1)

        self.txtbox = QTextEdit(self.centralwidget)
        self.txtbox.setObjectName(u"txtbox")

        self.gridLayout.addWidget(self.txtbox, 5, 0, 1, 2)

        self.generate = QPushButton(self.centralwidget)
        self.generate.setObjectName(u"generate")

        self.gridLayout.addWidget(self.generate, 5, 3, 1, 1)

        self.strong = QRadioButton(self.centralwidget)
        self.strong.setObjectName(u"strong")

        self.gridLayout.addWidget(self.strong, 4, 0, 1, 1)

        self.superstrong = QRadioButton(self.centralwidget)
        self.superstrong.setObjectName(u"superstrong")

        self.gridLayout.addWidget(self.superstrong, 1, 0, 1, 1)

        self.about = QPushButton(self.centralwidget)
        self.about.setObjectName(u"about")

        self.gridLayout.addWidget(self.about, 1, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 384, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.extra.setText(QCoreApplication.translate("MainWindow", u"Extra Strong", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.strong.setText(QCoreApplication.translate("MainWindow", u"Strong", None))
        self.superstrong.setText(QCoreApplication.translate("MainWindow", u"Super Strong", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

