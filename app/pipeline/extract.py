"""Pacote de extração."""
# Acessa o sistema operacional
import glob

# Irá retornar uma lista de arquivos
import os

# Manipulação de arquivos e diretórios
import shutil

import pandas as pd


def definir_caminhos():
    """
    Função responsável por definir o caminho dos diretórios.
    Return:
        tuple: Uma tupla contendo os caminhos para a pasta Origem, Staging e Destino.
    Example:
        >>> caminhos = definir_caminhos()
        >>> pasta_One, pasta_Staging, pasta_Destino = caminhos
        >>> print(f'Pasta One: {pasta_One}')
        >>> print(f'Pasta Staging: {pasta_Staging}')
        >>> print(f'Pasta Destino: {pasta_Destino}')
    Note:
        Certifique-se de que os caminhos estejam corretamente
        configurados antes de chamar esta função.
    """

     # Onde os arquivos estão sendo disponibilizados
    ORIGEM = '/mnt/c/Users/BlueShift/OneDrive/AmazonFACE'
    # Onde esses arquivos serão armazenados
    STAGING = '/mnt/c/Users/BlueShift/Documents/AFace/staging'
    # Arquivos de 1 minuto
    DESTINO = '/mnt/c/Users/BlueShift/Documents/AFace/1m'

    return ORIGEM, STAGING, DESTINO

# Armazenando a tupla retornada pela função
caminhos = definir_caminhos()
# Nessa linha de código acontece o desempacotamento dos valores da tupla
origem, staging, destino = caminhos

print('Estes são os caminhos de pasta')
print(f'Pasta One: {origem}')
print(f'Pasta Staging: {staging}')
print(f'Pasta Destino: {destino}')


def verify_dat():
    """
    Verifica se há arquivos .dat presentes na pasta origem.
    Parameters:
        origem(str): Caminho da pasta a ser verificada.
    Return:
        bool: True se há arquivos .dat, False se a pasta está vazia
    Raises:
        ValueError: Se não existirem arquivos na pasta
    type: input_folder: str
    """
    if not os.path.exists(origem):
        raise FileNotFoundError(f'A pasta {origem} não existe')

    files_origem = glob.glob(f'{origem}/*.dat')
    if not files_origem:
        raise ValueError('Erro: Não há arquivos .dat na pasta')
    else:
        # Para cada arquivo na pasta, retornar apenas o nome sem o caminho completo   
        nomes_arquivos = [os.path.basename(arquivo) for arquivo in files_origem]

    return nomes_arquivos

try:
    arquivos = verify_dat()
    print(arquivos)
except (FileNotFoundError, ValueError) as e:
    print(e)


def definindo_arquivos_dat():
    """
    Está sendo definido o nome dos arquivos de 1 minuto
    """
    # Variável para armazenar parte do nome do arquivo
    METEO_1M = "CR6_T1_meteo_"
    # Lista para armazenar a quantidade de arquivos 1m no One Drive
    METEO_30M = "meteoMedia30"
    # Lista para armazenar a quantidade de arquivos 1m no One Drive
    quantidade_1m = []
    # Lista para armazenar a quantidade de arquivos 30m no One Drive
    quantidade_30m = []

    # Loop para iterar em cada arquivo na pasta
    for arquivo in arquivos:
        if METEO_30M in arquivo:
            quantidade_30m.append(arquivo)
        elif METEO_1M in arquivo:
            quantidade_1m.append(arquivo) 
        else:
            print('Nenhum arquivo na pasta')

    return quantidade_30m, quantidade_1m

resultados_30m, resultados_1m = definindo_arquivos_dat()
print(f"Quantidade de arquivos 30m: {len(resultados_30m)}")
print(f"Quantidade de arquivos 1m: {len(resultados_1m)}")