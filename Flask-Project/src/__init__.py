from flask import Flask
from .config import config
from .db import db, migrate

def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])

    # Initialize the database and migrations
    db.init_app(app)
    migrate.init_app(app, db)

    return app
