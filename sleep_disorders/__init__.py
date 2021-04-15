import mysql.connector
from flask import Flask
from sleep_disorders.settings import settings
from flask_sqlalchemy import SQLAlchemy


mydatabase = mysql.connector.connect(
    host=settings.host,
    user=settings.user,
    password=settings.password,
    database=settings.database
)


app = Flask(__name__)
app.config['SECRET_KEY'] = settings.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/sleep_disorders'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)
app.config['SECRET_KEY'] = settings.secret_key


from sleep_disorders import routes

