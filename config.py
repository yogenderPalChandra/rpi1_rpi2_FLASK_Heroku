
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'bittoo'
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = "postgresql://yogi:bittoo@localhost:5432/TemaccessToRemoteRp2"
    #QLALCHEMY_DATABASE_URI ="postgresql://yogi:bittoo@10.208.8.121:5432/flow"
    #SQLALCHEMY_BINDS = {
    #'flow':     "postgresql://yogi:bittoo@localhost:5432/TemaccessToRemoteRp2"}
    SQLALCHEMY_BINDS = {'flow':     "postgresql://yogi:bittoo@10.208.8.121:5432/flow"}


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
