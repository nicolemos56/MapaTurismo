
# Clima e Uso do Solo (LU/LC) + Mobilidade e Infraestrutura – Angola

Este diretório contém scripts para gerar **dados sintéticos e não reais**, simulando fontes como WorldClim, Copernicus, Sentinel (para Clima e LU/LC) e Google Maps API, Geonames (para Mobilidade e Infraestrutura).

## Estrutura dos Dados

- `clima_LULC_realista.csv` → Temperatura, precipitação, umidade, NDVI, cobertura e uso do solo.
- `mobilidade_infra_realista.csv` → Cidade, população, tipo de infraestrutura, densidade de transporte.
- `dados_integrados_geo.csv` → Fusão dos dois datasets via latitude/longitude.
- `gerar_dados_clima_LULC.py` → Script gerador do dataset climático e LU/LC.
- `gerar_dados_mobilidade_infra.py` → Script gerador do dataset de mobilidade.
- `etl_fusao_geo.py` → Script de integração (ETL).

## Como usar
```bash
python gerar_dados_clima_LULC.py
python gerar_dados_mobilidade_infra.py
python etl_fusao_geo.py
```

## Observação
Todos os dados são **artificiais** e não representam valores reais. São indicados apenas para fins de **teste e pesquisa**.
