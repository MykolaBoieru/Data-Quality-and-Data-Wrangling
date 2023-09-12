# load packages
import requests
from bs4 import BeautifulSoup
import datetime as dt

# load a web page and extract its content
page = requests.get('https://coinmarketcap.com/currencies/bitcoin/')
soup = BeautifulSoup(page.content, 'html.parser')

# find and convert the price
price = soup.find('div', class_='sc-16891c57-0 hqcKQB flexStart alignBaseline').find(
    'span', class_='sc-16891c57-0 dxubiK base-text').text.replace("$", "").replace(",", "")
price = float(price)

# store insert datetime
insert_datetime = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")