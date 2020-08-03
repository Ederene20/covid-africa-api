""" Task Module Description """
from masonite.scheduler.Task import Task
from app.CountryHistoric import CountryHistoric

import pandas as pd
import requests


class UpdateCountryHistoricData(Task):
    """ Task description """
    run_every = '1 minute'

    def __init__(self):
        pass

    def handle(self):
        pass

    @staticmethod
    def africa_csv_to_df(self):

        countries_list = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Central African Republic', 'Chad', 'Democratic Republic of Congo', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Cote d\'Ivoire', 'Kenya', 'Liberia', 'Libya',
                          'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Mayotte', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Congo', 'Rwanda', 'Réunion', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Sao Tome and Principe', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Western Sahara', 'Zambia', 'Zimbabwe']

        df = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/full_data.csv',
                         index_col=1, parse_dates=True)

        df_africa = []
        for country in countries_list:
            for index, row in df.iterrows():
                if country == index:
                    df_africa.append(row)

        df_africa = pd.DataFrame(df_africa)

        return df_africa
