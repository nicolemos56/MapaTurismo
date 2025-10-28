
import pandas as pd
import numpy as np
from pathlib import Path

# Configuração
output_path = Path("data/clima-lulc/mobilidade_infra_realista.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Geração de 50 amostras sintéticas
np.random.seed(43)
n = 50
latitudes = np.random.uniform(-18, -4, n)
longitudes = np.random.uniform(11, 24, n)
cidades = np.random.choice(["Luanda", "Benguela", "Huambo", "Lubango", "Namibe", "Soyo", "Malanje"], n)

data = pd.DataFrame({
    "city": cidades,
    "latitude": latitudes.round(4),
    "longitude": longitudes.round(4),
    "population": np.random.randint(10000, 100000, n),
    "infrastructure_type": np.random.choice(["Airport", "Hospital", "Bus Station", "Primary Road", "Port"], n),
    "transport_density": np.random.uniform(0.1, 1.0, n).round(2)
})

data.to_csv(output_path, index=False)
print(f"✅ Dados de mobilidade e infraestrutura gerados: {output_path}")
