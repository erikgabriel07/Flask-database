from flask import Flask
from settings.config import Config
from database.sessao import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    return app
