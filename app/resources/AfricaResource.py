from masonite.api.resources import Resource
from app.AfricaData import AfricaData
from masonite.api.serializers import JSONSerializer


class AfricaResource(Resource, JSONSerializer):
    model = AfricaData
    methods = ['index']
    without = ['id', 'created_at']

    def index(self):
        return self.model.all()
