import streamlit as st
from pathlib import Path
from streamlit_option_menu import option_menu
from utils import dashboards, sobre, dataframe
from datetime import date
from utils.totalizadores import hoje,df
from utils.marcadores import texto,sidebar, background

st.set_page_config(
    layout="wide",
    page_title="EscolasRecife")


# Configurações Estruturais
ROOT_DIR = Path(__file__).resolve().parent
CSS_FILE = ROOT_DIR / "styles" / "geral.css"

with open(CSS_FILE, "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Mostra a data mais recente, importar dos totalizadores.py
#st.write(f"📅 Última atualização dos dados: {ultima_data.strftime('%d/%m/%Y')}")

def titulo_pagina():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(
            "<h1>Unidades de ensino do Recife</h1>"
            "<p>Fonte: Dados abertos da Prefeitura do Recife</p>",
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div style="margin-top: 40px;">
                <a href="https://dados.recife.pe.gov.br/" target="_blank">
                    🛢️ Acessar fonte dos dados
                </a>
            </div>
            """,
            unsafe_allow_html=True
        
        )
        # Exibe a data no formato desejado
        st.write(f"📅 Dados atualizados em: {hoje.strftime('%d/%m/%Y')}")



def criacao_navegacao_e_filtros():
    
    # Cópia do DataFrame original
    df_filtrado = df.copy()

    # Sidebar: Menu + Filtros
    with st.sidebar:
        st.markdown('<div class="custom-menu-title"><p>📡 Conheça</p></div>', unsafe_allow_html=True)

        selected = option_menu(
            menu_title=None,  # Não usa o menu_title original
            options=["Sobre", "Dashboards", "Dataframe"],
            icons=["info-circle", "bar-chart", "table"],
            default_index=0,
            styles={
                "container": {"background-color": sidebar},
                "nav-link": {
                    "color": "#fffddf",
                    "font-size": "18px",
                    "hover-color": texto,
                },
                "nav-link-selected": {
                    "background-color": "#ffffff",
                    "color": background,
                },
            }
        )

        
        # Título dos filtros
        st.markdown("<h1>Filtros</h1>", unsafe_allow_html=True)

        # Filtro de Opção
        tipo = sorted(df_filtrado['Tipo'].dropna().unique())
        filtro_tipo = st.multiselect('Selecione o tipo de escola', tipo, placeholder="Selecione uma opção")
        if filtro_tipo:
            df_filtrado = df_filtrado[df_filtrado['Tipo'].isin(filtro_tipo)]

        # Filtro de Zona
        zonas_disponiveis = sorted(df_filtrado['Região'].dropna().unique())
        filtro_zona = st.multiselect('Selecione a região', zonas_disponiveis, placeholder="Selecione uma opção")
        if filtro_zona:
            df_filtrado = df_filtrado[df_filtrado['Região'].isin(filtro_zona)]

        # Filtro de Bairro
        bairros_disponiveis = sorted(df_filtrado['Bairro'].dropna().unique())
        filtro_bairro = st.multiselect('Selecione o bairro', bairros_disponiveis, placeholder="Selecione uma opção")
        if filtro_bairro:
            df_filtrado = df_filtrado[df_filtrado['Bairro'].isin(filtro_bairro)]

        # Filtro de Climatização
        Climatizacao_disponiveis = sorted(df_filtrado['Escola_climatizada'].dropna().unique())
        filtro_climatizacao = st.multiselect('Selecione o tipo de climatização', Climatizacao_disponiveis, placeholder="Selecione uma opção")
        if filtro_climatizacao:
            df_filtrado = df_filtrado[df_filtrado['Escola_climatizada'].isin(filtro_climatizacao)]

        # Filtro de Biblioteca
        Biblioteca_disponiveis = sorted(df_filtrado['Biblioteca'].dropna().unique())
        filtro_biblioteca = st.multiselect('Selecione se possui biblioteca', Biblioteca_disponiveis, placeholder="Selecione uma opção")
        if filtro_biblioteca:
            df_filtrado = df_filtrado[df_filtrado['Biblioteca'].isin(filtro_biblioteca)]        

    # Conteúdo principal
    if selected == "Sobre":
        sobre.mainSobre(df)
    elif selected == "Dashboards":
        dashboards.mainGraficos(df_filtrado)
    else:
        dataframe.mainDataframe(df_filtrado)
    return df_filtrado

def main():
    titulo_pagina()
    criacao_navegacao_e_filtros()

# Definição do programa principal será o main()
if __name__ == '__main__':
    main()