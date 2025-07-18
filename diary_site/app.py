from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__, instance_relative_config=True)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    app.instance_path, "diary.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 10
    entries = Entry.query.order_by(Entry.date.desc()).paginate(
        page=page, per_page=per_page
    )
    return render_template("index.html", entries=entries)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        new_entry = Entry(title=title, content=content)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    entry = Entry.query.get_or_404(id)
    if request.method == "POST":
        entry.title = request.form["title"]
        entry.content = request.form["content"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", entry=entry)


@app.route("/delete/<int:id>")
def delete(id):
    entry = Entry.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
