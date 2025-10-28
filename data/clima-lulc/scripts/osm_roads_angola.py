# OpenStreetMap – Estradas de Angola (via HDX)
import wget
import zipfile

url = "https://data.humdata.org/dataset/1d3f0a7a-4e1a-4e1a-8e1a-4e1a4e1a4e1a/resource/8f0d8f0d-8f0d-8f0d-8f0d-8f0d8f0d8f0d/download/hotosm_ago_roads_shp.zip"
filename = "angola_roads.zip"

print("Baixando estradas OSM (Angola)...")
wget.download(url, filename)

print("\nExtraindo...")
with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall("osm_roads_angola")

print("Concluído! Shapefiles em: osm_roads_angola/")