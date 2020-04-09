"""Web Routes."""

from masonite.routes import Get, Post

from app.resources.CountryResource import CountryResource

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),

    # Api Routes
    CountryResource('/api/countries').routes(),
]
