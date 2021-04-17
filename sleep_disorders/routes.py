import datetime

from sqlalchemy.ext.automap import automap_base

from sleep_disorders import mydatabase
from flask import request, flash, redirect, render_template, url_for
from sleep_disorders import app

from sleep_disorders import db
# from sleep_disorders.models.models import Answer


@app.route('/', methods=["GET", "POST"])
def home():
    # print(Answer.query.filter_by(id=2))
    # mycursor = mydatabase.cursor()
    # mycursor.execute("SELECT * FROM question")
    # questions = mycursor.fetchall()
    # mycursor.execute("SELECT * FROM answer")
    # answer = mycursor.fetchall()
    # mycursor.execute("SELECT ip FROM user")
    # ip = mycursor.fetchall()
    # mycursor.close()

    Base = automap_base()
    Base.prepare(db.engine, reflect=True)
    Questions = Base.classes.question
    Answers = Base.classes.answer
    User = Base.classes.user
    Votes = Base.classes.vote

    questions = db.session.query(Questions).all()
    answer = db.session.query(Answers).all()
    user = db.session.query(User).all()

    for user in user:
        print(user.ip)

    if request.method == "POST":
        print(request.form)
        ip_address = request.headers['X-Real-IP']
        # ip_address = request.remote_addr

        if ip_address not in (item.ip for item in user):
            date = datetime.datetime.now()
            print(f"data {date} ip: {ip_address}")

            new_user = User(created_at=date, ip=ip_address)
            db.session.add(new_user)
            db.session.commit()

            user = db.session.query(User).filter(User.ip == ip_address).first()

            for key, value in request.form.items():
                new_vote = Votes(question_id=int(key), answer_id=int(value), user_id=int(user.id))
                db.session.add(new_vote)
                db.session.commit()

            flash('Formularz został wysłany. Dziękujemy za udział w ankiecie.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Formularz został już wypełniony.', 'danger')
            return redirect(url_for('home'))

    # mycursor.close()
    return render_template("index.html", questions=questions, answers=answer)


@app.route('/o-projekcie', methods=["GET"])
def about():
    return render_template("about.html")
