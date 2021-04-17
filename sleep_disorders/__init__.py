import mysql.connector
from flask import Flask, Blueprint
#from flask_sqlalchemy import SQLAlchemy
from sleep_disorders.settings.configuration import Config
from sleep_disorders.settings import db_settings as settings
from sleep_disorders.errors.handlers import errors

mydatabase = mysql.connector.connect(
    host=settings.host,
    user=settings.user,
    password=settings.password,
    database=settings.database
)


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(errors)
#db = SQLAlchemy(app)

from sleep_disorders import routes
