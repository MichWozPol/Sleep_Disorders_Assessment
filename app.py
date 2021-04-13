import datetime
import mysql.connector
from flask import Flask, request, render_template, url_for, flash, redirect
from flask_bootstrap import Bootstrap


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
    return "<h1>About our project</h1>"

@app.route('/badania', methods=["GET"])
def research():
    return "<h1>Research page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
    home()
