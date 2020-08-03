"""A AfricaCountryController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller

from app.Country import Country


class AfricaCountryController(Controller):
    """AfricaCountryController Controller Class."""

    def __init__(self, request: Request):
        """AfricaCountryController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def single(self, request: Request, view: View):
        country = Country.where('name', request.param(
            'country').capitalize()).first()
        # dd(Country.where('name', request.input('name')).first())
        if country is None:
            return '<h3>There is no country of this name.</h3>'
        else:
            return {'country': {
                'case_number': country.case_number,
                'case_recovered': country.case_recovered,
                'case_death': country.case_death
            }}
