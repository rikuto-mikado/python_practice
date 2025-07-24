# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from owm import OpenWeatherClient
from config import Config
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = (
    Config.SECRET_KEY
)  # ← ここを揃える（config.py に追加しておくと◎）

client = OpenWeatherClient()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city") or Config.DEFAULT_CITY
        return redirect(url_for("weather", city=city))
    return render_template("index.html", default_city=Config.DEFAULT_CITY)


@app.route("/weather")
def weather():
    city = request.args.get("city", Config.DEFAULT_CITY)
    try:
        data = client.current_by_city(city)
    except Exception as e:
        flash(f"天気情報の取得に失敗しました: {e}", "error")
        return redirect(url_for("index"))

    icon_url = f"https://openweathermap.org/img/wn/{data['icon']}@2x.png"
    return render_template("weather.html", city=city, data=data, icon_url=icon_url)


if __name__ == "__main__":
    app.run(debug=True)
