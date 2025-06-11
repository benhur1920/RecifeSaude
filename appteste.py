from pathlib import Path
import streamlit as st
from PIL import Image

# Configurações Estruturais
diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
arquivo_css = diretorio / "styles" / "geral.css"
arquivo_pdf = diretorio / "assets" / "CurriculoBen-Hur.pdf"
arquivo_img = diretorio / "assets" / "foto.jpeg"

# Configuração geral da informações

TITULO = "Curriculum  |  Ben-Hur Beltrão"
NOME = "Ben-Hur Beltrão"
DESCRICAO = """

- ADS - Analise e Desenvolvimento de Sistemas
- Formado em Administração de Empresas 
- Pós-graduado em Administração Financeira 
    

"""
EMAIL = "benbeltrao@gmail.com"
MIDIA_SOCIAL = {
    "Linkedin": "XXXX@x.com",
    "Github": "XXXXX@x.com",
    "YOutube": "XXXXXX@x.com"
}
PROJETOS = {

    "🎯 - Desenvolviemento do Observatorio do Recife":"xxxxx@xxx.com",
    "🎯 - DashBoard de Lincencimentos":"xxxxx@xxx.com",
    "🎯 - DashBoard de Escolas":"xxxxxx@xxx.com",
    "🎯 - DashBoard de Saúde":"XXXXXX@xxxx.com"
}

st.set_page_config(
    page_title=TITULO
)


# Carregando arquivos de assets

with open(arquivo_css) as c:
    st.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html=True ) #Importa as informaçoes que estiverem no arquivo css

with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()

imagem = Image.open(arquivo_img)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(imagem, width=200)
with col2:
    st.title(NOME)
    st.write(DESCRICAO)
    st.download_button(
        label = "Download Curriculo",
        data=pdfLeitura,
        file_name=arquivo_pdf.name,
        mime="application/octet-stream"

    )
    st.write("✉️", EMAIL)

# Mídias sociais
st.write("#")
colunas = st.columns(len(MIDIA_SOCIAL))
for indice, (plataforma, link) in enumerate(MIDIA_SOCIAL.items()):
    colunas[indice].markdown(f"[{plataforma}]({link})", unsafe_allow_html=True)

#Experiencias
st.write("#")
st.subheader("Experiências")
st.write(
    """
        - 💹 22 anos de experiencia trabalhando com cargos de chefia
        - 💹 Análise de dados com python
        - 💹 Análise de dados com Power BI

    """
)
#skilss
st.write("#")
st.subheader("Skills")
st.write(
    """
        - 💹 Liderança
        - 💹 Análise de dados
        - 💹 Linguagem Python

    """
)

# Historico de trabalho
st.write("#")
st.subheader("Histórico de Trabalho")
st.write("---")

# Job 1
st.write("** Gerente de Cobrança **")
st.write("08/1996 - 04/2013")
st.write("Gestor das equipes de corte e religaçao na prestação de serviços para Neoenergia")

#Job 2
st.write("** Gerente de Canteiro**")
st.write("09/2014 - 01/2021")
st.write("Gestor de base das equipes de construção, manutenção de redes de energia do grupo Neoenergia")



# Projetos
st.write("#")
st.write("Projetos")
st.write("---")
for curso, link in PROJETOS.items():
    st.markdown(f"[{curso}]({link})", unsafe_allow_html=True)
