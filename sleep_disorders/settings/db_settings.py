import os
from decouple import config

#secret_key = '5c357453c419ecbb80cd6603f35967f4'
secret_key = config("secret_key")
#host = "localhost"
host = config("host")
#user = "root"
user = config("user")
#password=""
password = config("password")
#database="sda_new"
database = config("database")
pool_recycle=280
track_modifications = False
pre_ping = True
timeout = 20
