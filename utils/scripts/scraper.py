import requests
from bs4 import BeautifulSoup


def scraper():
    url = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Africa'

    page_content = requests.get(url).text

    soup = BeautifulSoup(page_content, features='html.parser')

    table = soup.find('table', attrs={'class': 'wikitable sortable'})
    data = table.find_all('tr')
    row = []

    for tr in data:
        row.append(tr.text.replace('\n', ' ').strip())
    return row
