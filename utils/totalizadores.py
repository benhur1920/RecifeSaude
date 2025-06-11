from dados.saude import df
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
    totalHospital = (df['Opção'] == "Hospital").sum()
    return totalHospital

def calculo_total_maternidades(df):
    totalMaternidade = (df['Opção'] == "Maternidade").sum()
    return totalMaternidade

def calculo_total_UBS(df):
    totalUBS = (df['Opção'] == "UBS").sum()
    return totalUBS

def calculo_total_USF(df):
    totalUSF = (df['Opção'] == "USF").sum()
    return totalUSF







