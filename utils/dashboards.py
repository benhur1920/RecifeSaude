import matplotlib as pl
import plotly.express as px
import streamlit as st
from utils.totalizadores import *
from utils.graficos import grafico_zona, grafico_bairro, grafico_tipo, grafico_mapa
from utils.marcadores import divisor


def graficos(df_filtrado):

    figura_zona = grafico_zona(df_filtrado)
    figura_bairro = grafico_bairro(df_filtrado)
    fig_mapa = grafico_mapa(df_filtrado)
    fig_tipo = grafico_tipo(df_filtrado)
    

    # Calculo dos totalizadores importando o resultado das funcoes do arquivo totalizadores.py
    totalUnidades = calculo_total_unidades(df_filtrado)
    totalHospital = calculo_total_hospitais(df_filtrado)
    totalMaternidade = calculo_total_Maternidades(df_filtrado)
    totalUSB = calculo_total_USB(df_filtrado)
    totalUSF = calculo_total_USF(df_filtrado)
    
    
    aba1, aba2, aba3 = st.tabs(['🏫 Unidades', '📈 Dashboards', '🗺️ Mapas'])

    with aba1:
        col1, col2, col3 = st.columns([1, 1.5, 4], vertical_alignment='center')

        with col1:
            st.metric("🏫 Total de unidades", value=(totalUnidades),  border=True)
            
        with col2:
            st.metric("🏥 Hospital", value=(totalHospital), border=True)
            st.metric("🤰 Maternidade", value=(totalMaternidade), border=True)
            st.metric("🏪 USB", value=(totalUSB), border=True)
            st.metric("🏡 USF", value=(totalUSF), border=True)
        with col3:
            st.plotly_chart(fig_tipo, use_container_width=True, stack=False)
           
        
    
         
        
    with aba2:

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