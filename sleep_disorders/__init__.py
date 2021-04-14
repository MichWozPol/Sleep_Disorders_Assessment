import mysql.connector
from flask import Flask
from flask_bootstrap import Bootstrap
from sleep_disorders.settings import settings

mydatabase = mysql.connector.connect(
    host=settings.host,
    user=settings.user,
    password=settings.password,
    database=settings.database
)

app = Flask(__name__)
app.config['SECRET_KEY'] = settings.secret_key
Bootstrap(app)


from sleep_disorders import routes