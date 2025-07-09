from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = "quiz_secret_key"

# import from json
with open("quiz_app", encoding="utf-8") as f:
    quiz_list = json.load()


@app.route("/")
def index():
    session["current"] = 0
    session["score"] = 0
    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    current = session.get("current", 0)
    score = session.get("score", 0)

    if request.method == "POST":
        user_answer = request.form.get("answer") == "True"
        correct_answer = quiz_list[current]["answer"]
        if user_answer == correct_answer:
            session["score"] = score + 1
        session["current"] = current + 1
        return redirect(url_for("quiz"))

    if current >= len(quiz_list):
        return redirect(url_for("result"))

    question = quiz_list[current]["question"]
    return render_template("quiz.html", question=question)


@app.route("/result")
def result():
    score = session.get("score", 0)
    total = len(quiz_list)
    return render_template("result.html", score=score, total=total)


if __name__ == "__main__":
    app.run(debug=True)
