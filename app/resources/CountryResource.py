from masonite.api.resources import Resource
from app.Country import Country
from masonite.api.serializers import JSONSerializer


class CountryResource(Resource):
    model = Country
    methods = ['index', 'show']
