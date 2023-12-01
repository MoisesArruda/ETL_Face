"""Pacote de transformação."""
import csv
import glob
import os

import pandas as pd

from extract import definir_caminhos
from load import conferir_arquivos_nao_enviados_1m, conferir_arquivos_nao_enviados_30m

caminhos = definir_caminhos()
print(caminhos)
# Definindo constantes globais
origem, staging, destino = definir_caminhos()

# Obter a lista de arquivos DAT na pasta raiz
arquivos_dat_1m = conferir_arquivos_nao_enviados_1m()
arquivos_dat_30m = conferir_arquivos_nao_enviados_30m()
"""Pacote de transformação."""
import glob
import os

import pandas as pd

from extract import definir_caminhos, verify_dat 
from load import conferir_arquivos_nao_enviados_1m, conferir_arquivos_nao_enviados_30m, enviar_arquivos_1m_para_staging, enviar_arquivos_30m_para_staging

# Armazenando a tupla retornada pela função
caminhos = definir_caminhos()
origem, staging, destino = caminhos

# Modificar para obter os arquivos da pasta origem
arquivos = verify_dat(staging)

# Obter a lista de arquivos DAT na pasta raiz
arquivos_dat_1m = conferir_arquivos_nao_enviados_1m()
arquivos_dat_30m = conferir_arquivos_nao_enviados_30m()


def detectar_separador(arquivo):
    """
    Possui a finalidade de detectar o tipo de separador presente no arquivo original
    """
    with open(arquivo,'r', encoding='utf-8') as file:
        # Leitura dos primeiros 1024 bytes para detectar o separador
        conteudo = file.read(1024)
        if ';' in conteudo:
            return ';'
        elif ',' in conteudo:
            return ','
        else:
            # Use '\t' como separador padrão se nenhum for detectado
            return '\t'


def criar_DataFrame(arquivos, pasta):

    dfs = []
    for arquivo in arquivos:
        caminho_completo = os.path.join(pasta, arquivo)
        separador = detectar_separador(caminho_completo)
        df = pd.read_csv(caminho_completo, sep=separador, skiprows=[0, 2, 3])
        dfs.append(df)
        # Gerando o df_final sem duplicatas

    df_final = pd.concat(dfs, ignore_index=True)
    df_final.head()

    return df_final


def criar_arquivo_csv(pasta, nome_arquivo):

    caminho_csv = f'{pasta}/{nome_arquivo}.csv'
    with open(caminho_csv,'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
    return caminho_csv


def criar_arquivo_csv(pasta, nome_arquivo):

    caminho_csv = f'{pasta}/{nome_arquivo}.csv'
    with open(caminho_csv,'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
    return caminho_csv


def gerar_arquivo_csv(df, caminho_csv):

    df_sem_duplicatas = df.drop_duplicates()

    # Ordenando o DF pela coluna Record e resetar o indice
    df_sem_duplicatas = df_sem_duplicatas.sort_values(by='RECORD').reset_index(drop=True)

    # Use o método to_csv para salvar o DataFrame em um arquivo CSV
    pasta_destino = os.path.dirname(caminho_csv)
    os.makedirs(pasta_destino, exist_ok=True)
    
    df_sem_duplicatas.to_csv(caminho_csv,sep=',',index=False)


df_final = criar_DataFrame(arquivos_dat_1m, staging)
nome_csv = 'csv_1m'
criar_csv = criar_arquivo_csv(destino,nome_csv)
gerar_csv = gerar_arquivo_csv(df_final, criar_csv)

df_final = criar_DataFrame(arquivos_dat_30m, staging)
nome_csv = 'csv_30m'
criar_csv = criar_arquivo_csv(destino,nome_csv)
gerar_csv = gerar_arquivo_csv(df_final, criar_csv)


try:
    qntd_enviada_1m = enviar_arquivos_1m_para_staging(destino)
    print(f'Foi realizado o envio de {len(qntd_enviada_1m)} arquivos')
except (FileNotFoundError, ValueError) as e:
    print(e)


try:
    qntd_enviada_30m = enviar_arquivos_30m_para_staging(destino)
    print(f'Foi realizado o envio de {len(qntd_enviada_30m)} arquivos')
except (FileNotFoundError, ValueError) as e:
    print(e)