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


api_key = ''
address = "HOŞNİDİYE, SAĞIN SK. NO:32, TEPEBAŞI, ESKİŞEHİR/TURKEY"
latitude, longitude = get_lat_lng_google(address, api_key)
print(f"Latitude: {latitude}, Longitude: {longitude}")
