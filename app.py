from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="djangodb"
)

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

    return render_template("form.html", questions=questions, answers=answer)


if __name__ == '__main__':
    app.run()
