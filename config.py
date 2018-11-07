import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLED = False
    SECRET_KEY = 'somesecretkey'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/messanger'
    SQLALCHEMY_TRACK_MODIFICATIONS = False