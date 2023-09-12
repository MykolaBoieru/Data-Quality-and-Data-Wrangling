# load packages
import requests
from bs4 import BeautifulSoup
import datetime as dt


# load a web page and extract its content
page = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(page.content, 'html.parser')

# find and convert amount of cases
case_one = soup.find_all('div', class_="maincounter-number")[0].find('span').text.replace(",", "")
total_cases = case_one.split()
total_cases = ''.join(total_cases)
total_cases = int(total_cases)

# find and convert amount of deaths
deaths = soup.find_all('div', class_="maincounter-number")[1].find('span').text.replace(",", "")
deaths = int(deaths)

# find and convert amount of recovered
recovered = soup.find_all('div', class_="maincounter-number")[2].find('span').text.replace(",", "")
recovered = int(recovered)

# store insert datetime
insert_datetime = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

