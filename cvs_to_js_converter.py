import pandas as pd
import json

# CSV dosyasını oku
file_path = './data/districts_with_coordinates.csv'  # CSV dosyasının yolu
districts_df = pd.read_csv(file_path, encoding='utf-8')

# GeoJSON formatında JS dosyasını oluştur
geojson_features = []
for _, row in districts_df.iterrows():
    if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']):
        feature = {
            "type": "Feature",
            "properties": {
                "city": row['Il'],
                "district": row['Ilce']
            },
            "geometry": {
                "type": "Point",
                "coordinates": [row['Longitude'], row['Latitude']]
            }
        }
        geojson_features.append(feature)

geojson_data = {
    "type": "FeatureCollection",
    "features": geojson_features
}

# JSON verisini JS formatına dönüştür ve kaydet
output_js_path = './data/districts_data.js'  # Çıktı dosyasının yolu
with open(output_js_path, 'w', encoding='utf-8') as js_file:
    js_file.write('var data = ' + json.dumps(geojson_data, ensure_ascii=False, indent=4) + ';')

print(f"JS dosyası '{output_js_path}' olarak kaydedildi.")
