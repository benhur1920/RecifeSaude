import matplotlib as pl
import plotly.express as px
import streamlit as st
from utils.totalizadores import calculo_total_unidades, calculo_total_hospitais, calculo_total_maternidades,calculo_total_UBS, calculo_total_USF
from utils.graficos import grafico_zona, grafico_bairro, grafico_opcao, grafico_mapa, grafico_especialidade
from utils.marcadores import divisor

def graficos(df_filtrado):

    figura_zona = grafico_zona(df_filtrado)
    figura_bairro = grafico_bairro(df_filtrado)
    fig_mapa = grafico_mapa(df_filtrado)
    fig_opcao = grafico_opcao(df_filtrado)
    figura_especialidade = grafico_especialidade(df_filtrado)

    # Calculo dos totalizadores importando o resultado das funcoes do arquivo totalizadores.py
    totalUnidades = calculo_total_unidades(df_filtrado)
    totalHospital = calculo_total_hospitais(df_filtrado)
    totalMaternidade = calculo_total_maternidades(df_filtrado)
    totalUBS = calculo_total_UBS(df_filtrado)
    totalUSF = calculo_total_USF(df_filtrado)

    aba1, aba2, aba3 = st.tabs(['🏫 Unidades', '📈 Dashboards', '🗺️ Mapas'])

    with aba1:
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total de unidades básicas de saúde", value=int(totalUnidades),  border=True)
            col5, col6 = st.columns(2)
            with col5:
                st.metric("Total de USF", value=int(totalUSF), border=True)
                st.metric("Total de UBS", value=int(totalUBS), border=True)
                
            with col6:
                st.metric("Total de Hospitais", value=int(totalHospital), border=True)
                st.metric("Total de Maternidades", value=int(totalMaternidade), border=True)
                
        
        with col2:
            st.plotly_chart(fig_opcao, use_container_width=True, stack=False)
            
        
    with aba2:

        col3, col4 = st.columns(2)
            
        with col3:
            st.plotly_chart(figura_zona, use_container_width=True ) #config={"displayModeBar": False})
            
        with col4:
            st.plotly_chart(figura_bairro, use_container_width=True, stack=False)     
   
        
    with aba3:
        fig_mapa.update_layout(mapbox_style="open-street-map")
        fig_mapa.update_layout(margin={"r":0, "t":80, "l":0, "b":0})
        
        st.plotly_chart(fig_mapa, use_container_width=True)
        

def mainGraficos(df):
    divisor()
    graficos(df)
    divisor()