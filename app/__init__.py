from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
import os

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app


if os.getenv("PROD"):
    app = create_app('prod')


# Temp fix but need to make it work !
# app = create_app('prod')
