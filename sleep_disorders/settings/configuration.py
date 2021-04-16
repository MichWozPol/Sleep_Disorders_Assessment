from sleep_disorders.settings import db_settings as settings


class Config:
   SECRET_KEY = settings.secret_key
   SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{settings.user}:{settings.password}@{settings.host}/{settings.database}'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   SECRET_KEY = settings.secret_key
