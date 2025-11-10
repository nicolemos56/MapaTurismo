# README - model_training.ipynb

# Objetivo Principal
   O objetivo deste notebook é criar e validar um modelo base (baseline) funcional de Machine Learning. Este modelo serve como o nosso ponto de partida para prever o potencial de desenvolvimento turístico de localidades em Angola, utilizando o Índice de Desenvolvimento Humano (IDH) como métrica alvo.
   O foco aqui é construir uma metodologia robusta e correta, e não alcançar a perfeição preditiva imediatamente.

# Abordagem Metodológica e Justificativa
   A nossa abordagem foi escolhida por ser a mais alinhada com as melhores práticas de ciência de dados, garantindo relevância, robustez e honestidade.
   1. Tipo de Problema: Regressão em Dados Tabulares

      # O quê: Prever um valor numérico contínuo (IDH).
      # Porquê: Escolhemos a Regressão porque queremos prever o valor do IDH, uma métrica real e com significado. Nossos dados são dados tabulares estruturados (ou cross-sectional), onde cada linha é um "retrato" independente de um ponto turístico. A ordem das linhas não importa, e este é o cenário clássico para modelos de regressão.
   2. Escolha da Ferramenta: ML Clássico para Dados Estruturados

      # O quê: Optamos por um modelo de Machine Learning Clássico (RandomForestRegressor) em vez de abordagens de Deep Learning como Redes Neurais ou LSTMs.
      # Porquê: Esta foi uma decisão estratégica baseada no tipo de dados que possuímos:

   Dados Estruturados vs. Não Estruturados: Nosso dataset é estruturado (organizado em linhas e colunas, como uma tabela). Modelos como Random Forest e XGBoost são o estado-da-arte para este tipo de dado. Deep Learning, por outro lado, brilha com dados não estruturados (imagens, áudio, texto livre), onde não há uma organização tabular clara.
      Inadequado para Pequenos Datasets: Redes Neurais são "famintas por dados" (data-hungry). Com apenas 15 amostras, um modelo de Deep Learning iria quase certamente "decorar" os dados (overfitting), resultando num modelo inútil para previsões reais.
      Por que não LSTM? LSTM (Long Short-Term Memory) é uma arquitetura de rede neural especializada para dados sequenciais, onde a ordem é crucial (ex: séries temporais de preços de ações, palavras numa frase). Nossos dados não são sequenciais; cada local é independente. Usar LSTM aqui seria como usar uma ferramenta errada para a tarefa.

   3. Arquitetura Profissional: O Pipeline
     # O quê: Um objeto do scikit-learn que encapsula todas as etapas do projeto.
     # Porquê: Esta é a espinha dorsal do nosso código.

      Tratamento Completo dos Dados: O ColumnTransformer dentro do pipeline permite-nos usar todas as features, aplicando StandardScaler às colunas numéricas e OneHotEncoder às colunas de texto.
      Segurança e Reprodutibilidade: Garante que o pré-processamento e a modelagem sejam sempre executados na mesma ordem, eliminando o risco de erro humano.

# Análise dos Resultados
Desempenho
 R² (Coeficiente de Determinação): 0.958
 RMSE (Raiz do Erro Quadrático Médio): 0.018

# Artefato Gerado
A principal entrega deste notebook é o ficheiro tourism_model.pkl. Este ficheiro contém o Pipeline completo: uma "fábrica" autossuficiente que sabe como receber dados brutos, aplicar todo o pré-processamento e gerar uma previsão.

# Próximos Passos
   # Aumentar o Dataset: O passo mais crítico para melhorar o desempenho é adicionar mais pontos turísticos ao model_input.csv.
   # Visualização: Utilizar o pipeline salvo no notebook mapa_visualization.ipynb para gerar previsões e visualizá-las num mapa interativo.
   # Explorar Modelos de Deep Learning (Futuro):
   
   Redes Neurais: Uma vez que o dataset seja consideravelmente maior (centenas ou milhares de amostras), poderemos experimentar com Redes Neurais para dados tabulares, que poderiam capturar padrões não-lineares ainda mais complexos.
   Modelos Sequenciais (LSTM): Se o projeto evoluir para incluir dados de séries temporais (ex: número de visitantes por mês para cada local), a arquitetura LSTM se tornaria uma ferramenta extremamente relevante para prever tendências e sazonalidade.

## Como Executar
1. Instale as dependências listadas em `requirements.txt`.
2. Execute as células do notebook sequencialmente.
3. O modelo final será salvo em `models/tourism_model.pkl`.

