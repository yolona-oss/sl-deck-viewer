import sys
import math
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QFile, Slot
from PySide6.QtCore import Qt
from ui_mainwindow import Ui_MainWindow

from config import IMG_PATH
from config import IMAGE_SCALE

from config import ManaCapVariants
from config import ManaCapFirstVal
from config import ManaCapLinearFor
from config import ManaCapLastStep
from config import Elements


class MainWindow(QMainWindow):
        
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionQuit.triggered.connect(lambda: sys.exit())

        self.manaCap = ManaCapFirstVal
        self.elementN = 0
        self.element = Elements[self.elementN]
        self.elementsLabels = [self.ui.label_element_Neutral,\
                self.ui.label_element_Dragon,\
                self.ui.label_element_Death,\
                self.ui.label_element_Live,\
                self.ui.label_element_Earth,\
                self.ui.label_element_Water,\
                self.ui.label_element_Fire]
        self.manaCapLabels = [self.ui.label_mana_12,\
                self.ui.label_mana_13,\
                self.ui.label_mana_14,\
                self.ui.label_mana_15,\
                self.ui.label_mana_16,\
                self.ui.label_mana_17,\
                self.ui.label_mana_18,\
                self.ui.label_mana_19,\
                self.ui.label_mana_20,\
                self.ui.label_mana_21,\
                self.ui.label_mana_22,\
                self.ui.label_mana_23,\
                self.ui.label_mana_24,\
                self.ui.label_mana_25,\
                self.ui.label_mana_26,\
                self.ui.label_mana_27,\
                self.ui.label_mana_28,\
                self.ui.label_mana_29,\
                self.ui.label_mana_30,\
                self.ui.label_mana_99]

        # self.ui.manaCapSlider.setTickInterval(round(100/ManaCapVariants)*2)

        #SET DEF DECK

        self.ui.manaCapSlider.valueChanged[int].connect(self.manaCapChanged)
        self.ui.elementSlider.valueChanged[int].connect(self.elementChanged)

    def setCurBold(self, list, cur):
        i = 0
        for elem in list:
            if i == cur:
                elem.setStyleSheet("font-weight: bold;")
            else:
                elem.setStyleSheet("font-weight: normal;")
            i = i + 1


    def onChange(self):
        self.ui.label_selectedManaCap.setText(str(self.manaCap) + ' Mana'\
                + '\n' + self.element)

        self.setCurBold(self.elementsLabels, self.elementN)
        self.setCurBold(self.manaCapLabels, self.manaCap - ManaCapFirstVal)

        pixmaps = [1, 4, 4, 28, 1, 7, 0, 7]
        labels = [self.ui.label_pm1, self.ui.label_pm2, self.ui.label_pm3, self.ui.label_pm4, self.ui.label_pm5,self.ui.label_pm6, self.ui.label_pm7]

        f = open('assets/decks/' + self.element + '/' + str(self.manaCap), 'r')
        lines = f.readlines()

        i = 0
        for line in lines:
            path = str(IMG_PATH + '/' + line[:-1] + '.png')
            pixmaps[i] = QPixmap(path)
            labels[i].setPixmap(pixmaps[i].scaled(100, 100, Qt.KeepAspectRatio))
            i = i+1

        f.close()

        while i < 7:
            labels[i].setPixmap(QPixmap())
            i = i+1


    def manaCapChanged(self, val):
        mana = ManaCapFirstVal + \
                math.floor(val / round( 100/ManaCapVariants ))

        if (mana == ManaCapLinearFor):
            mana = ManaCapLastStep

        self.manaCap = mana
        self.onChange()


    def elementChanged(self, val):
        element = math.floor(val / round( 98/len(Elements) ) )

        if (element >= len(Elements)):
                element = len(Elements) - 1

        self.element = Elements[element]
        self.elementN = element
        self.onChange()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
