from flask import Flask
from src.config import config
from src.db import db, migrate


def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])

    # Initialize the database and migrations
    db.init_app(app)
    migrate.init_app(app, db)

    return app
