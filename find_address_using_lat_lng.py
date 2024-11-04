import requests
import os
from dotenv import load_dotenv
def reverse_geocode_google(lat, lng, api_key):
    """
    Google Maps Geocoding API kullanarak verilen enlem ve boylam değerlerinden adres elde eder.

    :param lat: Enlem
    :param lng: Boylam
    :param api_key: Google Maps API anahtarı
    :return: Adres (string)
    """
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'latlng': f'{lat},{lng}',
        'key': api_key
    }

    try:
        response = requests.get(base_url, params=params)

        # HTTP yanıt durum kodunu kontrol et
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                return data['results'][0]['formatted_address']
            else:
                return "Adres bulunamadı."
        else:
            return f"Hata: {response.status_code}"
    except Exception as e:
        return f"İstek sırasında bir hata oluştu: {e}"


# Örnek kullanım
latitude = 40.19475555                    #39.9334  # Ankara'nın enlemi
longitude =29.05800438                              #32.8597  # Ankara'nın boylamı
# keys.env/keys.env dosyasının yolunu belirtme
load_dotenv(dotenv_path=os.path.join('.venv', 'keys.env'))
api_key = os.getenv('GOOGLE_API_KEY')

adres = reverse_geocode_google(latitude, longitude, api_key)
print(f"Bulunan Adres: {adres}")
