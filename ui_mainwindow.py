# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QSlider, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(893, 386)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionShortcuts = QAction(MainWindow)
        self.actionShortcuts.setObjectName(u"actionShortcuts")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.CommonView = QWidget()
        self.CommonView.setObjectName(u"CommonView")
        self.gridLayout = QGridLayout(self.CommonView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.CommonView)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_5.addWidget(self.comboBox, 2, 0, 1, 1)

        self.label_selectedManaCap = QLabel(self.frame)
        self.label_selectedManaCap.setObjectName(u"label_selectedManaCap")

        self.gridLayout_5.addWidget(self.label_selectedManaCap, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(680, 150))
        self.gridLayout_7 = QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_pm4 = QLabel(self.groupBox_2)
        self.label_pm4.setObjectName(u"label_pm4")

        self.gridLayout_7.addWidget(self.label_pm4, 0, 3, 1, 1)

        self.label_pm2 = QLabel(self.groupBox_2)
        self.label_pm2.setObjectName(u"label_pm2")

        self.gridLayout_7.addWidget(self.label_pm2, 0, 1, 1, 1)

        self.label_pm7 = QLabel(self.groupBox_2)
        self.label_pm7.setObjectName(u"label_pm7")

        self.gridLayout_7.addWidget(self.label_pm7, 0, 6, 1, 1)

        self.label_pm3 = QLabel(self.groupBox_2)
        self.label_pm3.setObjectName(u"label_pm3")

        self.gridLayout_7.addWidget(self.label_pm3, 0, 2, 1, 1)

        self.label_pm5 = QLabel(self.groupBox_2)
        self.label_pm5.setObjectName(u"label_pm5")

        self.gridLayout_7.addWidget(self.label_pm5, 0, 4, 1, 1)

        self.label_pm6 = QLabel(self.groupBox_2)
        self.label_pm6.setObjectName(u"label_pm6")

        self.gridLayout_7.addWidget(self.label_pm6, 0, 5, 1, 1)

        self.label_pm1 = QLabel(self.groupBox_2)
        self.label_pm1.setObjectName(u"label_pm1")

        self.gridLayout_7.addWidget(self.label_pm1, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 1, 1, 2, 2)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_deck_Coment = QLabel(self.groupBox)
        self.label_deck_Coment.setObjectName(u"label_deck_Coment")

        self.gridLayout_6.addWidget(self.label_deck_Coment, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 3, 0, 1, 3)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_mana_30 = QLabel(self.CommonView)
        self.label_mana_30.setObjectName(u"label_mana_30")
        self.label_mana_30.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_30, 0, 18, 1, 1)

        self.label_mana_28 = QLabel(self.CommonView)
        self.label_mana_28.setObjectName(u"label_mana_28")
        self.label_mana_28.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_28, 0, 16, 1, 1)

        self.label_mana_25 = QLabel(self.CommonView)
        self.label_mana_25.setObjectName(u"label_mana_25")
        self.label_mana_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_25, 0, 13, 1, 1)

        self.label_mana_27 = QLabel(self.CommonView)
        self.label_mana_27.setObjectName(u"label_mana_27")
        self.label_mana_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_27, 0, 15, 1, 1)

        self.label_mana_99 = QLabel(self.CommonView)
        self.label_mana_99.setObjectName(u"label_mana_99")
        self.label_mana_99.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_99, 0, 19, 1, 1)

        self.label_mana_29 = QLabel(self.CommonView)
        self.label_mana_29.setObjectName(u"label_mana_29")
        self.label_mana_29.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_29, 0, 17, 1, 1)

        self.label_mana_13 = QLabel(self.CommonView)
        self.label_mana_13.setObjectName(u"label_mana_13")
        self.label_mana_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_13, 0, 1, 1, 1)

        self.label_mana_12 = QLabel(self.CommonView)
        self.label_mana_12.setObjectName(u"label_mana_12")
        self.label_mana_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_12, 0, 0, 1, 1)

        self.label_mana_24 = QLabel(self.CommonView)
        self.label_mana_24.setObjectName(u"label_mana_24")
        self.label_mana_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_24, 0, 12, 1, 1)

        self.label_mana_18 = QLabel(self.CommonView)
        self.label_mana_18.setObjectName(u"label_mana_18")
        self.label_mana_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_18, 0, 6, 1, 1)

        self.label_mana_17 = QLabel(self.CommonView)
        self.label_mana_17.setObjectName(u"label_mana_17")
        self.label_mana_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_17, 0, 5, 1, 1)

        self.label_mana_19 = QLabel(self.CommonView)
        self.label_mana_19.setObjectName(u"label_mana_19")
        self.label_mana_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_19, 0, 7, 1, 1)

        self.label_mana_21 = QLabel(self.CommonView)
        self.label_mana_21.setObjectName(u"label_mana_21")
        self.label_mana_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_21, 0, 9, 1, 1)

        self.label_mana_20 = QLabel(self.CommonView)
        self.label_mana_20.setObjectName(u"label_mana_20")
        self.label_mana_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_20, 0, 8, 1, 1)

        self.label_mana_15 = QLabel(self.CommonView)
        self.label_mana_15.setObjectName(u"label_mana_15")
        self.label_mana_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_15, 0, 3, 1, 1)

        self.label_mana_23 = QLabel(self.CommonView)
        self.label_mana_23.setObjectName(u"label_mana_23")
        self.label_mana_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_23, 0, 11, 1, 1)

        self.label_mana_16 = QLabel(self.CommonView)
        self.label_mana_16.setObjectName(u"label_mana_16")
        self.label_mana_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_16, 0, 4, 1, 1)

        self.label_mana_14 = QLabel(self.CommonView)
        self.label_mana_14.setObjectName(u"label_mana_14")
        self.label_mana_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_14, 0, 2, 1, 1)

        self.label_mana_22 = QLabel(self.CommonView)
        self.label_mana_22.setObjectName(u"label_mana_22")
        self.label_mana_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_22, 0, 10, 1, 1)

        self.label_mana_26 = QLabel(self.CommonView)
        self.label_mana_26.setObjectName(u"label_mana_26")
        self.label_mana_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_mana_26, 0, 14, 1, 1)

        self.manaCapSlider = QSlider(self.CommonView)
        self.manaCapSlider.setObjectName(u"manaCapSlider")
        self.manaCapSlider.setCursor(QCursor(Qt.SizeHorCursor))
        self.manaCapSlider.setMinimum(0)
        self.manaCapSlider.setSingleStep(5)
        self.manaCapSlider.setPageStep(5)
        self.manaCapSlider.setValue(0)
        self.manaCapSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.manaCapSlider, 1, 0, 1, 20)


        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_element_Neutral = QLabel(self.CommonView)
        self.label_element_Neutral.setObjectName(u"label_element_Neutral")

        self.gridLayout_2.addWidget(self.label_element_Neutral, 6, 1, 1, 1)

        self.label_element_Earth = QLabel(self.CommonView)
        self.label_element_Earth.setObjectName(u"label_element_Earth")

        self.gridLayout_2.addWidget(self.label_element_Earth, 2, 1, 1, 1)

        self.label_element_Fire = QLabel(self.CommonView)
        self.label_element_Fire.setObjectName(u"label_element_Fire")

        self.gridLayout_2.addWidget(self.label_element_Fire, 0, 1, 1, 1)

        self.label_element_Water = QLabel(self.CommonView)
        self.label_element_Water.setObjectName(u"label_element_Water")

        self.gridLayout_2.addWidget(self.label_element_Water, 1, 1, 1, 1)

        self.label_element_Dragon = QLabel(self.CommonView)
        self.label_element_Dragon.setObjectName(u"label_element_Dragon")

        self.gridLayout_2.addWidget(self.label_element_Dragon, 5, 1, 1, 1)

        self.label_element_Live = QLabel(self.CommonView)
        self.label_element_Live.setObjectName(u"label_element_Live")

        self.gridLayout_2.addWidget(self.label_element_Live, 3, 1, 1, 1)

        self.label_element_Death = QLabel(self.CommonView)
        self.label_element_Death.setObjectName(u"label_element_Death")

        self.gridLayout_2.addWidget(self.label_element_Death, 4, 1, 1, 1)

        self.elementSlider = QSlider(self.CommonView)
        self.elementSlider.setObjectName(u"elementSlider")
        self.elementSlider.setCursor(QCursor(Qt.SizeVerCursor))
        self.elementSlider.setContextMenuPolicy(Qt.NoContextMenu)
        self.elementSlider.setMaximum(97)
        self.elementSlider.setSingleStep(14)
        self.elementSlider.setPageStep(14)
        self.elementSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.elementSlider, 0, 0, 7, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.CommonView, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 893, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHELP = QMenu(self.menubar)
        self.menuHELP.setObjectName(u"menuHELP")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHELP.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuHELP.addAction(self.actionShortcuts)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(tooltip)
        self.actionQuit.setToolTip(QCoreApplication.translate("MainWindow", u"Quit from app", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionShortcuts.setText(QCoreApplication.translate("MainWindow", u"Shortcuts", None))
#if QT_CONFIG(whatsthis)
        self.CommonView.setWhatsThis(QCoreApplication.translate("MainWindow", u"Tab", None))
#endif // QT_CONFIG(whatsthis)
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Variant", None))

        self.label_selectedManaCap.setText(QCoreApplication.translate("MainWindow", u"12 Man,\n"
"Neutral", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Deck", None))
        self.label_pm4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_pm2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_pm7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_pm3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_pm5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_pm6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_pm1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Comment", None))
        self.label_deck_Coment.setText(QCoreApplication.translate("MainWindow", u"Best deck ever!", None))
        self.label_mana_30.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_mana_28.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.label_mana_25.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_mana_27.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.label_mana_99.setText(QCoreApplication.translate("MainWindow", u"99", None))
        self.label_mana_29.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.label_mana_13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_mana_12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_mana_24.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.label_mana_18.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.label_mana_17.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_mana_19.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_mana_21.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_mana_20.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_mana_15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_mana_23.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_mana_16.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.label_mana_14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_mana_22.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_mana_26.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.label_element_Neutral.setText(QCoreApplication.translate("MainWindow", u"Neutral", None))
        self.label_element_Earth.setText(QCoreApplication.translate("MainWindow", u"Earth", None))
        self.label_element_Fire.setText(QCoreApplication.translate("MainWindow", u"Fire", None))
        self.label_element_Water.setText(QCoreApplication.translate("MainWindow", u"Water", None))
        self.label_element_Dragon.setText(QCoreApplication.translate("MainWindow", u"Dragon", None))
        self.label_element_Live.setText(QCoreApplication.translate("MainWindow", u"Live", None))
        self.label_element_Death.setText(QCoreApplication.translate("MainWindow", u"Death", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CommonView), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Page", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHELP.setTitle(QCoreApplication.translate("MainWindow", u"HELP!", None))
    # retranslateUi

