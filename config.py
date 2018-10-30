import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLED = False
    SECRET_KEY = 'somesecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False