import requests


def get_lat_lng(address):
    base_url = 'https://nominatim.openstreetmap.org/search'
    headers = {'User-Agent': 'MyGeocodingApp/1.0 (example@example.com)'}
    params = {'q': address, 'format': 'json'}
    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code != 200:
        print(f"Error: HTTP {response.status_code}")
        return None, None

    try:
        data = response.json()
    except ValueError:
        print("Error: JSON formatında bir yanıt alınamadı.")
        print("Yanıt içeriği:", response.text)
        return None, None

    if data:
        return data[0]['lat'], data[0]['lon']
    else:
        print("Geçerli bir konum bulunamadı.")
        return None, None


address = "Çamlıca Mah. Ptt Lojmanları D Blok Daire 17 Demetevler Yenimahalle, ANKARA"
latitude, longitude = get_lat_lng(address)
print(f"Latitude: {latitude}, Longitude: {longitude}")
print(f"{latitude}, {longitude}")
