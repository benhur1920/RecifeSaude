from dados.servicosSaude import df
import pandas as pd
import streamlit as st
import re
from datetime import date


# Data atual
hoje = date.today()


# Cópia do DataFrame original
df_filtrado = df.copy()

#Calculo da ultima e menor data do sistema
#ultima_data =  df['data'].max()
#primeira_data =  df['data'].min()


# Calculo dos totalizadores
def calculo_total_unidades(df):
    totalUnidades = df.shape[0]
    return totalUnidades

def calculo_total_hospitais(df):
    totalHospitais = (df['Opção']=="Hospital").sum()
    return f"{totalHospitais:,.0f}".replace(",", ".")

def calculo_total_Maternidades(df):
    totalMaternidade = (df['Opção']=="Maternidade").sum()
    return f"{totalMaternidade:,.0f}".replace(",", ".")

def calculo_total_USB(df):
    totalUSB = (df['Opção']=="USB").sum()
    return f"{totalUSB:,.0f}".replace(",", ".")

def calculo_total_USF(df):
    totalEscolas = (df['Opção'] == "USF").sum()
    return totalEscolas

def calular_a_quantidade_de_colunas(df):
    colunasDisponiveis = sorted(df.columns)
    return len(colunasDisponiveis)  




