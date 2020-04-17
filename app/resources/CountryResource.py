from masonite.api.resources import Resource
from app.Country import Country
from masonite.api.serializers import JSONSerializer
from masonite.request import Request


class CountryResource(Resource, JSONSerializer):
    model = Country
    methods = ['index', 'show']
    without = ['created_at']

    def show(self, request: Request):
        # dd(request.input('name'))
        return self.model.where('name', request.input('name')).first()

    def index(self):
        return self.model.all()
