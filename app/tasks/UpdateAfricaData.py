"""This task updates the data about Africa historically. It's meant to be run as many times as possible.
As OurWorldInData updates the data two times per day, so we'll run this one two times per day."""
from masonite.scheduler.Task import Task
import pandas as pd

from app.AfricaData import AfricaData


class UpdateAfricaData(Task):
    run_every = '1 minute'

    def __init__(self):
        pass

    def handle(self):
        data = self.africa_df_to_dict(self.africa_csv_to_df())
        # We would normally add a simple line to insert just the last element, but OurWorldInData has
        # the habit to correct some errors
        # So for the sake of safety, we'll update every thing again.
        for entry in data:
            date = AfricaData.where('dates', entry['date']).first()
            if date is not None:
                date.new_cases = entry['new_cases']
                date.new_deaths = entry['new_deaths']
                date.total_cases = entry['total_cases']
                date.total_deaths = entry['total_deaths']
                print(date.dates)
                date.save()
            else:
                AfricaData.create(
                    dates=entry['date'],
                    new_cases=entry['new_cases'],
                    new_deaths=entry['new_deaths'],
                    total_cases=entry['total_cases'],
                    total_deaths=entry['total_deaths']
                )

    @staticmethod
    def africa_csv_to_df(self):

        countries_list = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde',
                          'Central African Republic', 'Chad', 'Democratic Republic of Congo', 'Djibouti', 'Egypt',
                          'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea',
                          'Guinea-Bissau', 'Cote d\'Ivoire', 'Kenya', 'Liberia', 'Libya',
                          'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Mayotte', 'Morocco', 'Mozambique',
                          'Namibia', 'Niger', 'Nigeria', 'Congo', 'Rwanda', 'Réunion', 'Senegal', 'Seychelles',
                          'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Sao Tome and Principe',
                          'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Western Sahara', 'Zambia', 'Zimbabwe']
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

    @staticmethod
    def africa_df_to_dict(self, df_africa):
        df_africa.sort_values(by=['date'])

        dates = df_africa['date'].tolist()
        dates = list(dict.fromkeys(dates))

        dates.sort()

        # The first case of Covid Africa was introduced the 2020-02-04, so we split the dates list
        dates = dates[44:]

        sum_list = []
        for date in dates:
            df_temp = df_africa.loc[df_africa['date'] == date]
            sum_list.append(df_temp.sum())
        # print(sum_list)
        sum_list = pd.DataFrame(sum_list)
        sum_list['date'] = sum_list['date'].apply(lambda x: x[:10])
        # sum_list = sum_list.set_index('date')

        # sum_list['date'] = pd.to_datetime(sum_list['date'])
        df_africa_total = sum_list.to_dict(orient='records')

        return df_africa_total
