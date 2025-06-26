import streamlit as st
import os
from utils.totalizadores import *
from utils.marcadores import divisor

def sobre(df):
    # Cálculo dos totais
    total = calculo_total_unidades(df)
    totalHospital = calculo_total_hospitais(df)
    totalMaternidade = calculo_total_Maternidades(df)
    totalUSB = calculo_total_USB(df)
    totalUSF = calculo_total_USF(df)
    
    
    # Imagens
    imagem_path1 = os.path.join(os.path.dirname(__file__), '..', 'images', 'Hospital_da_mulher.jpg')
    

    st.markdown("<h2 style='text-align: center; color: #0b3d91;'>Panorama da Saúde Municipal do Recife</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Primeira seção com imagem e texto
    col1, col2 = st.columns([2, 3], gap="small")

    with col1:
        st.image(imagem_path1, use_container_width=True, clamp=True, caption="Ampliação de leitos de pediatria no Hospital da Mulher - 13")

    with col2:
        
        st.markdown(
            f"""
            <div style="text-align: justify; font-size: 17px">
            <p>
            Bem-vindo ao painel interativo sobre as unidades de saúde do Recife. Segundo o portal de dados abertos da Prefeitura da capital, a cidade conta com <strong>{total}</strong> unidades de saúde.
            Elas estão distribuídas entre: <br></p>
            <ul>
                <li><strong>{totalHospital}</strong> Hospitais</li>
                <li><strong>{totalMaternidade}</strong> Maternidades</li>
                <li><strong>{totalUSB}</strong> USB -  Unidades Básicas de Saúde</li>
                <li><strong>{totalUSF}</strong> USF - Unidades Saúde da Família</li>
            </ul>
            <p>
                Essas unidades de saúde  atendem todos os bairros do Recife, promovendo o acesso à tratamentos de saúde de forma descentralizada e inclusiva.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    

def mainSobre(df):
    divisor()
    sobre(df)
    divisor()
