"""A AfricaDataController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller

from app.AfricaData import AfricaData


class AfricaDataController(Controller):
    """AfricaDataController Controller Class."""

    def __init__(self, request: Request):
        """AfricaDataController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def single(self, view: View, request: Request):
        date = AfricaData.where('dates', request.param(
            'date')).first()
        if date is None:
            return '<h2>Be sure the date is between 2020-02-13 and yesterday date.</h2>'
        else:
            return {
                date.dates: {
                    'new_deaths': date.new_deaths,
                    'new_cases': date.new_cases,
                    'total_cases': date.total_cases,
                    'total_deaths': date.total_deaths
                }
            }

    def show(self, request: Request):
        return request.redirect('https://www.covidafrica.info/api')
