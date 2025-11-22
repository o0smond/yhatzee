# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_1.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1077, 634)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_background = QLabel(self.centralwidget)
        self.lbl_background.setObjectName(u"lbl_background")
        self.lbl_background.setGeometry(QRect(-4, -3, 1091, 641))
        self.lbl_background.setStyleSheet(u"background-color: rgb(255, 163, 72);")
        self.lbl_logo = QLabel(self.centralwidget)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setGeometry(QRect(310, 10, 431, 241))
        self.lbl_logo.setPixmap(QPixmap(u"../images/logo.png"))
        self.lbl_logo.setScaledContents(True)
        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(1020, 10, 51, 26))
        self.btn_play = QPushButton(self.centralwidget)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setGeometry(QRect(430, 320, 251, 81))
        font = QFont()
        font.setPointSize(36)
        self.btn_play.setFont(font)
        self.btn_view = QPushButton(self.centralwidget)
        self.btn_view.setObjectName(u"btn_view")
        self.btn_view.setGeometry(QRect(430, 410, 251, 81))
        font1 = QFont()
        font1.setPointSize(18)
        self.btn_view.setFont(font1)
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(20, 10, 81, 31))
        font2 = QFont()
        font2.setPointSize(13)
        self.btn_back.setFont(font2)
        self.txt_instructions = QTextBrowser(self.centralwidget)
        self.txt_instructions.setObjectName(u"txt_instructions")
        self.txt_instructions.setGeometry(QRect(70, 150, 951, 331))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_exit.clicked.connect(MainWindow.btn_exit_a)
        self.btn_play.clicked.connect(MainWindow.btn_play_a)
        self.btn_view.clicked.connect(MainWindow.btn_view_a)
        self.btn_back.clicked.connect(MainWindow.btn_back_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Yhatzee", None))
        self.lbl_background.setText("")
        self.lbl_logo.setText("")
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btn_play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.btn_view.setText(QCoreApplication.translate("MainWindow", u"View Instructions", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.txt_instructions.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">Yahtzee is a game centered around making scoring combinations with 5 dice. Each turn, after your initial roll, you can choose to re-roll any number of your dice up to a maximum of two times. After you are done rolling, select &quot;Done&quot; and then choose the scoring value you would like to take, if possible. If you are confused about a scoring combination, click "
                        "the &quot;?&quot; button then the scoring combination you are confused about and an explanation popup will appear. Have fun!</span></p></body></html>", None))
    # retranslateUi

