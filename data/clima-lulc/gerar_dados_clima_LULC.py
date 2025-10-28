
import pandas as pd
import numpy as np
from pathlib import Path

# Configuração
output_path = Path("data/clima-lulc/clima_LULC_realista.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Geração de 50 amostras sintéticas para Angola
np.random.seed(42)
n = 50
latitudes = np.random.uniform(-18, -4, n)
longitudes = np.random.uniform(11, 24, n)

data = pd.DataFrame({
    "latitude": latitudes.round(4),
    "longitude": longitudes.round(4),
    "temperature_avg_c": np.random.uniform(18, 32, n).round(2),
    "precipitation_mm": np.random.uniform(500, 2000, n).round(1),
    "humidity_pct": np.random.uniform(40, 85, n).round(1),
    "wind_speed_mps": np.random.uniform(1, 6, n).round(2),
    "ndvi": np.random.uniform(0.2, 0.9, n).round(3),
    "elevation_m": np.random.uniform(50, 1800, n).round(1),
    "land_cover": np.random.choice(["Urban", "Forest", "Grassland", "Water Body", "Wetland"], n),
    "land_use": np.random.choice(["Agricultural", "Industrial", "Residential", "Protected Area", "Unused"], n)
})

data.to_csv(output_path, index=False)
print(f"✅ Dados climáticos e LU/LC gerados: {output_path}")
