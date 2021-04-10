import mysql.connector
from flask import Flask, request, render_template, url_for
from flask_bootstrap import Bootstrap


mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sleep_disorders"
)

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    mycursor = mydatabase.cursor()

    if request.method == "POST":
        print(request.form)
        for key, value in request.form.items():
            sql = "INSERT INTO vote (question_id, answer_id, user_id) VALUES (%s, %s, %s)"
            val = (int(key), int(value), 1)
            mycursor.execute(sql, val)

            mydatabase.commit()

        return "DZIEKUJE"

    mycursor.execute("SELECT * FROM question")
    questions = mycursor.fetchall()
    mycursor.execute("SELECT * FROM answer")
    answer = mycursor.fetchall()

    return render_template("index.html", questions=questions, answers=answer)


@app.route('/about', methods=["GET"])
def about_page():
    return "<h1>Gracias mi amigo</h1>"


if __name__ == '__main__':   
    app.run()
    hello_world()
