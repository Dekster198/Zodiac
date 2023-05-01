import sys
import requests
from PyQt5.QtWidgets import QPushButton
from bs4 import BeautifulSoup
import fake_useragent
from PyQt5 import QtWidgets, QtGui, QtCore
from GUI import Ui_MainWindow
from parser import Parser

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.centralwidget.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Zodiac(logo).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.centralwidget.setWindowIcon(icon)

        self.ui.Aries.clicked.connect(lambda: self.printer(self.ui.Aries))
        self.ui.Taurus.clicked.connect(lambda: self.printer(self.ui.Taurus))
        self.ui.Gemini.clicked.connect(lambda: self.printer(self.ui.Gemini))
        self.ui.Cancer.clicked.connect(lambda: self.printer(self.ui.Cancer))
        self.ui.Lion.clicked.connect(lambda: self.printer(self.ui.Lion))
        self.ui.Virgo.clicked.connect(lambda: self.printer(self.ui.Virgo))
        self.ui.Libra.clicked.connect(lambda: self.printer(self.ui.Libra))
        self.ui.Scorpio.clicked.connect(lambda: self.printer(self.ui.Scorpio))
        self.ui.Sagittarius.clicked.connect(lambda: self.printer(self.ui.Sagittarius))
        self.ui.Capricorn.clicked.connect(lambda: self.printer(self.ui.Capricorn))
        self.ui.Aquarius.clicked.connect(lambda: self.printer(self.ui.Aquarius))
        self.ui.Pisces.clicked.connect(lambda: self.printer(self.ui.Pisces))

    def printer(self, btn):
        self.ui.textBrowser.clear()
        self.ui.btn = btn
        name = self.ui.btn.objectName().lower()
        timesForHoro = {'На вчера': 'yesterday', 'На сегодня': 'today', 'На завтра': 'tomorrow', 'На неделю': 'week',
                     'На месяц': 'month', 'На год': 'year'}
        interval = timesForHoro[self.ui.comboBox.currentText()]
        horo = Parser(name, interval)
        horo.parsing()
        horo.print_horo()
        self.ui.textBrowser.append(horo.print_horo())

def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()