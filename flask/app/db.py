# linking to the database
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()
migrate= Migrate()