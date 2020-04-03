import os
from os import environ
basedir=os.path.abspath(os.path.dirname(__file__))


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Flask-Assets
    LESS_BIN = environ.get('LESS_BIN')
    ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = environ.get('STATIC_FOLDER')
    TEMPLATES_FOLDER = environ.get('TEMPLATES_FOLDER')
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')



    """Base config vars."""

    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')


    CONF = {"database": {"connection": "mysql+pymysql://lamtv10:lamtv10@172.16.29.196/auto_lamtv10"}}
    #db_engine = db.create_engine(CONF["database"]["connection"])
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_size": 200, "max_overflow": 200}
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        CONF["database"]["connection"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False