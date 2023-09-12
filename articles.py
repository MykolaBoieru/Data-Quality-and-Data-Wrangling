# load packages
import requests
from bs4 import BeautifulSoup
import datetime as dt

# load a web page and extract its content
page = requests.get('https://wikicount.net/')
soup = BeautifulSoup(page.content, 'html.parser')

# find and convert amount of articles
articles = soup.find('div', class_='number').text.replace(",", "")
articles = int(articles)

# find and convert amount of words per article
words = soup.find('div').find('strong').text.replace(",", "")
words = int(words)

# store insert datetime
insert_datetime = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
