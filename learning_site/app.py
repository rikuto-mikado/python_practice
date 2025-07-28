from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta, date
from models import db, StudyLog
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///study.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        d = request.form.get("date") or date.today().isoformat()
        minutes = int(request.form.get("minutes", 0))
        subject = (request.form.get("subject") or "General").strip() or "General"
        note = request.form.get("note") or ""
        db.session.add(
            StudyLog(
                date=datetime.fromisoformat(d),
                minutes=minutes,
                subject=subject,
                note=note,
            )
        )
        db.session.commit()
        return redirect(url_for("index"))

    recent = (
        StudyLog.query.order_by(StudyLog.date.desc(), StudyLog.id.desc())
        .limit(10)
        .all()
    )
    return render_template("index.html", recent=recent)


# chart.js
