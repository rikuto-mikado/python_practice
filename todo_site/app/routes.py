from flask import Blueprint, render_template, request, redirect, url_for
from .models import TodoModel

main = Blueprint("main", __name__)
todo_model = TodoModel()


@main.route("/")
def index():
    todos = todo_model.get_all()
    return render_template("index.html", todos=todos)


@main.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    todo_model.add(task)
    return redirect(url_for("main.index"))


@main.route("/delete/<int:index>")
def delete(index):
    todo_model.delete(index)
    return redirect(url_for("main.index"))
