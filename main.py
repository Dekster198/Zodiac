import sys
import requests
from bs4 import BeautifulSoup
import fake_useragent
from PyQt5 import QtWidgets
from GUI import Ui_MainWindow
from GUI import mywindow

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

url = 'https://orakul.com/'
aquarius_url = 'https://orakul.com/horoscope/astrologic/general/aries/today.html'
response = requests.get(aquarius_url, headers=header)
soup = BeautifulSoup(response.text, 'lxml')

aquarius_block = soup.find('div', class_='contentOnly')
birthday = aquarius_block.find('div', class_='sm-descr')
horo_date = aquarius_block.find('h2', class_='typehead')
horo_block = aquarius_block.find('p', class_='')
print(f'Дата рождения: {birthday.text.strip()}\n{horo_date.text.strip()}\n{horo_block.text.strip()}')

sys.exit(app.exec())