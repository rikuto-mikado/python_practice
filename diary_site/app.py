from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///diary.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# definition of model
class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


# home page
@app.route("/")
def index():
    entries = Diary.query.order_by(Diary.date.desc()).all()
    return render_template("index.html", entries=entries)


# create page
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        new_entry = Diary(title=title, content=content)
        db.session.add(new_entry)
        db.session.commit()
        return redirect("/")
    return render_template("create.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    entry = Diary.query.get_or_404(id)
    if request.method == "POST":
        entry.title = request.form["title"]
        entry.content = request.form["content"]
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", entry=entry)


@app.route("/delete/<int:id>")
def delete(id):
    entry = Diary.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
