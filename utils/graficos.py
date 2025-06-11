import matplotlib as pl
import plotly.express as px
import streamlit as st



#Criando o gráfico de distribuicao por zona
def grafico_zona(df):
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
                    'color': '#0b3d91'
                }
            },
            plot_bgcolor='#fcf7ff',
            paper_bgcolor='#fcf7ff',
        )
        return fig


# Criando o gráfico de distribuicao por bairro
def grafico_bairro(df):
        df_bairro = df.groupby('Bairro').size().reset_index(name='TOTAL')
        df_bairro = df_bairro.sort_values('TOTAL', ascending=False)

        fig1 =  px.bar(
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
                    'color':  '#0b3d91'
                }
            },
            plot_bgcolor='#fcf7ff',
            paper_bgcolor='#fcf7ff',
        )
        return fig1

# Criando o gráfico de Opção
def grafico_opcao(df):
    df_bairro = df.groupby('Opção').size().reset_index(name='TOTAL')
    df_bairro = df_bairro.sort_values('TOTAL', ascending=False)

    fig4 = px.pie(
        df_bairro,
        names='Opção',
        values='TOTAL',
        title='Opções de unidades de saúde'
    )

    fig4.update_traces(textposition='inside', textinfo='percent+label')

    fig4.update_layout(
        title={
            'text': 'Opções de unidades de saúde',
            'x': 0.5,
            'xanchor': 'center',
            'font': {
                'size': 22,
                'color':  '#0b3d91'
            }
        },
        plot_bgcolor='#fcf7ff',
        paper_bgcolor='#fcf7ff',
    )

    return fig4


# Criando o gráfico de distribuicao por mapa
def grafico_mapa(df):
    fig3 = px.scatter_mapbox(
        df,
        hover_name='Nome',
        hover_data={
            'Opção': True,
            'Região': True,
            'Bairro': True,
            'Como_usar': True,
            'Endereço': True,
            'Horario': True,
        },
        lat='Latitude',
        lon='Longitude',
        color='Opção',  # ← as cores agora representam os valores da coluna 'Opção'
        zoom=11,
        height=500
    )

    # Aumenta o tamanho das bolinhas
    fig3.update_traces(marker=dict(size=15))  # ajuste o valor conforme necessário
    
    fig3.update_layout(
        title={
            'text': 'Unidades básicas de saúde na cidade do Recife',
            'x': 0.5,
            'y': 0.90,  # ← abaixa o título (1.0 é o topo)
            'xanchor': 'center',
            'font': {
                'size': 22,
                'color': '#0b3d91'
            }
        },
        plot_bgcolor='#fcf7ff',
        paper_bgcolor='#fcf7ff',
        margin=dict(t=100, b=20, l=10, r=10)  # ← aqui você ajusta o espaço acima (top=t),
    )

    return fig3

# Criando o gráfico de distribuicao por especialidade
def grafico_especialidade(df):
        df_especialidade = df.groupby('Especialidade').size().reset_index(name='TOTAL')
        df_especialidade = df_especialidade.sort_values('TOTAL', ascending=False)

        fig5 =  px.bar(
            df_especialidade,
            x='Especialidade',
            y='TOTAL',
            
        )
        fig5.update_layout(
            title={
                'text': 'Total de especialidade',
                'x': 0.5,
                'xanchor': 'center',
                'font': {
                    'size': 22,
                    'color': 'white'
                }
            },  # <--- essa vírgula aqui é importante para separar os parâmetros
            plot_bgcolor='#0b3d91',
            paper_bgcolor='#0b3d91',
            font=dict(color='white'),
            xaxis=dict(showgrid=False, zeroline=False, color='white'),
            yaxis=dict(showgrid=False, zeroline=False, color='white')
        )

        return fig5

