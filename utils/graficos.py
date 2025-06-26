import matplotlib as pl
import plotly.express as px
import streamlit as st
from utils.marcadores import texto, background, sidebar



#Criando o gráfico de distribuicao por zona
def grafico_zona(df):
        
        if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
            st.warning("Não há dados disponíveis para gerar o gráfico de região.")
            return None
        
        df_agrupado = df.groupby('Região')[['Bairro']].count().reset_index()
        
        fig =  px.treemap(
            df_agrupado,
            path=['Região'],
            values='Bairro',
            color='Bairro',
            
        )
        fig.update_layout(
            title={
                'text': 'Unidades básicas de saúde por região',
                'x': 0.5,
                'xanchor': 'center',
                'font': {
                    'size': 22,
                    'color': texto
                }
            },
            plot_bgcolor= background,
            paper_bgcolor= background,
            font=dict(color=texto),
            modebar=dict(
            bgcolor=background,
            color=texto,
            activecolor=texto
            )
        )
        return fig


# Criando o gráfico de distribuicao por bairro
def grafico_bairro(df):

    if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
            st.warning("Não há dados disponíveis para gerar o gráfico de região.")
            return None
    
    df_bairro = df.groupby('Bairro').size().reset_index(name='TOTAL')
    df_bairro = df_bairro.sort_values('TOTAL', ascending=False)

    fig1 = px.bar(
        df_bairro,
        x='Bairro',
        y='TOTAL',
    )

    fig1.update_layout(
        title={
            'text': 'Unidades básicas de saúde por bairro',
            'x': 0.5,
            'xanchor': 'center',
            'font': {
                'size': 22,
                'color': texto
            }
        },
        xaxis_title='Bairro',
        yaxis_title='Total',
        xaxis_title_font=dict(size=18, color=texto),
        yaxis_title_font=dict(size=18, color=texto),
        xaxis_tickfont=dict(size=14, color=texto),
        yaxis_tickfont=dict(size=14, color=texto),
        plot_bgcolor=background,
        paper_bgcolor=background,
        modebar=dict(
            bgcolor=background,
            color=texto,
            activecolor=texto
            )
    )

    return fig1

# Criando o gráfico de Tipo de unidade de ensino
def grafico_tipo(df):

    if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
            st.warning("Não há dados disponíveis para gerar o gráfico de região.")
            return None
    
    df_bairro = df.groupby('Opção').size().reset_index(name='TOTAL')
    df_bairro = df_bairro.sort_values('TOTAL', ascending=False)

    fig4 = px.pie(
        df_bairro,
        names='Opção',
        values='TOTAL',
        title='Tipos de unidades de ensino'
    )

    fig4.update_traces(textposition='inside', textinfo='percent+label', textfont=dict(size=22) )

    fig4.update_layout(
    title={
        'text': 'Tipos de unidades de saúde',
        'x': 0.5,
        'xanchor': 'center',
        'font': {
            'size': 22,
            'color': texto
        }
    },
    plot_bgcolor=background,
    paper_bgcolor=background,
    # altera a legenda do grafico aqui
    legend=dict(
        font=dict(
            color=texto  # cor do texto da legenda
        )
    ),
    modebar=dict(
        bgcolor=background,
        color=texto,
        activecolor=texto
    )
)


    return fig4


# Criando o gráfico de distribuicao por mapa
def grafico_mapa(df):

    if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
            st.warning("Não há dados disponíveis para gerar o gráfico de região.")
            return None
    
    fig3 = px.scatter_mapbox(
        df.dropna(subset=['Latitude', 'Longitude']),
        hover_name='Nome',
        hover_data={
            'Opção': True,
            'Região': True,
            'Bairro': True,
            'Endereço': True,
            'Especialidade': True,
        },
        lat='Latitude',
        lon='Longitude',
        color='Opção',
        zoom=11,
        height=700
    )

    fig3.update_traces(marker=dict(size=15))
    
    fig3.update_layout(
    mapbox_style="open-street-map",
    mapbox_center={"lat": -8.0476, "lon": -34.8770},

    legend=dict(
        title_text='Tipo de Unidade de saúde',
        title_font=dict(size=20, color=texto),
        font=dict(size=12, color=texto),
        orientation='h',           # ← Horizontal
        x=0.5,                     # ← Centro horizontal da tela
        y=1.05,                    # ← Acima da área do gráfico (ajuste fino se quiser)
        xanchor='center',
        yanchor='bottom',
        bgcolor=background,
        #bordercolor='black',
        borderwidth=1
    ),

    plot_bgcolor=background,
    paper_bgcolor=background,
    margin=dict(t=150, b=20, l=10, r=10),  # ← Aumentei o top pra dar espaço
    modebar=dict(
        bgcolor=background,
        color=texto,
        activecolor=texto
    )
)



    return fig3






