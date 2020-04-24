''' Task Module Description '''
from masonite.scheduler.Task import Task
from app.Country import Country

import requests
from bs4 import BeautifulSoup


class UpdateData(Task):
    ''' Task description '''
    run_every = '1 minute'

    def __init__(self):
        pass

    def spliter(self, a):
        return a.split(',')

    def handle(self):
        data = self.formatter(self.scraper())

        for key in data.keys():

            Country.create(
                name=key,
                case_number=int(
                    "".join(self.spliter(data[key]['case_number']))),
                case_death=int(
                    "".join(self.spliter(data[key]['case_death']))),
                case_recovered=int(
                    "".join(self.spliter(data[key]['case_recovered'])))
            )

    def scraper(self):
        url = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Africa'

        page_content = requests.get(url).text

        soup = BeautifulSoup(page_content, features='html.parser')

        table = soup.find('table', attrs={'class': 'wikitable sortable'})
        data = table.find_all('tr')
        row = []

        for tr in data:
            row.append(tr.text.replace('\n', ' ').strip())
        return row

    def formatter(self, data):
        """
    Format the data returned by the scraper in usable format
    """

        # we delete the first and the last element of the list
        del data[0]
        data.pop()

        data_stats = {}

        country_stats = {}

        for element in data:

            element = element.split()
            element.pop()  # we delete the last element of the list which is a reference

            # some country have very long names so we extract the first strings
            country = element[:-3]
            # which represent the name of the country

            country = " ".join(country)
            # each element has a structure like this : ["countryname","number of case","number of death","number of recovered"]
            data_stats[country] = {
                "case_number": element[-3].replace(',', ''),
                "case_death": element[-2],
                "case_recovered": element[-1]
            }
        return data_stats
