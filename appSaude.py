import streamlit as st
from streamlit_option_menu import option_menu
from utils import dashboards, sobre, dataframe
from utils.totalizadores import hoje, df

st.set_page_config(
    layout="wide",
    page_title="SaudeRecife"
)

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
        st.write(f"📅 Dados atualizados em: {hoje.strftime('%d/%m/%Y')}")

def aplicando_filtros(df_filtrado, nome_do_filtro):
    opcoes = sorted(df_filtrado[nome_do_filtro].dropna().unique())
    filtro = st.multiselect(f"Selecione {nome_do_filtro}", opcoes, placeholder="Selecione uma opção")
    if filtro:
        df_filtrado = df_filtrado[df_filtrado[nome_do_filtro].isin(filtro)]
    return df_filtrado

def criacao_navegacao_e_filtros():
    df_filtrado = df.copy()

    with st.sidebar:
        selected = option_menu(
            menu_title="Navegação",
            options=["Sobre", "Dashboards", "Dataframe"],
            icons=["info-circle", "bar-chart", "table"],
            default_index=0
        )

        st.markdown("### Filtros")
        df_filtrado = aplicando_filtros(df_filtrado, "Opção")
        df_filtrado = aplicando_filtros(df_filtrado, "Região")
        df_filtrado = aplicando_filtros(df_filtrado, "Bairro")

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

if __name__ == '__main__':
    main()
