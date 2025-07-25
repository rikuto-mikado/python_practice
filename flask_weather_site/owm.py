# owm.py
import requests
from typing import Optional, Dict, Any
from config import Config
from collections import defaultdict  # 外に出しておいてOK


class OpenWeatherClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        default_city: Optional[str] = None,
    ):
        self.api_key = api_key or Config.OWM_API_KEY
        if not self.api_key:
            raise RuntimeError("OWM_API_KEY is missing. Put it in your .env.")
        self.base_url = base_url or Config.OWM_BASE_URL
        self.default_city = default_city or Config.DEFAULT_CITY

    def _get(self, path: str, **params) -> Dict[str, Any]:
        p = {
            "appid": self.api_key,
            "units": "metric",
            "lang": "ja",
            **params,
        }
        r = requests.get(f"{self.base_url}/{path}", params=p, timeout=10)
        r.raise_for_status()
        return r.json()

    def current_by_city(self, city: Optional[str] = None) -> Dict[str, Any]:
        city = city or self.default_city
        raw = self._get("weather", q=city)
        return self._normalize_current(raw)

    def _normalize_current(self, data: Dict[str, Any]) -> Dict[str, Any]:
        weather = data["weather"][0]
        main = data["main"]
        wind = data.get("wind", {})
        return {
            "name": data.get("name"),
            "temp": round(main["temp"]),
            "feels_like": round(main["feels_like"]),
            "humidity": main["humidity"],
            "pressure": main["pressure"],
            "description": weather["description"],
            "icon": weather["icon"],
            "wind_speed": wind.get("speed"),
            "dt": data.get("dt"),
        }

    def forecast_by_city(self, city: Optional[str] = None) -> Dict[str, Any]:
        city = city or self.default_city
        raw = self._get("forecast", q=city)
        return self._normalize_forecast(raw)

    def _normalize_forecast(self, data: Dict[str, Any]) -> Dict[str, Any]:
        days = defaultdict(list)
        for item in data["list"]:
            date = item["dt_txt"].split(" ")[0]  # YYYY-MM-DD
            days[date].append(item)

        daily = []
        for date, items in days.items():
            temps = [x["main"]["temp"] for x in items]
            icons = [x["weather"][0]["icon"] for x in items]
            descs = [x["weather"][0]["description"] for x in items]
            daily.append(
                {
                    "date": date,
                    "temp_min": round(min(temps)),
                    "temp_max": round(max(temps)),
                    "icon": icons[len(icons) // 2],
                    "desc": descs[len(descs) // 2],
                }
            )

        return {
            "city": data["city"]["name"],
            "daily": daily[:5],
        }
