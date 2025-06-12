import streamlit as st
from pathlib import Path
from streamlit_option_menu import option_menu
from utils import dashboards, sobre, dataframe
from datetime import date
from utils.totalizadores import hoje,df
from utils.marcadores import texto,sidebar, background

st.set_page_config(
    layout="wide",
    page_title="SaudeRecife")

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
            "<h1>Unidades de saúde do Recife</h1>"
            "<p>Fonte: Dados abertos da Prefeitura do Recife</p>",
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div style="margin-top: 40px;">
                <a href="https://dados.recife.pe.gov.br/" target="_blank">
                    🔗 Acessar fonte dos dados
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
        st.markdown('<div class="custom-menu-title">📡 Conheça</div>', unsafe_allow_html=True)

        selected = option_menu(
        menu_title=None,  # Não usa o menu_title original
        options=["Sobre", "Dashboards", "Dataframe"],
        icons=["info-circle", "bar-chart", "table"],
        default_index=0,
        styles={
            "container": {"background-color": sidebar},
            "nav-link": {
                "color": "#031f72",
                "font-size": "18px",
                "hover-color": texto,
            },
            "nav-link-selected": {
                "background-color": "#ffffff",
                "color": texto,
            },
        }
    )

        # Título dos filtros
        st.markdown("<h1>Filtros</h1>", unsafe_allow_html=True)

        # Filtro de Opção
        opcoes_disponiveis = sorted(df_filtrado['Opção'].dropna().unique())
        filtro_opcao = st.multiselect('Selecione a Opção', opcoes_disponiveis)
        if filtro_opcao:
            df_filtrado = df_filtrado[df_filtrado['Opção'].isin(filtro_opcao)]

        # Filtro de Zona
        zonas_disponiveis = sorted(df_filtrado['Região'].dropna().unique())
        filtro_zona = st.multiselect('Selecione a Zona', zonas_disponiveis)
        if filtro_zona:
            df_filtrado = df_filtrado[df_filtrado['Região'].isin(filtro_zona)]

        # Filtro de Bairro
        bairros_disponiveis = sorted(df_filtrado['Bairro'].dropna().unique())
        filtro_bairro = st.multiselect('Selecione o Bairro', bairros_disponiveis)
        if filtro_bairro:
            df_filtrado = df_filtrado[df_filtrado['Bairro'].isin(filtro_bairro)]

        # Filtro de Especialidade
        Especialidade_disponiveis = sorted(df_filtrado['Especialidade'].dropna().unique())
        filtro_especialidade = st.multiselect('Selecione a Especialidade', Especialidade_disponiveis)
        if filtro_especialidade:
            df_filtrado = df_filtrado[df_filtrado['Especialidade'].isin(filtro_especialidade)]    

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