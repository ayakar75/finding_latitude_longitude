def get_lat_lng(address):
    base_url = 'https://nominatim.openstreetmap.org/search'
    params = {'q': address, 'format': 'json'}
    response = requests.get(base_url, params=params)

    # Yanıtın durum kodunu kontrol et
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

address = "Büyükşehir Mahallesi Çamlık Caddesi A-33 Blok Daire:52 Kat 12 Beylikdüzü İSTANBUL Turkey"
latitude, longitude = get_lat_lng(address)
print(f"Latitude: {latitude}, Longitude: {longitude}")
