from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app import mydatabase as db
#from app import db


##TO BE CORRECTED

class Answer(db.Model):
    question = db.ForeignKey('Question', db.DO_NOTHING)
    content = db.TextField()

    class Meta:
        managed = False
        db_table = 'answer'


class Question(db.Model):
    content = db.TextField()
    type = db.CharField(max_length=50)
    max_answ_nb = db.IntegerField()

    class Meta:
        managed = False
        db_table = 'question'


class User(db.Model):
    created_at = db.DateTimeField()
    ip = db.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'user'


class Vote(db.Model):
    question = db.ForeignKey(Question, db.DO_NOTHING)
    answer = db.ForeignKey(Answer, db.DO_NOTHING)
    user = db.ForeignKey(User, db.DO_NOTHING)

    class Meta:
        db_table = 'vote'
