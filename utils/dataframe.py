import streamlit as st
from utils.marcadores import divisor
from utils.totalizadores import calular_a_quantidade_de_colunas, calculo_total_unidades



def dataframe(df_filtrado):
    
    
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: 60px">
            <h3>Download dos dados</h3>
                        
        </div>
        """, unsafe_allow_html=True
    )
    
    #st.dataframe(df_filtrado)
    # Seleção de colunas
    with st.expander('Clique para selecionar as colunas  que deseja para download do seu arquivo .csv na seta'):
        colunas = st.multiselect(
            'Selecione as Colunas',
            options=list(df_filtrado.columns),
            default=list(df_filtrado.columns),
            
        )
    
    filtro_dados=df_filtrado.copy()
    # Aplica seleção de colunas
    filtro_dados = filtro_dados[colunas]

    # Informa o tamanho do dataset filtrado
    totalLinhas = calculo_total_unidades(df_filtrado)
    totalColunas =  calular_a_quantidade_de_colunas(filtro_dados)

    # Mostra os dados
    st.data_editor(filtro_dados, use_container_width=True)



    
    # Estilo do buttom de dawnload
    st.markdown("""
    <style>
    .stDownloadButton button {
        color: #000000 !important;
        background-color:  #ffffff!important;
        size: 22px !importante
    }
    </style>
    """, unsafe_allow_html=True)


    col1, col2 = st.columns([4,1])
    with col1:
        csv = filtro_dados.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="data.csv",
            mime="text/csv",
            icon=":material/download:",
        )
    with col2:
        st.metric("Total linhas filtradas ", value=(totalLinhas), border=True)
        st.metric("Total colunas filtradas ", value=(totalColunas), border=True)

def mainDataframe(df_filtrado):
    divisor()
    dataframe(df_filtrado)
    divisor()