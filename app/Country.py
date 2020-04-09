"""Country Model."""

from config.database import Model


class Country(Model):
    """Country Model."""

    __table__ = 'countriestats'
    __fillable__ = ['short_name', 'name',
                    'case_number', 'case_death', 'case_recovered']
