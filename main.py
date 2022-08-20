import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

url = 'https://orakul.com/'
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'lxml')