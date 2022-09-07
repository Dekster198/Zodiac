import sys
import requests
from bs4 import BeautifulSoup
import fake_useragent
from PyQt5 import QtWidgets
from main import Ui_MainWindow
from parser import Parser

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    signs = {'овен': 'aries', 'телец': 'taurus', 'близнецы': 'gemini', 'рак': 'cancer', 'лев': 'leo', 'дева': 'virgo',
             'весы': 'libra', 'скорпион': 'scorpio', 'стрелец': 'sagittarius', 'козерог': 'capricorn', 'водолей': 'aquarius',
             'рыбы': 'pisces'}
    sign = input('Введите знак зодиака: ').lower()
    while sign not in signs:
        sign = input('Неправильно введён знак зодиака. Повторите попытку: ').lower()
    horo = Parser(signs[sign])
    horo.parsing()
    horo.print_horo()

    # sys.exit(app.exec())

if __name__ == '__main__':
    main()