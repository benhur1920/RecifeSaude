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
    
    df_bairro = df.groupby('Tipo').size().reset_index(name='TOTAL')
    df_bairro = df_bairro.sort_values('TOTAL', ascending=False)

    fig4 = px.pie(
        df_bairro,
        names='Tipo',
        values='TOTAL',
        title='Tipos de unidades de ensino'
    )

    fig4.update_traces(textposition='inside', textinfo='percent+label')

    fig4.update_layout(
    title={
        'text': 'Tipos de unidades de ensino',
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
        hover_name='Escola',
        hover_data={
            'Tipo': True,
            'Região': True,
            'Bairro': True,
            'Rua': True,
            'Numero': True,
        },
        lat='Latitude',
        lon='Longitude',
        color='Tipo',
        zoom=11,
        height=700
    )

    fig3.update_traces(marker=dict(size=15))
    
    fig3.update_layout(
    mapbox_style="open-street-map",
    mapbox_center={"lat": -8.0476, "lon": -34.8770},

    legend=dict(
        title_text='Tipo de Escola',
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


# Criando o gráfico de distribuicao por climatizacao
def grafico_climatizacao(df):
        
        if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
            st.warning("Não há dados disponíveis para gerar o gráfico de região.")
            return None
        
        df_climatizacao = df.groupby('Escola_climatizada').size().reset_index(name='TOTAL')
        df_climatizacao = df_climatizacao.sort_values('TOTAL', ascending=False)

        fig5 =  px.bar(
            df_climatizacao,
            x='Escola_climatizada',
            y='TOTAL',
            labels={'Escola_climatizada': 'Escola climatizada'},
            
        )
        fig5.update_layout(
            title={
                'text': 'Escolas climatizadas',
                'x': 0.5,
                'xanchor': 'center',
                'font': {
                    'size': 22,
                    'color': texto
                }
            },  # <--- essa vírgula aqui é importante para separar os parâmetros
            plot_bgcolor=background,
            paper_bgcolor=background,
            font=dict(color=texto),
            xaxis=dict(
                showgrid=False,
                zeroline=False,
                tickfont=dict(color=texto),
                title_font=dict(color=texto, size=16)
            ),
            yaxis=dict(
                showgrid=False,
                zeroline=False,
                tickfont=dict(color=texto),
                title_font=dict(color=texto, size=16)
            ),
            modebar=dict(
            bgcolor=background,
            color=texto,
            activecolor=texto
            )
        )

        return fig5

# Criando o gráfico de distribuicao por sala de recuros
def grafico_sala(df):
        
        if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
            st.warning("Não há dados disponíveis para gerar o gráfico de região.")
            return None
        
        df_sala = df.groupby('Sala_recurso').size().reset_index(name='TOTAL')
        df_sala = df_sala.sort_values('TOTAL', ascending=False)

        fig6 =  px.bar(
            df_sala,
            x='Sala_recurso',
            y='TOTAL',
            labels={'Sala_recurso': 'Sala recurso'},
            
        )
        fig6.update_layout(
            title={
                'text': 'Escolas com salas de recursos',
                'x': 0.5,
                'xanchor': 'center',
                'font': {
                    'size': 22,
                    'color': texto
                }
            },  # <--- essa vírgula aqui é importante para separar os parâmetros
            plot_bgcolor=background,
            paper_bgcolor=background,
            font=dict(color=texto),
            xaxis=dict(
                showgrid=False,
                zeroline=False,
                tickfont=dict(color=texto),
                title_font=dict(color=texto, size=16)
            ),
            yaxis=dict(
                showgrid=False,
                zeroline=False,
                tickfont=dict(color=texto),
                title_font=dict(color=texto, size=16)
            ),

            modebar=dict(
            bgcolor=background,
            color=texto,
            activecolor=texto
            )
        )

        return fig6

# Criando o gráfico de distribuicao por Bibliotecas
def grafico_bibliotecas(df):
        
        if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
            st.warning("Não há dados disponíveis para gerar o gráfico de região.")
            return None
        
        df_bibliotecas = df.groupby('Biblioteca').size().reset_index(name='TOTAL')
        df_bibliotecas = df_bibliotecas.sort_values('TOTAL', ascending=False)

        fig7 = px.bar(
            df_bibliotecas,
            x='Biblioteca',
            y='TOTAL',
        )
        fig7.update_layout(
            title={
                'text': 'Escolas com Bibliotecas',
                'x': 0.5,
                'xanchor': 'center',
                'font': {
                    'size': 22,
                    'color': texto
                }
            },
            plot_bgcolor=background,
            paper_bgcolor=background,
            font=dict(color=texto),
            xaxis=dict(
                showgrid=False,
                zeroline=False,
                tickfont=dict(color=texto),
                title_font=dict(color=texto, size=16)
            ),
            yaxis=dict(
                showgrid=False,
                zeroline=False,
                tickfont=dict(color=texto),
                title_font=dict(color=texto, size=16)
            ),
            modebar=dict(
            bgcolor=background,
            color=texto,
            activecolor=texto
            )
        )

        return fig7




