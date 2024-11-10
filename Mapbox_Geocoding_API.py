import requests
import os
from dotenv import load_dotenv


def get_lat_lng_mapbox(address, api_key):
    base_url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json'
    params = {
        'access_token': api_key,
        'limit': 1,
        'language': 'tr'  # Set the language to Turkish
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data['features']:
        location = data['features'][0]['center']
        return location[1], location[0]  # Latitude, Longitude
    else:
        print("Geçerli bir konum bulunamadı.")
        return None, None


load_dotenv(dotenv_path=os.path.join('.venv', 'keys.env'))
api_key = os.getenv('MAPBOX_TOKEN')

address = "Çamlıca Mah. Ptt Lojmanları Demetever Yenimahalle, ANKARA"
latitude, longitude = get_lat_lng_mapbox(address, api_key)
print(f"Latitude: {latitude}, Longitude: {longitude}")
print(f"{latitude},{longitude}")
