
import pandas as pd
from pathlib import Path

raw_path = Path("data/clima-lulc")
output_path = raw_path / "dados_integrados_geo.csv"

# Carregar dados
clima = pd.read_csv(raw_path / "clima_LULC_realista.csv")
infra = pd.read_csv(raw_path / "mobilidade_infra_realista.csv")

# Fusão baseada em proximidade geográfica (latitude)
dados_fusao = pd.merge_asof(
    clima.sort_values("latitude"),
    infra.sort_values("latitude"),
    on="latitude",
    direction="nearest",
    tolerance=0.05
)

dados_fusao.to_csv(output_path, index=False)
print(f"✅ Dados integrados salvos em: {output_path}")
