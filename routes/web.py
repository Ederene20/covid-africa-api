"""Web Routes."""

from masonite.routes import Get, Post
from masonite.request import Request
from app.resources.CountryResource import CountryResource
from app.resources.AfricaResource import AfricaResource

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),

    Get('/api/countries/@country',
        'AfricaCountryController@single').name('country'),
    # Api Routes
    CountryResource('/api/africa/countries').routes(),

    # Get(CountryResource('api/africa/countries/@name/').show(request=Request)),

    AfricaResource('/api/africa').routes(),
]
