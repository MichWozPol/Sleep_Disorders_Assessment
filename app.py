import mysql.connector
from flask import Flask, request, render_template, url_for, flash, redirect
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sleep_disorders"
)

app = Flask(__name__)
app.config['SECRET_KEY'] = '5c357453c419ecbb80cd6603f35967f4'
Bootstrap(app)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    mycursor = mydatabase.cursor()
    mycursor.execute("SELECT * FROM question")
    questions = mycursor.fetchall()
    mycursor.execute("SELECT * FROM answer")
    answer = mycursor.fetchall()

    if request.method == "POST":
        print(request.form)
        for key, value in request.form.items():
            sql = "INSERT INTO vote (question_id, answer_id, user_id) VALUES (%s, %s, %s)"
            val = (int(key), int(value), 1)
            mycursor.execute(sql, val)
            mydatabase.commit()

        flash(f'Formularz został wysłany. Dziękujemy za udział w ankiecie.', 'success')
        return redirect(url_for('hello_world'))

    return render_template("index.html", questions=questions, answers=answer)


@app.route('/o-projekcie', methods=["GET"])
def about_page():
    return "<h1>About our project</h1>"

@app.route('/badania', methods=["GET"])
def research():
    return "<h1>Research page</h1>"


if __name__ == '__main__':   
    app.run()
    hello_world()
