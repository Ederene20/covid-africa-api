"""Base Database Seeder Module."""

from orator.seeds import Seeder
from .user_table_seeder import UserTableSeeder

from .country_table_seeder import CountryTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """Run the database seeds."""
        self.call(UserTableSeeder)

        self.call(CountryTableSeeder)
