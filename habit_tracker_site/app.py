import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timedelta

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "instance", "habits.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    completions = db.relationship(
        "Completion", backref="habit", cascade="all, delete-orphan"
    )


class Completion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    habit_id = db.Column(db.Integer, db.ForeignKey("habit.id"), nullable=False)


@app.route("/add_habit", methods=["POST"])
def add_habit():
    habit_name = request.form.get("habit_name")
    if habit_name:
        new_habit = Habit(name=habit_name)
        db.session.add(new_habit)
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/")
def index():
    habits = Habit.query.all()

    return render_template("index.html", habits=habits)


if __name__ == "__main__":
    app.run(debug=True)
