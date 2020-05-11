"""CountryHistoric Model."""

from config.database import Model


class CountryHistoric(Model):
    """CountryHistoric Model."""
    __table__ = 'countryhistoricdatas'
    __fillable__ = ['dates', 'new_deaths',
                    'new_cases', 'total_cases', 'total_deaths']
