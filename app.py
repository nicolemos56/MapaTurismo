import streamlit as st
import pandas as pd
import numpy as np
import joblib
import folium
from streamlit_folium import st_folium
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
DATA_PATH = APP_DIR / "data" / "model_inputs" / "model_input.csv"
MAIN_SCRIPT_PATH = APP_DIR / "scripts" / "main.py"

# --- 2. ESTADO DA APLICAÇÃO E VERIFICAÇÃO INTELIGENTE ---
# ### ALTERAÇÃO PRINCIPAL: VERIFICA SE O MODELO JÁ EXISTE NO INÍCIO ###
if 'pipeline_status' not in st.session_state:
    if MODEL_PATH.exists():
        # Se o modelo já existe, pulamos o setup
        st.session_state.pipeline_status = "success"
    else:
        # Se não existe, o setup é necessário
        st.session_state.pipeline_status = "not_run"

if 'df_input' not in st.session_state:
    st.session_state.df_input = pd.DataFrame()
if 'df_results' not in st.session_state:
    st.session_state.df_results = pd.DataFrame()

# --- 3. FUNÇÃO PARA EXECUTAR O PIPELINE (sem alterações) ---
def run_main_pipeline():
    try:
        result = subprocess.run(
            [sys.executable, str(MAIN_SCRIPT_PATH)],
            capture_output=True, text=True, encoding='utf-8', errors='replace',
            check=False
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", f"Erro crítico ao iniciar o subprocesso: {str(e)}"

# --- INTERFACE PRINCIPAL ---

# --- FASE DE SETUP (só é mostrada se o pipeline_status não for 'success') ---
if st.session_state.pipeline_status != "success":
    st.title("MapaTurismo — Setup Inicial")
    st.markdown("Bem-vindo! O modelo de previsão ainda não foi treinado. É necessário executar o pipeline completo de preparação de dados e treinamento.")
    st.warning("Este processo pode demorar vários minutos.")

    if st.button(" Iniciar Pipeline Completo", type="primary"):
        st.session_state.pipeline_status = "running"
        st.rerun()
    
    if st.session_state.pipeline_status == "running":
        with st.spinner("Executando o pipeline... Por favor, aguarde. Isto pode demorar vários minutos."):
            return_code, stdout, stderr = run_main_pipeline()
            if return_code == 0:
                st.session_state.pipeline_status = "success"
            else:
                st.session_state.pipeline_status = "failed"
                st.session_state.error_log = stderr if stderr else stdout
        st.rerun()

    if st.session_state.pipeline_status == "success": # Esta parte só será vista brevemente após a execução
        st.success("Pipeline executado com sucesso!")
        st.balloons()
        st.info("Recarregando para a aplicação principal...")
        time.sleep(3)
        st.rerun()
    
    elif st.session_state.pipeline_status == "failed":
        st.error("O pipeline falhou. Verifique os detalhes do erro abaixo:")
        st.text_area("Log de Erro:", st.session_state.get("error_log", "Nenhum log de erro detalhado disponível."), height=300)

# --- FASE DE APLICAÇÃO (mostrada se o pipeline_status for 'success') ---
else:
    st.sidebar.title("Análise de Potencial")
    st.sidebar.success("Modelo pronto para uso!")
    st.title("MapaTurismo - Previsão de Potencial Turístico em Angola")
    
    @st.cache_resource
    def carregar_modelo(caminho_modelo):
        return joblib.load(caminho_modelo)
    
    pipeline = carregar_modelo(MODEL_PATH)

    st.sidebar.header("Adicionar Pontos para Análise")
    uploaded_file = st.sidebar.file_uploader("Carregar um ficheiro CSV", type=["csv"])
    if uploaded_file:
        df_uploaded = pd.read_csv(uploaded_file)
        st.session_state.df_input = pd.concat([st.session_state.df_input, df_uploaded], ignore_index=True).drop_duplicates().reset_index(drop=True)

    with st.sidebar.form("form_manual", clear_on_submit=True):
        st.write("**Ou adicione um ponto manualmente:**")
        manual_data = {
            'poi_nome': st.text_input("Nome do Ponto Turístico", "Ex: Praia Morena"),
            'provincia': st.text_input("Província", "Benguela"),
            'latitude': st.number_input("Latitude", value=-12.59, format="%.6f"),
            'longitude': st.number_input("Longitude", value=13.40, format="%.6f"),
        }
        submit_button = st.form_submit_button("Adicionar Ponto")
        if submit_button:
            st.session_state.df_input = pd.concat([st.session_state.df_input, pd.DataFrame([manual_data])], ignore_index=True)

    st.header("1. Pontos para Análise")
    if st.session_state.df_input.empty:
        st.info("Adicione pontos para análise usando as opções na barra lateral.")
    else:
        with st.expander("Ver/Ocultar Tabela de Pontos para Análise"):
            st.dataframe(st.session_state.df_input)

    if not st.session_state.df_input.empty:
        if st.button(" Prever Potencial e Gerar Mapa", type="primary"):
            with st.spinner("Realizando predições..."):
                df_to_predict = pd.DataFrame(columns=pipeline.feature_names_in_)
                df_to_predict = pd.concat([df_to_predict, st.session_state.df_input], ignore_index=True).fillna(0)
                predictions = pipeline.predict(df_to_predict)
                results = st.session_state.df_input.copy()
                results['idh_predito'] = predictions
                st.session_state.df_results = results
        
    if not st.session_state.df_results.empty:
        df_results = st.session_state.df_results
        st.header("2. Resultados e Mapa Interativo")
        
        st.sidebar.header("Opções de Visualização")
        max_points = len(df_results)
        if max_points > 1:
            top_n = st.sidebar.slider(
                "Exibir os 'Top N' pontos da sua lista:",
                min_value=1, max_value=max_points, value=max_points,
                help="Filtre o mapa para mostrar apenas os locais de maior potencial da sua lista."
            )
            df_display = df_results.sort_values('idh_predito', ascending=False).head(top_n)
        else:
            df_display = df_results
        
        with st.expander(f"Ver Tabela de Resultados (Top {len(df_display)})", expanded=True):
            st.dataframe(df_display.style.format({'idh_predito': "{:.3f}", 'latitude': "{:.4f}", 'longitude': "{:.4f}"}))
            csv_bytes = df_display.to_csv(index=False).encode("utf-8")
            st.download_button(" Descarregar Resultados Filtrados (CSV)", data=csv_bytes, file_name="predicoes_filtradas.csv", mime="text/csv")
        
        map_center = [-11.2027, 17.8739]
        m = folium.Map(location=map_center, zoom_start=5, tiles="CartoDB positron")
        
        def get_marker_color(idh_predito):
            if idh_predito >= 0.7: return 'green'
            elif idh_predito >= 0.55: return 'orange'
            else: return 'red'

        for _, row in df_display.iterrows():
            popup_html = f"<h4>📍 {row['poi_nome']}</h4><b>Província:</b> {row['provincia']}<br><hr style='margin: 5px 0;'><b>Potencial Predito (IDH):</b> <b style='font-size:1.1em;'>{row['idh_predito']:.3f}</b>"
            popup = folium.Popup(popup_html, max_width=300)
            
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=popup,
                tooltip=f"{row['poi_nome']} (Potencial: {row['idh_predito']:.3f})",
                icon=folium.Icon(color=get_marker_color(row['idh_predito']), icon='star')
            ).add_to(m)
        
        st_folium(m, width="100%", height=600, returned_objects=[])

    if not st.session_state.df_input.empty:
        if st.button("Limpar Pontos"):
            st.session_state.df_input = pd.DataFrame()
            st.session_state.df_results = pd.DataFrame()
            st.rerun()

    # Botão para forçar a re-execução do pipeline
    st.sidebar.markdown("---")
    if st.sidebar.button("Forçar Re-execução do Pipeline"):
        st.session_state.pipeline_status = "not_run"
        st.rerun()