from flask import Flask
from .config import Config
from .db import db,migrate
from .models import *
from app.routes import student_bp
def create_app():

        app= Flask(__name__)
        app.config.from_object(Config)

        db.init_app(app)
        migrate.init_app(app,db)

        app.register_blueprint(student_bp)

        return app