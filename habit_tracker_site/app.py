import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timedelta, date
import calendar

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
    habits = Habit.query.order_by(Habit.id).all()
    today = date.today()
    year, month = today.year, today.month

    cal = calendar.monthcalendar(year, month)

    completions_by_habit = {}

    for habit in habits:

        completed_dates = (
            db.session.query(Completion.date)
            .filter(
                Completion.habit_id == habit.id,
                db.extract("year", Completion.date) == year,
                db.extract("month", Completion.date) == month,
            )
            .all()
        )

        completions_by_habit[habit.id] = {d[0].day for d in completed_dates}

    return render_template(
        "index.html",
        habits=habits,
        calendar_data=cal,
        year=year,
        month=month,
        month_name=calendar.month_name[month],
        weekdays=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        completions_by_habit=completions_by_habit,
    )


@app.route("/delete/<int:habit_id>", methods=["POST"])
def delete_habit(habit_id):

    habit_to_delete = Habit.query.get_or_404(habit_id)

    db.session.delete(habit_to_delete)

    db.session.commit()

    return redirect(url_for("index"))


@app.route("/toggle/<int:habit_id>/<int:year>/<int:month>/<int:day>", methods=["GET"])
def toggle_completion(habit_id, year, month, day):
    completion_date = date(year, month, day)

    completion = Completion.query.filter_by(
        habit_id=habit_id, date=completion_date
    ).first()

    if completion:
        db.session.delete(completion)
    else:
        new_completion = Completion(habit_id=habit_id, date=completion_date)
        db.session.add(new_completion)

    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
