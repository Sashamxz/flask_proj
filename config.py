from importlib.resources import path
import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.join(os.path.dirname(__file__))

# # Platforma
# WIN = sys.platform.startswith('win')
# if WIN:
#     prefix = 'sqlite:///'
# else:
#     prefix = 'sqlite:////'


class Config():
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL')
    SECURITY_PASSWORD_SALT = os.getenv('SALT')
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing'    : TestingConfig,
    'production': ProductionConfig}
