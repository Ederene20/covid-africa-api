from masonite.api.resources import Resource
from masonite.request import Request
from app.AfricaData import AfricaData


class AfricaResource(Resource):
    model = AfricaData
    methods = ['index']
    without = ['created_at']
