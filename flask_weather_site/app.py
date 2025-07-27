# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from owm import OpenWeatherClient
from config import Config

app = Flask(__name__)
app.config["SECRET_KEY"] = Config.SECRET_KEY

client = OpenWeatherClient()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = (request.form.get("city") or "").strip() or Config.DEFAULT_CITY
        action = request.form.get("action", "current")
        session["last_city"] = city
        if action == "forecast":
            return redirect(url_for("forecast", city=city))
        return redirect(url_for("weather", city=city))

    initial = request.args.get("city") or session.get("last_city") or ""
    return render_template("index.html", initial_city=initial)


@app.route("/weather")
def weather():
    city = request.args.get("city") or session.get("last_city") or Config.DEFAULT_CITY
    try:
        data = client.current_by_city(city)
    except Exception as e:
        flash(f"天気情報の取得に失敗しました: {e}", "error")
        return redirect(url_for("index"))

    session["last_city"] = data.get("name", city)

    icon_url = f"https://openweathermap.org/img/wn/{data['icon']}@2x.png"
    return render_template("weather.html", city=city, data=data, icon_url=icon_url)


@app.route("/forecast")
def forecast():
    city = request.args.get("city") or session.get("last_city") or Config.DEFAULT_CITY
    try:
        data = client.forecast_by_city(city)
    except Exception as e:
        flash(f"予報の取得に失敗しました: {e}", "error")
        return redirect(url_for("index"))

    session["last_city"] = data.get("city", city)

    return render_template("forecast.html", city=city, data=data)


if __name__ == "__main__":
    app.run(debug=True)
