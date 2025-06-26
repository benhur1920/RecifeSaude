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
            "<h1>Unidades de Saúde do Recife</h1>"
            "<p>Fonte: Dados abertos da Prefeitura do Recife</p>",
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div style="margin-top: 40px;">
                <a href="http://dados.recife.pe.gov.br/dataset?q=saude&sort=score+desc%2C+metadata_modified+desc" target="_blank">
                    🛢️ Acessar fonte dos dados
                </a>
            </div>
            """,
            unsafe_allow_html=True
        
        )
        # Exibe a data no formato desejado
        st.write(f"📅 Dados atualizados em: {hoje.strftime('%d/%m/%Y')}")

def aplicando_filtros(df_filtrado, nome_do_filtro):
    opcoes = sorted(df_filtrado[nome_do_filtro].dropna().unique())
    filtro = st.multiselect(f"Selecione {nome_do_filtro}", opcoes, placeholder="Selecione uma opção")
    if filtro:
        df_filtrado = df_filtrado[df_filtrado[nome_do_filtro].isin(filtro)]
    return df_filtrado


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
        df_filtrado = aplicando_filtros(df_filtrado, "Opção")

        # Filtro de Zona
        df_filtrado = aplicando_filtros(df_filtrado, "Região")

        # Filtro de Bairro
        df_filtrado = aplicando_filtros(df_filtrado, "Bairro")

        
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