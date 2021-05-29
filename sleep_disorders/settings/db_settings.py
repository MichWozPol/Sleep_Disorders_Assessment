from decouple import config

secret_key = config("secret_key")
host = config("host")
user = config("user")
password = config("password")
database = config("database")
port = config("port")
pool_recycle=280
track_modifications = False
pre_ping = True
timeout = 20
