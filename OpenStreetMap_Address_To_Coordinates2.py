import requests

def get_lat_lng_optimized(street, district, city, country):
    base_url = 'https://nominatim.openstreetmap.org/search'
    headers = {'User-Agent': 'MyGeocodingApp/1.0 (example@example.com)'}
    full_address = f"{district}, {street}, {city}, {country}"
    params = {'q': full_address, 'format': 'json'}
    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code != 200:
        print(f"Error: HTTP {response.status_code}")
        return None, None

    try:
        data = response.json()
    except ValueError:
        print("Error: JSON formatında bir yanıt alınamadı.")
        return None, None

    if data:
        return data[0]['lat'], data[0]['lon']
    else:
        print("Geçerli bir konum bulunamadı.")
        return None, None

street = "SAĞIN SK. No: 32"
district = "HOŞNİDİYE Mahallesi"
city = "TEPEBAŞI, ESKİŞEHİR"
country = "Turkey"

latitude, longitude = get_lat_lng_optimized(street, district, city, country)
print(f"Latitude: {latitude}, Longitude: {longitude}")
