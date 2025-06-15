import streamlit as st
import os
from utils.totalizadores import *
from utils.marcadores import divisor

def sobre(df):
    # Cálculo dos totais
    totalCrechesEscolas = calculo_total_creche_escola_municipal(df)
    totalEscolas = calculo_total_escola_municipal(df)
    totalCreches = calculo_total_creche_municipal(df)
    totalCmei = calculo_total_Cmei(df)
    totalProfessores = calculo_total_professores(df)
    totalAlunos = calculo_total_alunos(df)
    totalTurmas = calculo_total_turmas(df)
    totalUnidadesEnsino = calculo_total_unidades(df)
    
    # Imagens
    imagem_path1 = os.path.join(os.path.dirname(__file__), '..', 'images', 'escolas1.jpg')
    imagem_path2 = os.path.join(os.path.dirname(__file__), '..', 'images', 'escolas2.jpg')

    st.markdown("<h2 style='text-align: center; color: #0b3d91;'>Panorama da Educação Municipal do Recife</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Primeira seção com imagem e texto
    col1, col2 = st.columns([2, 3], gap="small")

    with col1:
        st.image(imagem_path1, use_container_width=True, clamp=True)

    with col2:
        
        st.markdown(
            f"""
            <div style="text-align: justify; font-size: 17px">
            <p>
            Bem-vindo ao painel interativo sobre as unidades de ensino do Recife. Segundo o portal de dados abertos da Prefeitura da capital, a cidade conta com <strong>{totalUnidadesEnsino}</strong> unidades de ensino.
            Elas estão distribuídas entre: <br></p>
            <ul>
                <li><strong>{totalEscolas}</strong> Escolas Municipais</li>
                <li><strong>{totalCreches}</strong> Creches</li>
                <li><strong>{totalCrechesEscolas}</strong> Creches Escolas</li>
                <li><strong>{totalCmei}</strong> CMEIs (Centros Municipais de Educação Infantil)</li>
            </ul>
            <p>
                Essas unidades de ensino  atendem todos os bairros do Recife, promovendo o acesso à educação de forma descentralizada e inclusiva.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Segunda seção com texto e imagem
    col3, col4 = st.columns([3, 2], gap="small")

    with col3:
        
        st.markdown(
            f"""
            <div style="text-align: justify; font-size: 17px ;">
                <p>
                    A rede municipal de ensino conta com aproximadamente:
                </p>
                <ul>
                    <li><strong>{totalProfessores}</strong> Professores</li>
                    <li><strong>{totalTurmas}</strong>Turmas</li>
                    <li><strong>{totalAlunos}</strong> Alunos</li>
                </ul> 
                <p>
                    Este painel foi desenvolvido com o objetivo de tornar os dados educacionais mais <strong>transparentes</strong>, <strong>acessíveis</strong> e <strong>visuais</strong>. 
                    Explore os <em>gráficos</em>, <em>filtros</em> e <em>mapas</em> disponíveis para conhecer melhor a realidade das escolas municipais do Recife e contribuir para uma educação pública cada vez mais eficiente, inclusiva e de qualidade.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.image(imagem_path2, use_container_width=True, clamp=True)

def mainSobre(df):
    divisor()
    sobre(df)
    divisor()
