import datetime
from flask import request, flash, redirect, render_template, url_for
from sleep_disorders import app
from sleep_disorders import db
from sleep_disorders.models.models import Question, Answer, User, Vote


@app.route('/', methods=["GET", "POST"])
def home():
    questions = db.session.query(Question.Questions).all()
    answer = db.session.query(Answer.Answers).all()
    user = db.session.query(User.Users).all()

    if request.method == "POST":
        ip_address = request.headers['X-Real-IP']
        #ip_address = request.remote_addr  #one should uncomment that line on the local host

        if ip_address not in (item.ip for item in user):
            date = datetime.datetime.now()
            new_user = User.Users(created_at=date, ip=ip_address)
            db.session.add(new_user)
            db.session.commit()
            user = db.session.query(User.Users).filter(User.Users.ip == ip_address).first()

            for key, value in request.form.items(multi=True):
                new_vote = Vote.Votes(question_id=int(key), answer_id=int(value), user_id=int(user.id))
                db.session.add(new_vote)
                db.session.commit()

            flash('Formularz został wysłany. Dziękujemy za udział w ankiecie.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Formularz został już wypełniony.', 'danger')
            return redirect(url_for('home'))

    return render_template("index.html", questions=questions, answers=answer)

@app.route('/o-projekcie', methods=["GET"])
def about():
    return render_template("about.html")

@app.route('/wyniki', methods=["GET"])
def results():
    return render_template("results.html")
