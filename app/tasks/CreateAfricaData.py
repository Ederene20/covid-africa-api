''' This task insert data since the beginning of the epidemic in Africa in the Data Base. It's meaned to 
run just once.'''
from masonite.scheduler.Task import Task

import pandas as pd
import requests

from app.AfricaData import AfricaData


class CreateAfricaData(Task):
    ''' Task description '''
    run_every = '1 minute'

    def __init__(self):
        pass

    def handle(self):
        data = self.africa_df_to_dict(self.africa_csv_to_df())

        for entry in data:
            AfricaData.create(
                dates=entry['date'],
                new_cases=entry['new_cases'],
                new_deaths=entry['new_deaths'],
                total_cases=entry['total_cases'],
                total_deaths=entry['total_deaths']
            )

    def africa_csv_to_df(self):

        countries_list = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Central African Republic', 'Chad', 'Democratic Republic of the Congo', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Liberia', 'Libya',
                          'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Mayotte', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Republic of the Congo', 'Rwanda', 'Réunion', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'São Tomé and Príncipe', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Western Sahara', 'Zambia', 'Zimbabwe']

        df = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/full_data.csv',
                         index_col=1, parse_dates=True)

        df_africa = []
        for country in countries_list:
            for index, row in df.iterrows():
                if country == index:
                    df_africa.append(row)

        df_africa = pd.DataFrame(df_africa)

        return df_africa

    # Here we'll try to get the total of cases and cases death in all Africa

    def africa_df_to_dict(self, df_africa):
        df_africa.sort_values(by=['date'])

        dates = df_africa['date'].tolist()
        dates = list(dict.fromkeys(dates))
        dates.sort()
        sum_list = []
        for date in dates:
            df_temp = df_africa.loc[df_africa['date'] == date]
            sum_list.append(df_temp.sum())
        # print(sum_list)
        sum_list = pd.DataFrame(sum_list)
        sum_list['date'] = sum_list['date'].apply(lambda x: x[:10])
        #sum_list = sum_list.set_index('date')

        #sum_list['date'] = pd.to_datetime(sum_list['date'])
        df_africa_total = sum_list.to_dict(orient='records')

        return df_africa_total
