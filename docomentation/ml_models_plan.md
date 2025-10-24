# Plano Experimental do Modelo 
Caso de Uso	Modelo	Input	Output	Métrica	Validação
Potencial Turístico	Random Forest	Acessibilidade, Infraestrutura, Biodiversidade	Classe (Baixo/Médio/Alto)	Accuracy, AUC	Cross-Validation Espacial
Crescimento de Visitantes	LSTM	Série temporal de visitas	Nº Visitantes Futuros	RMSE, MAE	Train/Test Split temporal
Risco Ambiental	Regressão Espacial	LULC, Densidade Populacional	Índice de Risco	R²	Moran’s I / Spatial CV

# Nota:“Serão usados dados reais quando disponíveis e dados sintéticos simulados para calibração inicial.”