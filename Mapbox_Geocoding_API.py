import requests

def get_lat_lng_mapbox(address, api_key):
    base_url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json'
    params = {'access_token': api_key}
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data['features']:
        location = data['features'][0]['center']
        return location[1], location[0]  # Latitude, Longitude
    else:
        print("Geçerli bir konum bulunamadı.")
        return None, None

api_key = "YOUR_MAPBOX_API_KEY"
address = "HOŞNİDİYE, SAĞIN SK. NO:32, TEPEBAŞI, ESKİŞEHİR/TURKEY"
latitude, longitude = get_lat_lng_mapbox(address, api_key)
print(f"Latitude: {latitude}, Longitude: {longitude}")
