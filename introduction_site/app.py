from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("pages/home.html", title="ホーム")


@app.route("/about")
def about():
    return render_template("pages/about.html", title="About Us")


@app.route("/contact")
def contact():
    return render_template("pages/contact.html", title="Contact Us")


if __name__ == "__main__":
    app.run(debug=True)
