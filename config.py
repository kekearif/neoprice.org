import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'HD73HFY8329742HDG'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    JSON_PATH = "/Users/kekearif/Documents/neoprice.org/app/static/prices.json"


class ProductionConfig(Config):
    PROD = True
    JSON_PATH = "/var/www/neoprice.org/app/static/prices.json"


config = {
    'default': DevelopmentConfig,
    'prod': ProductionConfig
}
