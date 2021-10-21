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
        MainWindow.resize(476, 296)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
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
        self.groupBox_2.setMinimumSize(QSize(700, 150))
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
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 3, 0, 1, 3)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_11 = QLabel(self.CommonView)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 0, 18, 1, 1)

        self.label_13 = QLabel(self.CommonView)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 16, 1, 1)

        self.label_16 = QLabel(self.CommonView)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 0, 13, 1, 1)

        self.label_14 = QLabel(self.CommonView)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 0, 15, 1, 1)

        self.label_8 = QLabel(self.CommonView)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 0, 19, 1, 1)

        self.label_12 = QLabel(self.CommonView)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 0, 17, 1, 1)

        self.label_28 = QLabel(self.CommonView)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_3.addWidget(self.label_28, 0, 1, 1, 1)

        self.label_29 = QLabel(self.CommonView)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_3.addWidget(self.label_29, 0, 0, 1, 1)

        self.label_17 = QLabel(self.CommonView)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 0, 12, 1, 1)

        self.label_23 = QLabel(self.CommonView)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 0, 6, 1, 1)

        self.label_24 = QLabel(self.CommonView)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_3.addWidget(self.label_24, 0, 5, 1, 1)

        self.label_22 = QLabel(self.CommonView)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 0, 7, 1, 1)

        self.manaCapSlider = QSlider(self.CommonView)
        self.manaCapSlider.setObjectName(u"manaCapSlider")
        self.manaCapSlider.setCursor(QCursor(Qt.SizeHorCursor))
        self.manaCapSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.manaCapSlider, 1, 0, 1, 20)

        self.label_20 = QLabel(self.CommonView)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 0, 9, 1, 1)

        self.label_21 = QLabel(self.CommonView)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 0, 8, 1, 1)

        self.label_26 = QLabel(self.CommonView)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_3.addWidget(self.label_26, 0, 3, 1, 1)

        self.label_18 = QLabel(self.CommonView)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 0, 11, 1, 1)

        self.label_25 = QLabel(self.CommonView)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_3.addWidget(self.label_25, 0, 4, 1, 1)

        self.label_27 = QLabel(self.CommonView)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_3.addWidget(self.label_27, 0, 2, 1, 1)

        self.label_19 = QLabel(self.CommonView)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 0, 10, 1, 1)

        self.label_15 = QLabel(self.CommonView)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 0, 14, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.CommonView)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 6, 1, 1, 1)

        self.label_3 = QLabel(self.CommonView)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)

        self.label = QLabel(self.CommonView)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(self.CommonView)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_6 = QLabel(self.CommonView)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 5, 1, 1, 1)

        self.label_4 = QLabel(self.CommonView)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)

        self.label_5 = QLabel(self.CommonView)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 4, 1, 1, 1)

        self.elementSlider = QSlider(self.CommonView)
        self.elementSlider.setObjectName(u"elementSlider")
        self.elementSlider.setCursor(QCursor(Qt.SizeVerCursor))
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
        self.menubar.setGeometry(QRect(0, 0, 476, 20))
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
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Best deck ever!", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"99", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Neutral", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Earth", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fire", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Water", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Dragon", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Live", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Death", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CommonView), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Page", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHELP.setTitle(QCoreApplication.translate("MainWindow", u"HELP!", None))
    # retranslateUi

