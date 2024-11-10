import pandas as pd
import requests
import os
from dotenv import load_dotenv

def get_coordinates_google(address, api_key):
    """
    Google Maps Geocoding API kullanarak verilen adresin koordinatlarını elde eder.

    :param address: Adres (string)
    :param api_key: Google Maps API anahtarı
    :return: (enlem, boylam) tuple
    """
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': address,
        'key': api_key
    }

    try:
        response = requests.get(base_url, params=params)

        # HTTP yanıt durum kodunu kontrol et
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                location = data['results'][0]['geometry']['location']
                return location['lat'], location['lng']
            else:
                return None, None
        else:
            print(f"Hata: {response.status_code}")
            return None, None
    except Exception as e:
        print(f"İstek sırasında bir hata oluştu: {e}")
        return None, None

# Örnek kullanım için dosyaları yükle
ilceler_path = './data/ilceler.csv'  # İlçelerin bulunduğu dosyanın yolu
iller_path = './data/iller.csv'  # İllerin bulunduğu dosyanın yolu

# Dosyaları oku
ilceler_df = pd.read_csv(ilceler_path, encoding='ISO-8859-9', sep=';', names=['ID', 'Ilce', 'IlID'])
iller_df = pd.read_csv(iller_path, encoding='ISO-8859-9', sep=';', names=['ID', 'Il'])

# İl ve ilçe bilgilerini birleştir
merged_df = pd.merge(ilceler_df, iller_df, left_on='IlID', right_on='ID', suffixes=('_district', '_city'))
districts_with_cities = merged_df[['Il', 'Ilce']].drop_duplicates()

# Google API anahtarını yükle
load_dotenv(dotenv_path=os.path.join('.venv', 'keys.env'))
api_key = os.getenv('GOOGLE_API_KEY')

# Her bir ilçe için koordinatları al ve tabloya ekle
districts_with_cities['Latitude'] = None
districts_with_cities['Longitude'] = None

for index, row in districts_with_cities.iterrows():
    address = f"{row['Ilce']}, {row['Il']}, Turkey"
    lat, lon = get_coordinates_google(address, api_key)
    districts_with_cities.at[index, 'Latitude'] = lat
    districts_with_cities.at[index, 'Longitude'] = lon

# Sonucu göster
print(districts_with_cities)

# Sonucu CSV dosyasına kaydet
districts_with_cities.to_csv('./data/districts_with_coordinates.csv', index=False, encoding='utf-8')
