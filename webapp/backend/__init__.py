import os
import pickle
from config import config
from flask import Flask, jsonify

model = pickle.load(open('/data/model.pkl', 'rb'))


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    @app.route('/')
    def index():
        return jsonify("it works!")

    from .api import api
    app.register_blueprint(api)

    return app
