"""CountryHistoricData Model."""

from config.database import Model


class CountryHistoricData(Model):
    """CountryHistoricData Model."""
    __table__ = 'countryhistoricdatas'
    __fillable__ = ['dates', 'new_deaths',
                    'new_cases', 'total_cases', 'total_deaths']
