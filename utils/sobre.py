import streamlit as st
import os
from utils.totalizadores import calculo_total_unidades
from utils.marcadores import divisor

def sobre(df):

    
    imagem_path3 = os.path.join(os.path.dirname(__file__), '..', 'images', 'hospitalgnoite.jpg')  # ou o nome 
    #correto da imagem
    col1, col2 = st.columns([2,4],gap="large")  # proporção da largura das colunas

    with col1:
        
        st.image(imagem_path3, use_container_width=True,clamp=True) 
    with col2:
        totalUnidadesSaude = calculo_total_unidades(df)
        st.markdown(
        f"""
        <div style="text-align: center;  color: #0b3d91; margin-top: 10px">
        <h3>Unidades de saúde do Recife</h3>
            <p>
            Aqui você encontra  {totalUnidadesSaude} unidades de saúde do Recife, com informações atualizadas, baseadas em dados abertos disponibilizados pela Prefeitura. Explore a rede de hospitais da cidade, com diversas especialidades distribuídas pelos bairros do Recife, garantindo serviços de saúde de qualidade para toda a população.
            </p>
            
        </div>
        """, unsafe_allow_html=True
    ) 
        
        

def mainSobre(df):
    divisor()
    sobre(df)
    divisor()