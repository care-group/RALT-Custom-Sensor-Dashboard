# flask packages
from flask_restful import Api

# project resources
from api.sensors import SensorsApi

def create_routes(api: Api):
    api.add_resource(SensorsApi, '/update')