# Copernicus Land Cover (100m) – Ano 2020 (via Google Earth Engine)
import ee
import geemap
import os

# Autenticar (primeira vez)
ee.Authenticate()
ee.Initialize()

# Definir área de Angola
angola = ee.FeatureCollection("FAO/GAUL/2015/level0").filter(ee.Filter.eq('ADM0_NAME', 'Angola'))

# Land Cover Copernicus 2020
lc = ee.Image("COPERNICUS/Landcover/100m/Proba-V-C3/Global/2020") \
        .select('discrete_classification')

# Recortar e exportar
task = ee.batch.Export.image.toDrive(
    image=lc.clip(angola),
    description='Angola_LandCover_2020',
    folder='GEE_Angola',
    fileNamePrefix='angola_landcover_2020',
    scale=100,
    region=angola.geometry(),
    maxPixels=1e10
)

task.start()
print("Exportação iniciada no Google Earth Engine. Verifique em Google Drive > GEE_Angola")