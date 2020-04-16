"""Web Routes."""

from masonite.routes import Get, Post

from app.resources.CountryResource import CountryResource
from app.resources.AfricaResource import AfricaResource

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),

    # Api Routes
    CountryResource('/api/africa/countries').routes(),
    AfricaResource('/api/africa').routes(),
]
