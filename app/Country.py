"""Country Model."""

from config.database import Model


class Country(Model):
    """Country Model."""

    __table__ = 'countries'
    __fillable__ = ['name', 'active_case',
                    'case_number', 'case_death', 'case_recovered']
