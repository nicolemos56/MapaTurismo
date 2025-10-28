# GeoNames – Download de todos os pontos de Angola
import requests
import zipfile
import os

url = "https://download.geonames.org/export/dump/AO.zip"
filename = "AO.zip"

print("Baixando GeoNames Angola...")
r = requests.get(url, stream=True)
with open(filename, 'wb') as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)

print("Extraindo...")
with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall("geonames_angola")

os.remove(filename)
print("Concluído! Arquivos em: geonames_angola/AO.txt")