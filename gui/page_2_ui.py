# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(945, 847)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_background = QLabel(self.centralwidget)
        self.lbl_background.setObjectName(u"lbl_background")
        self.lbl_background.setGeometry(QRect(-4, -3, 1301, 921))
        font = QFont()
        font.setFamilies([u"C059"])
        font.setPointSize(16)
        font.setBold(True)
        self.lbl_background.setFont(font)
        self.lbl_background.setStyleSheet(u"background-color: rgb(255, 163, 72);")
        self.btn_d2 = QPushButton(self.centralwidget)
        self.btn_d2.setObjectName(u"btn_d2")
        self.btn_d2.setGeometry(QRect(170, 130, 121, 111))
        font1 = QFont()
        font1.setPointSize(1)
        self.btn_d2.setFont(font1)
        self.btn_roll = QPushButton(self.centralwidget)
        self.btn_roll.setObjectName(u"btn_roll")
        self.btn_roll.setGeometry(QRect(130, 620, 191, 51))
        font2 = QFont()
        font2.setFamilies([u"C059"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.btn_roll.setFont(font2)
        self.btn_done = QPushButton(self.centralwidget)
        self.btn_done.setObjectName(u"btn_done")
        self.btn_done.setGeometry(QRect(160, 680, 141, 51))
        self.btn_done.setFont(font2)
        self.lbl_div1 = QLabel(self.centralwidget)
        self.lbl_div1.setObjectName(u"lbl_div1")
        self.lbl_div1.setGeometry(QRect(480, 0, 16, 911))
        self.lbl_div1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.lbl_div2 = QLabel(self.centralwidget)
        self.lbl_div2.setObjectName(u"lbl_div2")
        self.lbl_div2.setGeometry(QRect(490, 440, 801, 16))
        self.lbl_div2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(490, 450, 291, 401))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_3same = QPushButton(self.verticalLayoutWidget)
        self.btn_3same.setObjectName(u"btn_3same")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3same.sizePolicy().hasHeightForWidth())
        self.btn_3same.setSizePolicy(sizePolicy)
        self.btn_3same.setFont(font)

        self.verticalLayout.addWidget(self.btn_3same)

        self.btn_4same = QPushButton(self.verticalLayoutWidget)
        self.btn_4same.setObjectName(u"btn_4same")
        sizePolicy.setHeightForWidth(self.btn_4same.sizePolicy().hasHeightForWidth())
        self.btn_4same.setSizePolicy(sizePolicy)
        self.btn_4same.setFont(font)

        self.verticalLayout.addWidget(self.btn_4same)

        self.btn_fullhouse = QPushButton(self.verticalLayoutWidget)
        self.btn_fullhouse.setObjectName(u"btn_fullhouse")
        sizePolicy.setHeightForWidth(self.btn_fullhouse.sizePolicy().hasHeightForWidth())
        self.btn_fullhouse.setSizePolicy(sizePolicy)
        self.btn_fullhouse.setFont(font)

        self.verticalLayout.addWidget(self.btn_fullhouse)

        self.btn_smstr = QPushButton(self.verticalLayoutWidget)
        self.btn_smstr.setObjectName(u"btn_smstr")
        sizePolicy.setHeightForWidth(self.btn_smstr.sizePolicy().hasHeightForWidth())
        self.btn_smstr.setSizePolicy(sizePolicy)
        self.btn_smstr.setFont(font)

        self.verticalLayout.addWidget(self.btn_smstr)

        self.btn_lgstr = QPushButton(self.verticalLayoutWidget)
        self.btn_lgstr.setObjectName(u"btn_lgstr")
        sizePolicy.setHeightForWidth(self.btn_lgstr.sizePolicy().hasHeightForWidth())
        self.btn_lgstr.setSizePolicy(sizePolicy)
        self.btn_lgstr.setFont(font)

        self.verticalLayout.addWidget(self.btn_lgstr)

        self.btn_yhatzee = QPushButton(self.verticalLayoutWidget)
        self.btn_yhatzee.setObjectName(u"btn_yhatzee")
        sizePolicy.setHeightForWidth(self.btn_yhatzee.sizePolicy().hasHeightForWidth())
        self.btn_yhatzee.setSizePolicy(sizePolicy)
        self.btn_yhatzee.setFont(font)

        self.verticalLayout.addWidget(self.btn_yhatzee)

        self.btn_chance = QPushButton(self.verticalLayoutWidget)
        self.btn_chance.setObjectName(u"btn_chance")
        sizePolicy.setHeightForWidth(self.btn_chance.sizePolicy().hasHeightForWidth())
        self.btn_chance.setSizePolicy(sizePolicy)
        self.btn_chance.setFont(font)

        self.verticalLayout.addWidget(self.btn_chance)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(490, 0, 291, 441))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.verticalLayoutWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalLayoutWidget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_skip = QPushButton(self.verticalLayoutWidget_2)
        self.btn_skip.setObjectName(u"btn_skip")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.btn_skip.setFont(font3)

        self.verticalLayout_2.addWidget(self.btn_skip)

        self.btn_ones = QPushButton(self.verticalLayoutWidget_2)
        self.btn_ones.setObjectName(u"btn_ones")
        sizePolicy.setHeightForWidth(self.btn_ones.sizePolicy().hasHeightForWidth())
        self.btn_ones.setSizePolicy(sizePolicy)
        self.btn_ones.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_ones)

        self.btn_twos = QPushButton(self.verticalLayoutWidget_2)
        self.btn_twos.setObjectName(u"btn_twos")
        sizePolicy.setHeightForWidth(self.btn_twos.sizePolicy().hasHeightForWidth())
        self.btn_twos.setSizePolicy(sizePolicy)
        self.btn_twos.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_twos)

        self.btn_threes = QPushButton(self.verticalLayoutWidget_2)
        self.btn_threes.setObjectName(u"btn_threes")
        sizePolicy.setHeightForWidth(self.btn_threes.sizePolicy().hasHeightForWidth())
        self.btn_threes.setSizePolicy(sizePolicy)
        self.btn_threes.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_threes)

        self.btn_fours = QPushButton(self.verticalLayoutWidget_2)
        self.btn_fours.setObjectName(u"btn_fours")
        sizePolicy.setHeightForWidth(self.btn_fours.sizePolicy().hasHeightForWidth())
        self.btn_fours.setSizePolicy(sizePolicy)
        self.btn_fours.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_fours)

        self.btn_fives = QPushButton(self.verticalLayoutWidget_2)
        self.btn_fives.setObjectName(u"btn_fives")
        sizePolicy.setHeightForWidth(self.btn_fives.sizePolicy().hasHeightForWidth())
        self.btn_fives.setSizePolicy(sizePolicy)
        self.btn_fives.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_fives)

        self.btn_sixes = QPushButton(self.verticalLayoutWidget_2)
        self.btn_sixes.setObjectName(u"btn_sixes")
        sizePolicy.setHeightForWidth(self.btn_sixes.sizePolicy().hasHeightForWidth())
        self.btn_sixes.setSizePolicy(sizePolicy)
        self.btn_sixes.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_sixes)

        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(10, 810, 51, 31))
        font4 = QFont()
        font4.setFamilies([u"C059"])
        font4.setBold(True)
        self.btn_exit.setFont(font4)
        self.btn_d1 = QPushButton(self.centralwidget)
        self.btn_d1.setObjectName(u"btn_d1")
        self.btn_d1.setGeometry(QRect(170, 10, 121, 111))
        self.btn_d1.setFont(font1)
        self.btn_d5 = QPushButton(self.centralwidget)
        self.btn_d5.setObjectName(u"btn_d5")
        self.btn_d5.setGeometry(QRect(170, 490, 121, 111))
        self.btn_d5.setFont(font1)
        self.btn_d4 = QPushButton(self.centralwidget)
        self.btn_d4.setObjectName(u"btn_d4")
        self.btn_d4.setGeometry(QRect(170, 370, 121, 111))
        self.btn_d4.setFont(font1)
        self.btn_d3 = QPushButton(self.centralwidget)
        self.btn_d3.setObjectName(u"btn_d3")
        self.btn_d3.setGeometry(QRect(170, 250, 121, 111))
        self.btn_d3.setFont(font1)
        self.lbl_turn = QLabel(self.centralwidget)
        self.lbl_turn.setObjectName(u"lbl_turn")
        self.lbl_turn.setGeometry(QRect(150, 740, 151, 51))
        font5 = QFont()
        font5.setFamilies([u"C059"])
        font5.setPointSize(16)
        self.lbl_turn.setFont(font5)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(830, 30, 111, 411))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_ones = QLabel(self.verticalLayoutWidget_3)
        self.lbl_ones.setObjectName(u"lbl_ones")
        self.lbl_ones.setFont(font5)

        self.verticalLayout_3.addWidget(self.lbl_ones)

        self.lbl_twos = QLabel(self.verticalLayoutWidget_3)
        self.lbl_twos.setObjectName(u"lbl_twos")
        self.lbl_twos.setFont(font5)

        self.verticalLayout_3.addWidget(self.lbl_twos)

        self.lbl_threes = QLabel(self.verticalLayoutWidget_3)
        self.lbl_threes.setObjectName(u"lbl_threes")
        self.lbl_threes.setFont(font5)

        self.verticalLayout_3.addWidget(self.lbl_threes)

        self.lbl_fours = QLabel(self.verticalLayoutWidget_3)
        self.lbl_fours.setObjectName(u"lbl_fours")
        self.lbl_fours.setFont(font5)

        self.verticalLayout_3.addWidget(self.lbl_fours)

        self.lbl_fives = QLabel(self.verticalLayoutWidget_3)
        self.lbl_fives.setObjectName(u"lbl_fives")
        self.lbl_fives.setFont(font5)

        self.verticalLayout_3.addWidget(self.lbl_fives)

        self.lbl_sixes = QLabel(self.verticalLayoutWidget_3)
        self.lbl_sixes.setObjectName(u"lbl_sixes")
        self.lbl_sixes.setFont(font5)

        self.verticalLayout_3.addWidget(self.lbl_sixes)

        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(830, 450, 111, 401))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_3same = QLabel(self.verticalLayoutWidget_4)
        self.lbl_3same.setObjectName(u"lbl_3same")
        self.lbl_3same.setFont(font5)

        self.verticalLayout_4.addWidget(self.lbl_3same)

        self.lbl_4same = QLabel(self.verticalLayoutWidget_4)
        self.lbl_4same.setObjectName(u"lbl_4same")
        self.lbl_4same.setFont(font5)

        self.verticalLayout_4.addWidget(self.lbl_4same)

        self.lbl_fullhouse = QLabel(self.verticalLayoutWidget_4)
        self.lbl_fullhouse.setObjectName(u"lbl_fullhouse")
        self.lbl_fullhouse.setFont(font5)

        self.verticalLayout_4.addWidget(self.lbl_fullhouse)

        self.lbl_smstr = QLabel(self.verticalLayoutWidget_4)
        self.lbl_smstr.setObjectName(u"lbl_smstr")
        self.lbl_smstr.setFont(font5)

        self.verticalLayout_4.addWidget(self.lbl_smstr)

        self.lbl_lgstr = QLabel(self.verticalLayoutWidget_4)
        self.lbl_lgstr.setObjectName(u"lbl_lgstr")
        self.lbl_lgstr.setFont(font5)

        self.verticalLayout_4.addWidget(self.lbl_lgstr)

        self.lbl_yhatzee = QLabel(self.verticalLayoutWidget_4)
        self.lbl_yhatzee.setObjectName(u"lbl_yhatzee")
        self.lbl_yhatzee.setFont(font5)

        self.verticalLayout_4.addWidget(self.lbl_yhatzee)

        self.lbl_chance = QLabel(self.verticalLayoutWidget_4)
        self.lbl_chance.setObjectName(u"lbl_chance")
        self.lbl_chance.setFont(font5)

        self.verticalLayout_4.addWidget(self.lbl_chance)

        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(60, 810, 51, 31))
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        self.btn_back.setFont(font6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_ones.clicked.connect(MainWindow.btn_ones_a)
        self.btn_twos.clicked.connect(MainWindow.btn_twos_a)
        self.btn_threes.clicked.connect(MainWindow.btn_threes_a)
        self.btn_fours.clicked.connect(MainWindow.btn_fours_a)
        self.btn_fives.clicked["bool"].connect(MainWindow.btn_fives_a)
        self.btn_sixes.clicked.connect(MainWindow.btn_sixes_a)
        self.btn_3same.clicked.connect(MainWindow.btn_3same_a)
        self.btn_4same.clicked.connect(MainWindow.btn_4same_a)
        self.btn_fullhouse.clicked.connect(MainWindow.btn_fullhouse_a)
        self.btn_smstr.clicked.connect(MainWindow.btn_smstr_a)
        self.btn_lgstr.clicked.connect(MainWindow.btn_lgstr_a)
        self.btn_yhatzee.clicked.connect(MainWindow.btn_yhatzee_a)
        self.btn_chance.clicked.connect(MainWindow.btn_chance_a)
        self.btn_roll.clicked.connect(MainWindow.btn_roll_a)
        self.btn_done.clicked.connect(MainWindow.btn_done_a)
        self.btn_exit.clicked.connect(MainWindow.btn_exit_a)
        self.btn_d1.clicked.connect(MainWindow.dice_click_a)
        self.btn_d2.clicked.connect(MainWindow.dice_click_a)
        self.btn_d3.clicked.connect(MainWindow.dice_click_a)
        self.btn_d4.clicked.connect(MainWindow.dice_click_a)
        self.btn_d5.clicked.connect(MainWindow.dice_click_a)
        self.btn_skip.clicked.connect(MainWindow.btn_skip_a)
        self.btn_back.clicked.connect(MainWindow.btn_back_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.lbl_background.setText("")
        self.btn_d2.setText("")
        self.btn_roll.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.btn_done.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.lbl_div1.setText("")
        self.lbl_div2.setText("")
        self.btn_3same.setText(QCoreApplication.translate("MainWindow", u"3 of a kind", None))
        self.btn_4same.setText(QCoreApplication.translate("MainWindow", u"4 of a kind", None))
        self.btn_fullhouse.setText(QCoreApplication.translate("MainWindow", u"Full House", None))
        self.btn_smstr.setText(QCoreApplication.translate("MainWindow", u"Sm Straight", None))
        self.btn_lgstr.setText(QCoreApplication.translate("MainWindow", u"Lg Straight", None))
        self.btn_yhatzee.setText(QCoreApplication.translate("MainWindow", u"Yhatzee", None))
        self.btn_chance.setText(QCoreApplication.translate("MainWindow", u"Chance", None))
        self.btn_skip.setText(QCoreApplication.translate("MainWindow", u"Skip Turn", None))
        self.btn_ones.setText(QCoreApplication.translate("MainWindow", u"Ones", None))
        self.btn_twos.setText(QCoreApplication.translate("MainWindow", u"Twos", None))
        self.btn_threes.setText(QCoreApplication.translate("MainWindow", u"Threes", None))
        self.btn_fours.setText(QCoreApplication.translate("MainWindow", u"Fours", None))
        self.btn_fives.setText(QCoreApplication.translate("MainWindow", u"Fives", None))
        self.btn_sixes.setText(QCoreApplication.translate("MainWindow", u"Sixes", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btn_d1.setText("")
        self.btn_d5.setText("")
        self.btn_d4.setText("")
        self.btn_d3.setText("")
        self.lbl_turn.setText(QCoreApplication.translate("MainWindow", u"Player 1's Turn", None))
        self.lbl_ones.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lbl_twos.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lbl_threes.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lbl_fours.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lbl_fives.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lbl_sixes.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lbl_3same.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lbl_4same.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lbl_fullhouse.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lbl_smstr.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lbl_lgstr.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lbl_yhatzee.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lbl_chance.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

