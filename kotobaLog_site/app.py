import json
from flask import Flask, render_template
import random
import random

app = Flask(__name__)

with open("quotes.json", encoding="utf-8") as f:
    quotes = json.load(f)


@app.route("/")
def index():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)


if __name__ == "__main__":
    app.run(debug=True)
