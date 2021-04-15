from sleep_disorders import db
from sqlalchemy import Table



class Answer(db.Model):
    __table__ = Table('answer', db.Model.metadata, autoload=True)


class Question(db.Model):
    __table__ = Table('question', db.Model.metadata, autoload=True)


class User(db.Model):
    __table__ = Table('user', db.Model.metadata, autoload=True)


class Vote(db.Model):
    __table__ = Table('vote', db.Model.metadata, autoload=True)
