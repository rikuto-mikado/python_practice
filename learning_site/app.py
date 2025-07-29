from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta, date
from models import db, StudyLog

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
                date=datetime.fromisoformat(d).date(),
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
    # ← ここで今日の日付を渡す
    return render_template("index.html", recent=recent, today=date.today().isoformat())


@app.route("/api/stats")
def api_stats():
    rng = request.args.get("range", "week")
    today = date.today()
    if rng == "month":
        start = today.replace(day=1)
    else:
        start = today - timedelta(days=today.weekday())
    end = today

    days = [(start + timedelta(days=i)) for i in range((end - start).days + 1)]
    series = {d.isoformat(): 0 for d in days}

    q = StudyLog.query.filter(StudyLog.date >= start, StudyLog.date <= end).all()
    for row in q:
        k = row.date.isoformat()
        series[k] = series.get(k, 0) + row.minutes

    labels = list(series.keys())
    values = [series[k] for k in labels]
    total = sum(values)
    return jsonify({"labels": labels, "values": values, "total": total})
