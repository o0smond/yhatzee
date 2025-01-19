# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_2.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
        self.btn_roll = QPushButton(self.centralwidget)
        self.btn_roll.setObjectName(u"btn_roll")
        self.btn_roll.setGeometry(QRect(160, 620, 141, 51))
        font1 = QFont()
        font1.setFamilies([u"C059"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.btn_roll.setFont(font1)
        self.btn_done = QPushButton(self.centralwidget)
        self.btn_done.setObjectName(u"btn_done")
        self.btn_done.setGeometry(QRect(160, 680, 141, 51))
        self.btn_done.setFont(font1)
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.verticalLayoutWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalLayoutWidget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        font2 = QFont()
        font2.setFamilies([u"C059"])
        font2.setBold(True)
        self.btn_exit.setFont(font2)
        self.btn_d1 = QPushButton(self.centralwidget)
        self.btn_d1.setObjectName(u"btn_d1")
        self.btn_d1.setGeometry(QRect(170, 10, 121, 111))
        self.btn_d5 = QPushButton(self.centralwidget)
        self.btn_d5.setObjectName(u"btn_d5")
        self.btn_d5.setGeometry(QRect(170, 490, 121, 111))
        self.btn_d4 = QPushButton(self.centralwidget)
        self.btn_d4.setObjectName(u"btn_d4")
        self.btn_d4.setGeometry(QRect(170, 370, 121, 111))
        self.btn_d3 = QPushButton(self.centralwidget)
        self.btn_d3.setObjectName(u"btn_d3")
        self.btn_d3.setGeometry(QRect(170, 250, 121, 111))
        self.lbl_turn = QLabel(self.centralwidget)
        self.lbl_turn.setObjectName(u"lbl_turn")
        self.lbl_turn.setGeometry(QRect(150, 740, 151, 51))
        font3 = QFont()
        font3.setFamilies([u"C059"])
        font3.setPointSize(16)
        self.lbl_turn.setFont(font3)
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
        self.btn_d5.clicked.connect(MainWindow.btn_d6_a)
        self.btn_d4.clicked.connect(MainWindow.btn_d5_a)
        self.btn_d3.clicked.connect(MainWindow.btn_d4_a)
        self.btn_d2.clicked.connect(MainWindow.btn_d2_a)
        self.btn_d1.clicked.connect(MainWindow.btn_d1_a)

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
    # retranslateUi

