import requests
GEO_ENDPOINT = 'http://api.openweathermap.org/geo/1.0/direct'
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = '7a956fa249de7c4633a84a4eeccac274'


class API:
    def __init__(self, query):
        self.query = query

    def lat_lon(self):
        parameters_geo = {
            'q': self.query,
            'appid': API_KEY
        }
        response = requests.get(GEO_ENDPOINT, params=parameters_geo)
        data = response.json()[0]
        return data['lat'], data['lon']

    def weather_data(self):
        # Parameters for OpenWeatherMap API
        lat, lon = self.lat_lon()
        parameters = {
            "lat": lat,
            "lon": lon,
            "appid": API_KEY
        }
        # Get Weather Data
        response = requests.get(OWM_ENDPOINT, params=parameters)
        data = response.json()
        # Getting Weather Info
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp'] - 273
        humidity = data['main']['humidity']
        icon = data['weather'][0]['icon']
        wind_speed = data['wind']['speed']
        data = {
            'weather_desc': weather_desc,
            'temp': round(temp, 2),
            "humidity": humidity,
            'icon': icon,
            "wind_speed": wind_speed

        }
        return data
