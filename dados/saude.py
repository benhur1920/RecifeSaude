import pandas as pd
from unidecode import unidecode


def entrada_de_dados(url):
    df = pd.read_csv(url, sep=';', encoding='utf-8')
    #print(df[['latitude', 'longitude']].head())
    return df

def converter_latitude_e_longitude_para_string(df):
    df['latitude'] = df['latitude'].astype(str)
    df['longitude'] = df['longitude'].astype(str)
    return df

def substituir_ponto_por_virgula_longitude_e_latitude(df):
    df['latitude'] = df['latitude'].fillna('').astype(str)
    df['longitude'] = df['longitude'].fillna('').astype(str)
    
    def tratar_valor(x):
        if x == '':
            return ''
        return x.replace('.', ',', 1)[:7]
    
    df['latitude'] = df['latitude'].apply(tratar_valor)
    df['longitude'] = df['longitude'].apply(tratar_valor)
    return df

def converter_para_float_seguro(coluna):
    import pandas as pd
    return pd.to_numeric(coluna.str.replace(',', '.'), errors='coerce')



def usar_title_para_deixar_primeira_letra_como_maiuscula(df):
    df = df.apply(lambda x: x.str.title() if x.dtype == "object" else x)
    return df

def criar_a_coluna_opcao(df, nome_opcao):
    df['Opção'] = nome_opcao
    return df

def criar_um_novo_DataFrame_com_as_colunas_desejadas_e_renomeando_as(df):
   
    df = df[['nome_oficial', 'endereço', 'bairro', 'fone', 'especialidade', 'horario', 'como_usar', 'latitude', 'longitude',
                       'Opção']].rename(columns={'nome_oficial': 'Nome'})
    return df

def concatenar_DataFrames( hospital, usf, maternidade, ubs ):
    dados = pd.concat([hospital, usf, maternidade, ubs], ignore_index=True)
    return dados

def Aplicar_capitalize_a_coluna_como_usar(dados):
    dados['como_usar'] = dados['como_usar'].apply(str.capitalize)
    return dados

def salvar_o_DataFrame_no_arquivo_CSV_com_codificação_UTF_8_para_subir_para_o_BI(dados):
    dados.to_csv('ServicosSaude.csv', sep=';',encoding='utf-8-sig', index=False)

def mensagem(mensagem):
    """
    Função para informar mensagem para o usuario
    
    Retorna:
        Sem retorno
    """
    print(mensagem)

def criar_a_coluna_Regiao(df):
    dicionario = {
        'Centro': [
            'Boa Vista', 'Cabanga', 'Coelhos', 'Ilha Do Leite', 'Ilha Joana Bezerra',
            'Paissandu', 'Recife', 'Santo Amaro', 'Santo Antônio', 'Soledade', 'São José'
        ],
        'Noroeste': [
            'Aflitos', 'Alto Do Mandu', 'Alto José Bonifácio', 'Alto José Do Pinho', 'Apipucos',
            'Brejo Da Guabiraba', 'Brejo De Beberibe', 'Casa Amarela', 'Casa Forte',
            'Córrego Do Jenipapo', 'Derby', 'Dois Irmãos', 'Espinheiro', 'Graças', 'Guabiraba',
            'Jaqueira', 'Macaxeira', 'Mangabeira', 'Monteiro', 'Morro Da Conceição',
            'Nova Descoberta', 'Parnamirim', 'Passarinho', 'Pau Ferro', 'Poço', 'Santana',
            'Sítio Dos Pintos', 'Tamarineira', 'Vasco Da Gama'
        ],
        'Norte': [
            'Alto Santa Terezinha', 'Arruda', 'Beberibe', 'Bomba Do Hemetério', 'Cajueiro',
            'Campina Do Barreto', 'Campo Grande', 'Dois Unidos', 'Encruzilhada', 'Fundão',
            'Hipódromo', 'Linha Do Tiro', 'Peixinhos', 'Ponto De Parada', 'Porto Da Madeira',
            'Rosarinho', 'Torreão', 'Água Fria'
        ],
        'Oeste': [
            'Caxangá', 'Cidade Universitária', 'Cordeiro', 'Engenho Do Meio',
            'Ilha Do Retiro', 'Iputinga', 'Madalena', 'Prado', 'Torre',
            'Torrões', 'Várzea', 'Zumbi'
        ],
        'Sudeste': [
            'Afogados', 'Areias', 'Barro', 'Bongi', 'Caçote', 'Coqueiral', 'Curado',
            'Estância', 'Jardim São Paulo', 'Jiquiá', 'Mangueira', 'Mustardinha',
            'San Martin', 'Sancho', 'Tejipió', 'Totó'
        ],
        'Sul': [
            'Boa Viagem', 'Brasília Teimosa', 'Cohab', 'Ibura',
            'Imbiribeira', 'Ipsep', 'Jordão', 'Pina'
        ]
    }

    # Criar dicionário com bairros sem acento como chave
    bairro_para_regiao = {
        unidecode(bairro).strip().title(): regiao
        for regiao, bairros in dicionario.items()
        for bairro in bairros
    }

    df['Bairro_norm'] = df['bairro'].astype(str).apply(lambda x: unidecode(x).strip().title())
    # Criar a coluna Região
    df['Região'] = df['Bairro_norm'].map(bairro_para_regiao)

    # (Opcional) remover a coluna auxiliar
    df.drop(columns='Bairro_norm', inplace=True)

    return df

def aplicando_capitalize_no_nome_das_colunas(df):
    df.columns = [col.strip().capitalize() for col in df.columns]
    return df

def retirando_os_sinais_coluna_especialidade(df):
    df['Especialidade'] = df['Especialidade'].astype(str).apply(unidecode)
    return df

def main():
    urlhospital = 'http://dados.recife.pe.gov.br/dataset/6c77a814-7161-4eb5-9662-234642dc8cc1/resource/a2dab4d4-3a7b-4cce-b3a7-dd7f5ef22226/download/hospitais.csv'
    urlusf = 'http://dados.recife.pe.gov.br/dataset/abc2d796-aa13-4ea0-b83a-13605ff98b87/resource/7ec4de7c-004c-4be1-88b1-80b70cf1250a/download/usf.csv'
    urlmaternidade = 'http://dados.recife.pe.gov.br/dataset/95b78bdd-f2bc-4f30-90bd-c3f311ba555f/resource/666c2a03-d18d-4520-8afc-6ae6a8d7d0ed/download/maternidades.csv'
    urlubs = 'http://dados.recife.pe.gov.br/dataset/39d3ab40-573d-42e7-b96e-0cc051695391/resource/54232db8-ed15-4f1f-90b0-2b5a20eef4cf/download/unidades-basica-saude.csv'
    hospital = entrada_de_dados(urlhospital)
    usf = entrada_de_dados(urlusf)
    maternidade = entrada_de_dados(urlmaternidade)
    ubs = entrada_de_dados(urlubs)
    hospital = converter_latitude_e_longitude_para_string(hospital)
    usf = converter_latitude_e_longitude_para_string(usf)
    maternidade = converter_latitude_e_longitude_para_string(maternidade)
    ubs = converter_latitude_e_longitude_para_string(ubs)
    hospital = substituir_ponto_por_virgula_longitude_e_latitude(hospital)
    usf = substituir_ponto_por_virgula_longitude_e_latitude(usf)
    maternidade = substituir_ponto_por_virgula_longitude_e_latitude(maternidade)
    ubs = substituir_ponto_por_virgula_longitude_e_latitude(ubs)
    hospital = usar_title_para_deixar_primeira_letra_como_maiuscula(hospital)
    usf = usar_title_para_deixar_primeira_letra_como_maiuscula(usf)
    maternidade = usar_title_para_deixar_primeira_letra_como_maiuscula(maternidade)
    ubs = usar_title_para_deixar_primeira_letra_como_maiuscula(ubs)
    hospital = criar_a_coluna_opcao(hospital, 'Hospital')
    usf = criar_a_coluna_opcao(usf, 'USF')
    maternidade = criar_a_coluna_opcao(maternidade, 'Maternidade')
    ubs = criar_a_coluna_opcao(ubs, 'UBS')
    hospital = criar_um_novo_DataFrame_com_as_colunas_desejadas_e_renomeando_as(hospital)
    usf = criar_um_novo_DataFrame_com_as_colunas_desejadas_e_renomeando_as(usf)
    maternidade = criar_um_novo_DataFrame_com_as_colunas_desejadas_e_renomeando_as(maternidade)
    ubs = criar_um_novo_DataFrame_com_as_colunas_desejadas_e_renomeando_as(ubs)
    dados = concatenar_DataFrames(hospital, usf, maternidade, ubs)
    dados =  Aplicar_capitalize_a_coluna_como_usar(dados)
    dados = criar_a_coluna_Regiao(dados)
    dados = aplicando_capitalize_no_nome_das_colunas(dados)
    dados['Latitude'] = converter_para_float_seguro(dados['Latitude'])
    dados['Longitude'] = converter_para_float_seguro(dados['Longitude'])
    dados = retirando_os_sinais_coluna_especialidade(dados)
    return dados
    #salvar_o_DataFrame_no_arquivo_CSV_com_codificação_UTF_8_para_subir_para_o_BI(dados)


df = main()

if __name__ == '__main__':
    main()
