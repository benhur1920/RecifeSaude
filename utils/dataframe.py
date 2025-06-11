import streamlit as st
from utils.marcadores import divisor

def dataframe(df_filtrado):
    
    

    st.markdown(
        f"""
        <div style="text-align: center;  color: #0b3d91; margin-top: 60px">
            <h3>Download dos dados</h3>
                        
        </div>
        """, unsafe_allow_html=True
    )
    
    st.dataframe(df_filtrado)
    
    csv = df_filtrado.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
    st.download_button(
        label="📥 Baixar CSV",
        data=csv,
        file_name='unidades_saude_recife.csv',
        mime='text/csv'
    )

def mainDataframe(df_filtrado):
    divisor()
    dataframe(df_filtrado)
    divisor()