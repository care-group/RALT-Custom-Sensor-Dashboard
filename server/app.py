# flask packages
from flask import Flask, app
from flask_restful import Api
from flask_cors import CORS, cross_origin

# local packages
from api.routes import create_routes

# external packages
import os

def get_flask_app(config: dict = None) -> app.Flask:
    # init flask
    flask_app = Flask(__name__)

    # configure app
    flask_app.config.update()

    # init api and routes
    api = Api(app=flask_app)
    create_routes(api=api)

    return flask_app

if __name__ == '__main__':
    app = get_flask_app()
    
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.run(debug=True, host='0.0.0.0')
