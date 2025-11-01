# README - model_training.ipynb

## Objetivo
O notebook `model_training.ipynb` implementa um pipeline completo de modelagem preditiva para análise do potencial turístico em Angola, utilizando dados socioeconômicos, ambientais e geoespaciais.

## Etapas do Notebook

1. **Importação de Bibliotecas**
   - Importa as principais bibliotecas de ciência de dados, machine learning, deep learning e análise espacial (pandas, scikit-learn, xgboost, torch, geopandas, etc).

2. **Carregamento e Exploração dos Dados**
   - Carrega os dados preparados do arquivo `data/model_inputs/model_input.csv`.
   - Exibe as colunas e as primeiras linhas para inspeção.

3. **Definição de Variáveis**
   - Seleciona automaticamente as colunas numéricas como features.
   - Cria uma variável alvo binária baseada na média dos indicadores.
   - Realiza split espacial dos dados para garantir validação cruzada robusta.

4. **Treinamento de Modelos**
   - Treina três abordagens:
     - Random Forest (scikit-learn)
     - XGBoost (xgboost)
     - Rede Neural (PyTorch)
   - Todos os modelos são treinados e avaliados com os mesmos dados.

5. **Avaliação e Interpretação**
   - Analisa a importância das variáveis (feature importance do Random Forest).
   - Exibe métricas de desempenho: classification report, AUC-ROC, acurácia da rede neural.
   - Visualiza as variáveis mais relevantes para a predição.

6. **Salvamento do Modelo**
   - O modelo XGBoost treinado é salvo em `models/tourism_model.pkl` para uso futuro.

## Resultados
- O pipeline permite identificar os principais fatores que influenciam o potencial turístico.
- O modelo pode ser utilizado para prever o potencial de novas localidades e apoiar políticas públicas.

## Observações
- O notebook está preparado para ser expandido com análises espaciais (PySAL) e previsão temporal (redes neurais) conforme disponibilidade de dados.
- O split espacial por províncias/municípios reduz o risco de overfitting e aumenta a robustez da avaliação.

## Como Executar
1. Instale as dependências listadas em `requirements.txt`.
2. Execute as células do notebook sequencialmente.
3. O modelo final será salvo em `models/tourism_model.pkl`.

---
