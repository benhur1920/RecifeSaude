import matplotlib as pl
import plotly.express as px
import streamlit as st
from utils.totalizadores import *
from utils.graficos import grafico_zona, grafico_bairro, grafico_tipo, grafico_mapa, grafico_climatizacao, grafico_bibliotecas, grafico_sala
from utils.marcadores import divisor


def graficos(df_filtrado):

    figura_zona = grafico_zona(df_filtrado)
    figura_bairro = grafico_bairro(df_filtrado)
    fig_mapa = grafico_mapa(df_filtrado)
    fig_tipo = grafico_tipo(df_filtrado)
    figura_climatizacao = grafico_climatizacao(df_filtrado)
    figura_sala = grafico_sala(df_filtrado)
    figura_biblioteca = grafico_bibliotecas(df_filtrado)

    # Calculo dos totalizadores importando o resultado das funcoes do arquivo totalizadores.py
    totalUnidades = calculo_total_unidades(df_filtrado)
    totalProfessores = calculo_total_professores(df_filtrado)
    totalAlunos = calculo_total_alunos(df_filtrado)
    totalTurmas = calculo_total_turmas(df_filtrado)
    totalEscola = calculo_total_escola_municipal(df_filtrado)
    totalCreche = calculo_total_creche_municipal(df_filtrado)
    totalCrecheEscola = calculo_total_creche_escola_municipal(df_filtrado)
    totalCmei = calculo_total_Cmei(df_filtrado)
    
    aba1, aba2, aba3 = st.tabs(['🏫 Unidades', '📈 Dashboards', '🗺️ Mapas'])

    with aba1:
        col1, col2, col3 = st.columns([1, 1, 3], vertical_alignment='center')

        with col1:
            st.metric("🏫 Unidades de ensino", value=(totalUnidades),  border=True)
            st.metric("👨‍🏫 Professores", value=(totalProfessores), border=True)
        with col2:
            st.metric("👥 Alunos", value=(totalAlunos), border=True)
            st.metric("👨‍👩‍👧‍👦 Turmas", value=(totalTurmas), border=True)
        with col3:
            st.plotly_chart(fig_tipo, use_container_width=True, stack=False)
           
        col5, col6, col7 =  st.columns(3, gap="large") 
    
        with col5:
            st.plotly_chart(figura_climatizacao, use_container_width=True, stack=False)
        with col6:
            st.plotly_chart(figura_sala, use_container_width=True, stack=False)
        with col7:
            st.plotly_chart(figura_biblioteca, use_container_width=True, stack=False)    
        
    with aba2:

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("🏫  Escolas municipais", value=totalEscola, border=True)
        with col2:
            st.metric("👶 Creches municipais", value=totalCreche, border=True)
        with col3:
            st.metric("🏫👶 Creches escolas municipais", value=totalCrecheEscola, border=True)
        with col4:
            st.metric("🏠📚 Cmei", value=totalCmei, border=True)

        
        
        col5, col6 = st.columns(2, gap="small") 

        with col5:
            st.plotly_chart(figura_zona, use_container_width=True ) #config={"displayModeBar": False})
            
        with col6:
            st.plotly_chart(figura_bairro, use_container_width=True, stack=False)     
   
        
    with aba3:
        fig_mapa.update_layout(mapbox_style="open-street-map")
        fig_mapa.update_layout(margin={"r":0, "t":80, "l":0, "b":0})
        
        st.plotly_chart(fig_mapa, use_container_width=True)
        

def mainGraficos(df):
    divisor()
    graficos(df)
    divisor()