import requests
from bs4 import BeautifulSoup

def change_type():
    url = 'https://mx.investing.com/currencies/usd-mxn'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    command = soup.find('div', class_='mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6').get_text()
    time = soup.find('time').get_text()
    print(command, time)

change_type()