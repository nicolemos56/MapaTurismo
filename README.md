# MapaTurismo Angola: Análise Preditiva de Potencial Turístico


## 🌍 Visão Geral

Este projeto utiliza Ciência de Dados e Machine Learning para criar uma ferramenta de suporte à decisão para o setor do turismo em Angola. O objetivo é analisar e prever o potencial de desenvolvimento (medido pelo Índice de Desenvolvimento Humano - IDH) de diversas localidades turísticas, com base em dados geoespaciais, ambientais e socioeconômicos.

A aplicação final é um dashboard interativo que permite a investidores e planeadores governamentais visualizar e comparar o potencial de diferentes regiões, otimizando assim a alocação de recursos.

---

## 🚀 Como Executar o Projeto

A forma mais simples de ver o projeto em ação é através da nossa aplicação web implementada.

**URL da Aplicação:** **[http://13.222.132.210:8501/](http://13.222.132.210:8501/)**

*Nota: Por se tratar de um protótipo, a instância pode não estar sempre ativa.*

### Execução Local

Para executar o projeto no seu próprio ambiente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o pipeline de dados e treino (opcional, se quiser treinar o modelo do zero):**
    ```bash
    python scripts/main.py
    ```

5.  **Inicie a aplicação Streamlit:**
    ```bash
    streamlit run app.py  # Substitua 'app.py' pelo nome do seu script principal da aplicação
    ```
A aplicação estará disponível em `http://localhost:8501`.

---

## 📂 Estrutura do Repositório

O projeto está organizado da seguinte forma para garantir modularidade e clareza:

```
.
├── app.py                  # Script principal da aplicação Streamlit
├── data/                   # Conjuntos de dados brutos e processados
    ├── models/             # Modelos de Machine Learning treinados (.pkl)
├── documentation/          # Documentação técnica, relatórios e apresentações
├── notebooks/              # Jupyter Notebooks para análise exploratória e prototipagem
├── scripts/                # Scripts Python para coleta, processamento e treino
│   ├── 01_coleta_dados.py
│   ├── 02_feature_engineering.py
│   └── 03_treino_modelo.py
├── requirements.txt        # Lista de dependências Python
└── README.md               # Este arquivo
```

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias e bibliotecas:

*   **Análise de Dados e ML:** `Python`, `Scikit-learn`, `Pandas`, `GeoPandas`, `NumPy`
*   **Dados Geoespaciais:** `OSMnx`, `Folium`
*   **Dashboard Web:** `Streamlit`
*   **Fontes de Dados:** OpenStreetMap, ESA (Sentinel-2)

---

## 👥 Colaboradores

Este projeto foi desenvolvido com a dedicação e o trabalho em equipa de:

*   **[Nico cohen](https://github.com/nicolemos56)** (@nicolemos56) - Gestão de Projeto, Análise de Dados
*   **[Walissaco Jorge Tomás](https://github.com/Walissaco)** (@Walissaco) - Engenharia de Dados, Backend
*   **[Mbala Pedro Kiala Domingos](https://github.com/mbalapedrokialadomingos4)** (@mbalapedrokialadomingos4) - Machine Learning
*   **[Baltazar Henrique](https://github.com/baltahenrique647-fonte)** (@baltahenrique647-fonte) - Frontend, Visualização

Agradecemos a todos os contribuidores pelas suas valiosas contribuições.

