from flask import Flask, render_template, request, redirect, url_for
from models import db, Habit
from datetime import date

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///habits.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


# reset
with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            new_habit = Habit(name=name, created_date=date.today())
            db.session.add(new_habit)
            db.session.commit()
        return redirect(url_for("index"))

    habits = Habit.query.all()
    return render_template("index.html", habits=habits, today=date.today())


if __name__ == "__main__":
    app.run(debug=True)
