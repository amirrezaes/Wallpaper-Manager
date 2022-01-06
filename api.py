from geocoder import api
from geocoder.api import get
import requests
import datetime
import geocoder


class Time:
    '''
    Uses system time to determine day part
    '''
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return 'time'

    @staticmethod
    def day_part() -> str:
        # https://gist.github.com/rbw/cd9ce89398a08e2f6b2acab14e3c58d7
        h = datetime.datetime.now().hour
        return (
        "morning"
        if 6 <= h <= 12
        else "afternoon"
        if 12 <= h <= 17
        else "evening"
        if 18 <= h <= 20
        else "night"
        )

    @staticmethod
    def get_update() -> str:
        return Time.day_part()


class Weather:
    '''
    Using https://open-meteo.com/ as api
    '''
    WEATHERCODES = {(0,): "sunny",
                    (1, 2, 3, 45, 48): "cloudy",
                    (51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82): "rainy",
                    (71, 73, 75, 77, 85, 86): "snowy"}

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return 'weather'

    @staticmethod
    def get_geo():
        g = geocoder.ip('me')
        return g.latlng

    def weather_condition() -> int:
        latitude, longitude = Weather.get_geo()
        api_request = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
        code = int(api_request.json()["current_weather"]["weathercode"])
        for lst in Weather.WEATHERCODES:
            if code in lst:
                return Weather.WEATHERCODES[lst]
    

    def get_update() -> str:
        return Weather.weather_condition()