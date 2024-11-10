import os
from dotenv import load_dotenv

import requests


def get_lat_lng_google(address, api_key):
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': address, 'key': api_key}
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data['results']:
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        print(f"Error: {data.get('error_message', 'No data found')}")
        return None, None


# keys.env/keys.env dosyasının yolunu belirtme
load_dotenv(dotenv_path=os.path.join('.venv', 'keys.env'))
api_key = os.getenv('GOOGLE_API_KEY')


address = "Çamlıca Mah. Ptt Lojmanları D Blok Daire 17 Demetevler Yenimahalle, ANKARA"
latitude, longitude = get_lat_lng_google(address, api_key)
print(f"Latitude: {latitude}, Longitude: {longitude}")
print(f"{latitude},{longitude}")

