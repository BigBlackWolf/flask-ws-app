from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from app.events import Chat
from app.stream import Stream
from config import Config

socketio = SocketIO()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'main.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes import main
    app.register_blueprint(main)

    socketio.init_app(app)
    socketio.on_namespace(Chat('/'))
    socketio.on_namespace(Stream('/stream'))
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    return app


from app import models