import requests
from bs4 import BeautifulSoup
import fake_useragent

class Parser:
    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}
    def __init__(self, sign, interval):
        self.sign = sign
        self.interval = interval
    def parsing(self):
        url = f'https://orakul.com/horoscope/astrologic/general/{self.sign}/{self.interval}.html'
        response = requests.get(url, headers=self.header)
        soup = BeautifulSoup(response.text, 'lxml')

        block = soup.find('div', class_='contentOnly')
        self.horo_title = block.find('h1')
        self.birthday = block.find('div', class_='sm-descr')
        self.horo_date = block.find('h2', class_='typehead')
        self.horo_block = block.find('p', class_='')
    def print_horo(self):
        return(f'Знак зодиака: {self.horo_title.text.strip()}\nДата рождения: {self.birthday.text.strip()}\n{self.horo_date.text.strip()}\n'
              f'{self.horo_block.text.strip()}')