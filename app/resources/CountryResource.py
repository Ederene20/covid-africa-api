from masonite.api.resources import Resource
from app.Country import Country
from masonite.api.serializers import JSONSerializer
from masonite.request import Request


class CountryResource(Resource, JSONSerializer):
    model = Country
    methods = ['index']
    without = ['id', 'created_at']

    def index(self):
        return self.model.all()
