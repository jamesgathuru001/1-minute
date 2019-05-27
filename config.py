import os


class Config:
    '''
    general configuration
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:james55@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    production configuration child class
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:james55@localhost/pitch_test'

class DevConfig(Config):
    '''
    development configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:james55@localhost/pitch'
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
