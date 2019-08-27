import pickle
from flask import Flask, jsonify

model = pickle.load(open("/data/model.pkl", "rb"))


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("/app/webapp/config.py", silent=True)

    @app.route("/")
    def index():
        return jsonify("it works!")

    from .api import api

    app.register_blueprint(api)

    return app
