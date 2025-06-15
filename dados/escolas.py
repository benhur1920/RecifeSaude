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
    return pd.to_numeric(coluna.str.replace(',', '.'), errors='coerce')



def usar_title_para_deixar_primeira_letra_como_maiuscula(df):
    df = df.apply(lambda x: x.str.title() if x.dtype == "object" else x)
    return df



def salvar_o_DataFrame_no_arquivo_CSV_com_codificação_UTF_8_para_subir_para_o_BI(dados):
    dados.to_csv('ServicosSaude.csv', sep=';',encoding='utf-8-sig', index=False)



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


def main():
    url = 'http://dados.recife.pe.gov.br/dataset/4d3a3b39-9ea9-46ed-bf21-a2670de519c1/resource/7c613836-9edd-4c0f-bc72-495008dd29c3/download/info_escolas_2023_27122023.csv'
    dados = entrada_de_dados(url)
    dados = converter_latitude_e_longitude_para_string(dados)
    dados = substituir_ponto_por_virgula_longitude_e_latitude(dados)
    dados['latitude'] = converter_para_float_seguro(dados['latitude'])
    dados['longitude'] = converter_para_float_seguro(dados['longitude'])
    dados = usar_title_para_deixar_primeira_letra_como_maiuscula(dados)
    dados = criar_a_coluna_Regiao(dados)
    dados = aplicando_capitalize_no_nome_das_colunas(dados)
    #dados = salvar_o_DataFrame_no_arquivo_CSV_com_codificação_UTF_8_para_subir_para_o_BI(dados)
    return dados
    #salvar_o_DataFrame_no_arquivo_CSV_com_codificação_UTF_8_para_subir_para_o_BI(dados)


df = main()

if __name__ == '__main__':
    main()
