""" Global Flask Application Settings """

import os


class Config(object):
    """Base configuration."""

    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.dirname(__file__)
    CLIENT_DIR = os.path.join(BASE_DIR, 'client', 'vue_app')

    if not os.path.exists(CLIENT_DIR):
        raise Exception(
            'Client App directory not found: {}'.format(CLIENT_DIR))

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    """Development configuration."""

    DEBUG = True
    PRODUCTION = False
    SECRET_KEY = 'SuperSecretKey'
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(Config.BASE_DIR, 'app.db'))

class ProdConfig(Config):
    """Production configuration."""

    DEBUG = False
    PRODUCTION = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'UnsafeSecret')

class TestConfig(Config):
    """Testing configuration."""

    TESTING = True
    PRODUCTION = False
