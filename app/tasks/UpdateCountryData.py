"""This task updates the data about each country in Africa. It's meant to be run as many times as possible.
As Wikipedia updates the data two times per day, so we'll run this one two times per day.
"""
from masonite.scheduler.Task import Task
from app.Country import Country

import requests
from bs4 import BeautifulSoup


class UpdateCountryData(Task):

    run_every = '1 minute'

    def __init__(self):
        pass

    @staticmethod
    def splitter(self, a):
        # As the data comes form wikipedia, there times somme characters may introducdes some errors.
        a = a.split('[')
        a = a[0].split(',')
        return a

    def handle(self):
        data = self.formatter(self, data=self.scraper(self))

        for key in data.keys():

            country = Country.where('name', key).first()
            if country is not None:
                country.active_case = int(
                    "".join(self.splitter(self, a=data[key]['active_case'])))
                country.case_number = int(
                    "".join(self.splitter(self, a=data[key]['case_number'])))
                country.case_death = int(
                    "".join(self.splitter(self, a=data[key]['case_death'])))
                country.case_recovered = int(
                    "".join(self.splitter(self, a=data[key]['case_recovered'])))
                country.save()
            else:
                Country.create(
                    name=key,
                    active_case=int(
                        "".join(self.splitter(self, a=data[key]['active_case']))),
                    case_number=int(
                        "".join(self.splitter(self, a=data[key]['case_number']))),
                    case_death=int(
                        "".join(self.splitter(self, a=data[key]['case_death']))),
                    case_recovered=int(
                        "".join(self.splitter(self, a=data[key]['case_recovered'])))
                )

    @staticmethod
    def scraper(self):
        url = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Africa'

        page_content = requests.get(url).text

        soup = BeautifulSoup(page_content, features='html.parser')

        table = soup.find('table', attrs={'class': 'wikitable sortable plainrowheaders'})
        data = table.find_all('tr')
        row = []

        for tr in data:
            row.append(tr.text.replace('\n', ' ').strip())
        return row

    @staticmethod
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
            if ']' in element[-1]:
                element.pop()  # we delete the last element of the list which is a reference
            for b in element:
                if ']' in b:
                    element.remove(b)
            # some country have very long names so we extract the first strings
            country = element[:-4]
            # which represent the name of the country

            country = " ".join(country)
            # We must modify some contries name to show it in google-charts
            if country == "Democratic Republic of the Congo":
                country = "Democratic Republic of Congo"
            if country == "Republic of Congo":
                country = "Congo"
            # each element has a structure like this : ["countryname","active cases","number of case","number of
            # death","number of recovered"]
            data_stats[country] = {
                "case_number": element[-4],
                "active_case": element[-3],
                "case_death": element[-1],
                "case_recovered": element[-2]
            }
        return data_stats
