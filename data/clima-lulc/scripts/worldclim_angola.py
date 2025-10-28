# WorldClim – Precipitação e Temperatura (1 km)worldclim_angola.py
import requests
from osgeo import gdal
import os

# Definir bounding box de Angola (aproximado)
minx, miny, maxx, maxy = 11.5, -18.5, 24.5, -4.5

# Variáveis: tmean (temperatura média), prec (precipitação)
vars = ['tmean', 'prec']
res = '30s'  # ~1 km

for var in vars:
    url = f"https://biogeo.ucdavis.edu/data/worldclim/v2.1/base/wc2.1_{res}_{var}.zip"
    zipfile = f"wc2.1_{res}_{var}.zip"
    
    print(f"Baixando {var}...")
    os.system(f"wget -q {url} -O {zipfile}")
    
    print(f"Extraindo e recortando {var} para Angola...")
    os.system(f"unzip -o {zipfile}")
    
    # Recortar com GDAL (exemplo para um mês, repita para todos)
    tif_files = [f for f in os.listdir('.') if f.endswith('.tif') and var in f]
    for tif in tif_files:
        out_tif = f"angola_{tif}"
        os.system(f"gdal_translate -projwin {minx} {maxy} {maxx} {miny} {tif} {out_tif}")
        print(f"  -> {out_tif}")

    # Limpar
    os.system(f"rm {zipfile} *.tif")
print("WorldClim concluído! Arquivos recortados para Angola.")