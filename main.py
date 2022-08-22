import sys
import requests
from bs4 import BeautifulSoup
import fake_useragent
from PyQt5 import QtWidgets
from GUI import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

url = 'https://orakul.com/'
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'lxml')