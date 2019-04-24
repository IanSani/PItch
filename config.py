import os

class Config:

    SECRET_KEY=('Ian')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ain:saniboy254@localhost/pitch'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch!'
    SENDER_EMAIL = 'iansani259@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    pass
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://ain:saniboy254@localhost/pitches_test'


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI =''

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(" postgresql-polished-69398")

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
