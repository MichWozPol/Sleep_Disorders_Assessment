from sleep_disorders.settings import db_settings as settings


class Config:
   SECRET_KEY = settings.secret_key
   #SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{settings.user}:{settings.password}@{settings.host}:{settings.port}/{settings.database}'
   SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{settings.user}@{settings.host}:{settings.port}/{settings.database}'
   SQLALCHEMY_TRACK_MODIFICATIONS = settings.track_modifications
   SECRET_KEY = settings.secret_key
   SQLALCHEMY_POOL_RECYCLE = settings.pool_recycle
   SQLALCHEMY_POOL_TIMEOUT = settings.timeout
   SQLALCHEMY_POOL_PRE_PING = settings.pre_ping