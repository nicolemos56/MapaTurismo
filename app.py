import streamlit as st
import pandas as pd
import joblib
import folium
from streamlit_folium import st_folium # Componente para renderizar mapas Folium
from pathlib import Path
import subprocess
import sys
import os
import time

# ====================================================================
# APLICAÇÃO STREAMLIT ORQUESTRADORA DO PROJETO MAPATURISMO
# ====================================================================

# --- 1. CONFIGURAÇÃO DA PÁGINA E CAMINHOS ---
st.set_page_config(page_title="MapaTurismo Angola", page_icon="🗺️", layout="wide")

APP_DIR = Path(__file__).parent
MODEL_PATH = APP_DIR / "data" / "model_inputs" / "tourism_model.pkl"
# Precisamos dos dados originais para obter IDH real, lat/lon, etc.
DATA_PATH = APP_DIR / "data" / "model_inputs" / "model_input.csv"
MAIN_SCRIPT_PATH = APP_DIR / "scripts" / "main.py"

# --- 2. ESTADO DA APLICAÇÃO ---
if 'pipeline_status' not in st.session_state:
    st.session_state.pipeline_status = "not_run"
if 'log_content' not in st.session_state:
    st.session_state.log_content = ""

# --- 3. FUNÇÃO PARA EXECUTAR O PIPELINE ---
# (Esta função permanece a mesma da versão anterior, que já está correta)
def run_main_pipeline():
    try:
        process = subprocess.Popen(
            [sys.executable, str(MAIN_SCRIPT_PATH)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0,
        )
        for line in iter(process.stdout.readline, b''):
            yield line.decode('utf-8', errors='replace')
        process.stdout.close()
        return_code = process.wait()
        yield return_code
    except Exception as e:
        yield f"\n\n ERRO CRÍTICO AO INICIAR O PIPELINE:\n{str(e)}"
        yield 1

# --- INTERFACE PRINCIPAL ---

if st.session_state.pipeline_status != "success" or not MODEL_PATH.exists():
    st.title(" Previsão de Potencial de Desenvolvimento Turístico com Machine Learning — Setup Inicial")
    st.markdown("...") # Mensagem de boas-vindas
    st.warning("Este processo pode demorar vários minutos.")

    if st.button("Iniciar Pipeline Completo", type="primary"):
        st.session_state.pipeline_status = "running"
        st.session_state.log_content = "Iniciando processo...\n"
        st.rerun()

    if st.session_state.pipeline_status == "running":
        st.info("Executando o pipeline...")
        log_placeholder = st.empty()
        log_placeholder.text_area("Log da Execução:", st.session_state.log_content, height=400)
        
        return_code = None
        for output in run_main_pipeline():
            if isinstance(output, str):
                st.session_state.log_content += output
                log_placeholder.text_area("Log da Execução:", st.session_state.log_content, height=400)
            else:
                return_code = output

        if return_code == 0:
            st.session_state.pipeline_status = "success"
        else:
            st.session_state.pipeline_status = "failed"
        st.rerun()

    if st.session_state.pipeline_status == "success":
        st.success("Pipeline executado com sucesso!")
        st.balloons()
        st.info("Recarregando para a aplicação principal...")
        time.sleep(3)
        st.rerun()
    
    elif st.session_state.pipeline_status == "failed":
        st.text_area("Log Final da Execução:", st.session_state.log_content, height=400)
        st.error("O pipeline falhou.")

# --- 4. FASE DE APLICAÇÃO: EXIBIÇÃO DO MAPA E PREVISÃO ---
else:
    st.sidebar.title("MapaTurismo")
    st.sidebar.success("Modelo pronto e dados carregados!")
    st.title("📊 Mapa de Potencial Turístico em Angola")
    st.markdown("Este mapa exibe os pontos turísticos analisados, com seu potencial de desenvolvimento (IDH) previsto pelo modelo.")

    # --- CARREGAR RECURSOS NECESSÁRIOS ---
    @st.cache_resource
    def carregar_recursos():
        """Carrega o modelo e os dados, usando cache para performance."""
        try:
            pipeline = joblib.load(MODEL_PATH)
            df_dados = pd.read_csv(DATA_PATH)
            return pipeline, df_dados
        except FileNotFoundError:
            st.error("Arquivos de modelo ou dados não encontrados. Por favor, execute o pipeline novamente.")
            st.session_state.pipeline_status = "not_run" # Força a volta para a tela de setup
            st.rerun()
    
    pipeline, df = carregar_recursos()

    # --- FAZER PREVISÕES (SE NECESSÁRIO) ---
    # Rodar as previsões nos dados carregados para garantir que estão atualizadas
    if 'idh_predito' not in df.columns:
        predicoes = pipeline.predict(df)
        df['idh_predito'] = predicoes

    # --- LÓGICA DE CRIAÇÃO DO MAPA (COPIADA DO NOTEBOOK) ---
    st.header("Mapa Interativo")
    map_center = [-11.2027, 17.8739]
    m = folium.Map(location=map_center, zoom_start=6, tiles="CartoDB positron")

    def get_marker_color(idh_predito):
        if idh_predito >= 0.8: return 'darkblue'
        elif idh_predito >= 0.7: return 'green'
        elif idh_predito >= 0.55: return 'orange'
        else: return 'red'

    for idx, row in df.iterrows():
        popup_html = f"""
        <h4>📍 {row['poi_nome']}</h4>
        <b>Província:</b> {row['provincia']}<br>
        <hr style='margin: 5px 0;'>
        <b>IDH Real (dados base):</b> {row['idh']:.3f}<br>
        <b>Potencial Predito (IDH):</b> <b style='font-size:1.1em;'>{row['idh_predito']:.3f}</b>
        """
        popup = folium.Popup(popup_html, max_width=300)
        
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=popup,
            tooltip=f"{row['poi_nome']} (Potencial: {row['idh_predito']:.3f})",
            icon=folium.Icon(color=get_marker_color(row['idh_predito']), icon='star')
        ).add_to(m)

    # --- EXIBIR O MAPA NO STREAMLIT ---
    st_folium(m, width="100%", height=500)

    # Adicionar uma seção para visualizar os dados
    with st.expander("Ver Tabela de Dados e Previsões"):
        st.dataframe(df[['poi_nome', 'provincia', 'latitude', 'longitude', 'idh', 'idh_predito']].style.format({
            'latitude': "{:.4f}", 'longitude': "{:.4f}",
            'idh': "{:.3f}", 'idh_predito': "{:.3f}"
        }))
    
    # Botão para re-executar o pipeline
    if st.sidebar.button("Re-executar Pipeline"):
        st.session_state.pipeline_status = "not_run"
        st.rerun()