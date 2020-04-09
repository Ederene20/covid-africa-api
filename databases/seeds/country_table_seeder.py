from orator.seeds import Seeder
from app.Country import Country

from config.factories import factory


class CountryTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        factory(Country, 55).create()
