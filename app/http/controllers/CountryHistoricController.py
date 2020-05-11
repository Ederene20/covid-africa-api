"""A CountryHistoricController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller

from app.CountryHistoric import CountryHistoric


class CountryHistoricController(Controller):
    """CountryHistoricController Controller Class."""

    def __init__(self, request: Request):
        """CountryHistoricController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def single(self, view: View, request: Request):
        country = CountryHistoric.where(
            'name', request.param('country').capitalize()).all()

        return 'country'
