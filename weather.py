import os
import datetime as dt
import requests
import sys
from pprint import pprint

CITY = "Glasgow"
API_KEY = os.environ.get("WEATHER_API_KEY")


# get coordinates of city
def get_coordinates():
    geocoding_url = (
        f"http://api.openweathermap.org/geo/1.0/direct?q={CITY}&appid={API_KEY}"
    )

    try:
        response = requests.get(geocoding_url)
        response.raise_for_status()
        response_body = response.json()[0]

        lat, lon = response_body["lat"], response_body["lon"]

        return lat, lon

    except requests.exceptions.HTTPError as error:
        sys.exit(f"An error occurred getting coords: {error}")


def get_current_forecast(lat, lon):
    current_weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=daily,minutely,hourly&appid={API_KEY}&units=metric"

    try:
        response = requests.get(current_weather_url)
        response.raise_for_status()
        response_body = response.json()

        sunrise = dt.datetime.fromtimestamp(
            response_body["timezone_offset"] + response_body["current"]["sunrise"],
            tz=dt.timezone.utc,
        ).strftime("%H:%M")
        sunset = dt.datetime.fromtimestamp(
            response_body["timezone_offset"] + response_body["current"]["sunset"],
            tz=dt.timezone.utc,
        ).strftime("%H:%M")

        response_body["current"]["sunrise"] = sunrise
        response_body["current"]["sunset"] = sunset

        return response_body["current"]

    except requests.exceptions.HTTPError as error:
        sys.exit(f"An error occurred getting forecast: {error}")


def get_ai_weather_summary(today, lat, lon):
    weather_summary_url = f"https://api.openweathermap.org/data/3.0/onecall/overview?lat={lat}&lon={lon}&date={today}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(weather_summary_url)
        response.raise_for_status()
        response_body = response.json()

        return response_body["weather_overview"]

    except requests.exceptions.HTTPError as error:
        sys.exit(f"An error occurred getting weather summary: {error}")


# returns current forecast and weather summary
def get_todays_weather():
    today = dt.datetime.today().strftime("%Y-%m-%d")
    lat, lon = get_coordinates()

    current_forecast = get_current_forecast(lat, lon)
    weather_summary = get_ai_weather_summary(today, lat, lon)

    todays_weather = {
        "description": current_forecast["weather"][0]["description"].capitalize(),
        "temp": f"Currently {current_forecast['temp']}C",
        "feels_like": f"Feels like {current_forecast['feels_like']}C",
        "sunrise": f"Sunrise at {current_forecast['sunrise']}AM",
        "sunset": f"Sunset at {current_forecast['sunset']}PM",
        "humidity": f"{current_forecast['humidity']}% humidity",
        "wind_speed": f"{current_forecast['wind_speed']}mph wind speed",
        "summary": weather_summary,
    }

    return todays_weather


if __name__ == "__main__":
    print(f"Coordinates of {CITY}: {get_coordinates()}")
    print("Today's weather: ")
    pprint(get_todays_weather())
