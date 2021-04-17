import mysql.connector
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sleep_disorders.settings.configuration import Config
from sleep_disorders.settings import db_settings as settings
from sleep_disorders.errors.handlers import errors
from sqlalchemy.ext.automap import automap_base


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(errors)
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)
Base = automap_base()
Base.prepare(db.engine, reflect=True)


from sleep_disorders import routes
