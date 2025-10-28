#Sentinel-2 – Imagem Recente de Luanda (exemplo)
import ee
ee.Authenticate()
ee.Initialize()

# Área de Luanda
luanda = ee.Geometry.Rectangle([13.15, -8.9, 13.35, -8.75])

# Coleção Sentinel-2 (nuvens < 20%)
s2 = ee.ImageCollection('COPERNICUS/S2_SR') \
       .filterBounds(luanda) \
       .filterDate('2025-01-01', '2025-10-27') \
       .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)) \
       .sort('CLOUDY_PIXEL_PERCENTAGE') \
       .first()

# Exportar
task = ee.batch.Export.image.toDrive(
    image=s2.select(['B4', 'B3', 'B2']),
    description='Luanda_Sentinel2_2025',
    folder='GEE_Angola',
    fileNamePrefix='luanda_s2_2025',
    scale=10,
    region=luanda,
    maxPixels=1e9
)
task.start()
print("Exportando imagem Sentinel-2 de Luanda...")