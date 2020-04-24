"""AfricaData Model."""

from config.database import Model


class AfricaData(Model):
    """AfricaData Model."""
    __table__ = 'africadatas'
    __fillable__ = ['dates', 'new_deaths',
                    'new_cases', 'total_cases', 'total_deaths']
