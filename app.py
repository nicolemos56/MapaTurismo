import streamlit as st
import pandas as pd
import joblib
import folium
from streamlit_folium import st_folium
from pathlib import Path
import subprocess
import sys

# ====================================================================
# APLICAÇÃO STREAMLIT ORQUESTRADORA DO PROJETO MAPATURISMO
# ====================================================================

# --- 1. CONFIGURAÇÃO DA PÁGINA E CAMINHOS ---
st.set_page_config(page_title="MapaTurismo Angola", page_icon="🗺️", layout="wide")

APP_DIR = Path(__file__).parent
MODEL_PATH = APP_DIR / "data" / "model_inputs" / "tourism_model.pkl"
MAIN_SCRIPT_PATH = APP_DIR / "scripts" / "main.py"

# --- 2. ESTADO DA APLICAÇÃO (SETUP vs. RUN) ---
# Usar o estado da sessão para controlar se o pipeline já foi executado
if 'pipeline_executed' not in st.session_state:
    st.session_state.pipeline_executed = False

# --- 3. FASE DE SETUP: EXECUTAR O PIPELINE DE DADOS ---

def run_main_pipeline():
    """Chama o script main.py para preparar dados e treinar o modelo."""
    st.info("Iniciando o pipeline de preparação de dados e treinamento do modelo...")
    st.warning("Este processo pode demorar vários minutos. Por favor, aguarde.")
    
    log_area = st.empty()
    log_area.code("Aguardando o início do processo...")

    try:
        # Executar o main.py usando o mesmo interpretador Python
        process = subprocess.Popen(
            [sys.executable, str(MAIN_SCRIPT_PATH)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='utf-8',
            bufsize=1
        )

        # Mostrar a saída do processo em tempo real
        log_content = ""
        for line in iter(process.stdout.readline, ''):
            log_content += line
            log_area.code(log_content)
        
        process.wait() # Esperar o processo terminar
        
        if process.returncode == 0:
            st.success("Pipeline executado com sucesso!")
            st.session_state.pipeline_executed = True
            st.balloons()
            st.button("Iniciar a Aplicação de Previsão") # Botão para recarregar a página
        else:
            st.error("O pipeline falhou. Verifique os logs acima para mais detalhes.")
            st.session_state.pipeline_executed = False

    except Exception as e:
        st.error(f"Ocorreu um erro ao tentar executar o pipeline: {e}")

# Mostrar a interface de setup se o pipeline ainda não foi executado ou o modelo não existe
if not st.session_state.pipeline_executed or not MODEL_PATH.exists():
    st.title("Mapeador Preditivo de Turismo em Angola — Setup Inicial")
    st.write(
        "Bem-vindo! Antes de usar a aplicação de previsão, é necessário executar o "
        "pipeline completo de preparação de dados e treinamento do modelo."
    )
    if st.button(" Iniciar Pipeline Completo"):
        run_main_pipeline()

# --- 4. FASE DE APLICAÇÃO: EXECUTAR A INTERFACE DE PREVISÃO ---
else:
    st.title(" MapaTurismo — Previsão de Potencial Turístico em Angola")

    # --- CARREGAR O MODELO (AGORA SABEMOS QUE ELE EXISTE) ---
    @st.cache_resource
    def carregar_pipeline(caminho_modelo):
        return joblib.load(caminho_modelo)
    
    pipeline = carregar_pipeline(MODEL_PATH)
    st.success("Modelo carregado com sucesso!")

    # --- O RESTO DA SUA APLICAÇÃO (INTERFACE DE PREVISÃO) ---
    st.sidebar.header("Adicionar Pontos para Previsão")
    uploaded_file = st.sidebar.file_uploader("Carregar um ficheiro CSV", type=["csv"])

    # ... (cole aqui o resto do seu código da interface do app.py:
    #      o formulário manual, a lógica de adição de dados,
    #      a exibição da tabela, o botão de predição e o mapa)
    # ...
    # Exemplo:
    with st.sidebar.form("form_manual", clear_on_submit=True):
        st.write("**Ou adicione um ponto manualmente:**")
        poi_nome = st.text_input("Nome do Ponto Turístico", "Ex: Praia Morena")
        provincia = st.text_input("Província", "Benguela")
        latitude = st.number_input("Latitude", value=-12.59, format="%.6f")
        longitude = st.number_input("Longitude", value=13.40, format="%.6f")
        submit_button = st.form_submit_button("Adicionar Ponto")
        # ... (etc.)