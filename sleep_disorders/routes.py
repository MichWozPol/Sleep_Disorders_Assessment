import datetime
from sleep_disorders.__init__ import mydatabase
from flask import request, flash, redirect, render_template, url_for
from sleep_disorders import app

@app.route('/', methods=["GET", "POST"])
def home():
    mycursor = mydatabase.cursor()
    mycursor.execute("SELECT * FROM question")
    questions = mycursor.fetchall()
    mycursor.execute("SELECT * FROM answer")
    answer = mycursor.fetchall()
    mycursor.execute("SELECT ip FROM user")
    ip = mycursor.fetchall()


    if request.method == "POST":

        print(request.form)
        ip_address = request.remote_addr

        if ip_address not in (item[0] for item in ip):
            date = datetime.datetime.now()
            value = (date, ip_address)
            print(f"data {date} ip: {ip_address}")
            req = "INSERT INTO user (created_at, ip) VALUES (%s, %s)"
            mycursor.execute(req, value)
            mydatabase.commit()
            sql = f"SELECT id FROM user WHERE ip = '{ip_address}' "
            mycursor.execute(sql)
            user_id = mycursor.fetchall()
            print(int(user_id[-1][0]))

            for key, value in request.form.items():
                sql = "INSERT INTO vote (question_id, answer_id, user_id) VALUES (%s, %s, %s)"
                val = (int(key), int(value), int(user_id[-1][0]))
                mycursor.execute(sql, val)
                mydatabase.commit()

            flash('Formularz został wysłany. Dziękujemy za udział w ankiecie.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Formularz został już wypełniony', 'danger')
            return redirect(url_for('home'))

    return render_template("index.html", questions=questions, answers=answer)


@app.route('/o-projekcie', methods=["GET"])
def about():
    return render_template("about.html")

@app.route('/badania', methods=["GET"])
def research():
    return "<h1>Research page</h1>"