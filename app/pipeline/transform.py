"""Pacote de transformação."""

import glob
import os

import pandas as pd
from extract import definir_caminhos, verify_dat
from load import (
    conferir_arquivos_nao_enviados_1m,
    conferir_arquivos_nao_enviados_30m,
)

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
    with open(arquivo, 'r') as file:
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


def gerar_arquivo_csv(df, caminho_csv):

    df_sem_duplicatas = df.drop_duplicates()

    # Ordenando o DF pela coluna Record
    df_sem_duplicatas = df_sem_duplicatas.sort_values(by='RECORD')
    # Resetar o indice
    df_sem_duplicatas = df_sem_duplicatas.reset_index(drop=True)

    # Use o método to_csv para salvar o DataFrame em um arquivo CSV
    df_sem_duplicatas.to_csv(caminho_csv, sep=',', index=False)


df_final = criar_DataFrame(arquivos_dat_1m, staging)
df_final.head()
caminho_csv = os.path.join(destino, 'csv_1m.csv')
gerar_csv = gerar_arquivo_csv(df_final, caminho_csv)