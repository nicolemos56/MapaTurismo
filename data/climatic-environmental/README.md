# Clima, Uso do Solo, Mobilidade e Infraestrutura

# Descrição Geral
Este conjunto de dados foi criado para fins de **prototipagem e treino de modelos de Machine Learning **, simulando informações reais obtidas de **fontes globais de dados abertos** sobre **clima, uso do solo, mobilidade e infraestrutura em Angola**.  

Os dados correspondem a **15 pontos turísticos de referência** (POIs) localizados em diversas províncias do país.  

# Estrutura dos Arquivos

# clima_lulc.csv
Contém informações sobre **clima** e **uso do solo (Land Use / Land Cover – LULC)**.  

| Coluna | Descrição |
|---------|------------|
| Nome | Nome do ponto turístico |
| Província | Província onde se localiza |
| Temp_Média_Anual_(°C) | Temperatura média anual (simulada com base em WorldClim / Copernicus) |
| Precipitação_Anual_(mm) | Média anual de precipitação |
| Tipo_Clima | Classificação climática geral (Tropical, Subtropical, Semiárido, etc.) |
| Uso_Solo_(LULC) | Tipo predominante de uso do solo (floresta, savana, urbana, etc.) |
| Cobertura_Vegetal_(%) | Percentual aproximado de cobertura vegetal |
| Altitude_(m) | Altitude média aproximada do local |
| Distância_Corpo_Água_(km) | Distância estimada até o corpo de água mais próximo |

**Fontes simuladas:**
- [WorldClim v2](https://www.worldclim.org/)
- [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/)
- [Sentinel-2 Land Use / Land Cover (LULC)](https://land.copernicus.eu/global/products/lc)

---

# mobilidade_infra.csv
Contém informações sobre **mobilidade**, **acessibilidade** e **infraestrutura** local.

| Coluna | Descrição |
|---------|------------|
| Nome | Nome do ponto turístico |
| Província | Província onde se localiza |
| Distância_Estrada_Principal_(km) | Distância estimada até a estrada principal mais próxima |
| Distância_Cidade_(km) | Distância até a cidade principal da província |
| Acessibilidade | Qualidade de acesso ao local (boa, média, difícil) |
| Tipo_Via_Acesso | Tipo de via (pavimentada, terra batida, trilho) |
| Infraestrutura | Nível geral de infraestrutura local |
| Serviços_Disponíveis | Serviços presentes (energia, telecom, hospedagem, etc.) |
| Densidade_Populacional_(hab/km²) | Densidade populacional aproximada na área |

**Fontes simuladas:**
- [Google Maps Platform APIs](https://developers.google.com/maps)
- [GeoNames Geographical Database](https://www.geonames.org/)
- [Copernicus Global Human Settlement Layer (GHSL)](https://ghsl.jrc.ec.europa.eu/)
