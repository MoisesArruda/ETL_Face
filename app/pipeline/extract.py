"""Pacote de extração."""
# Acessa o sistema operacional
import glob

# Irá retornar uma lista de arquivos
import os

# Manipulação de arquivos e diretórios
import shutil
from typing import List

import pandas as pd


def definir_caminhos(ORIGEM=None, STAGING=None, DESTINO=None):
    """
    Define os caminhos dos diretórios.

    Args:
        ORIGEM (str): Caminho para o diretório de origem. Padrão é None.
        STAGING (str): Caminho para o diretório de staging. Padrão é None.
        DESTINO (str): Caminho para o diretório de destino. Padrão é None.

    Return:
        tuple: Uma tupla contendo os caminhos para a pasta Origem, Staging e Destino.

    Example:
        >>> caminhos = definir_caminhos()
        >>> pasta_Origem, pasta_Staging, pasta_Destino = caminhos
        >>> print(f'Pasta Origem: {Origem}')
        >>> print(f'Pasta Staging: {Staging}')
        >>> print(f'Pasta Destino: {Destino}')

    Note:
        Certifique-se de que os caminhos estejam corretamente
        configurados antes de chamar esta função. Isso pode ser feito
        definindo os caminhos externamente ou passando-os como argumentos.
    """

    # Onde os arquivos estão sendo disponibilizados
    ORIGEM = ORIGEM or '/mnt/c/Users/BlueShift/OneDrive/AmazonFACE'
    # Onde esses arquivos serão armazenados temporariamente para gerar o arquivo CSV
    STAGING = STAGING or '/mnt/c/Users/BlueShift/Documents/AFace/staging'
    # Destino final dos arquivos
    DESTINO = DESTINO or '/mnt/c/Users/BlueShift/Documents/AFace/1m'

    return ORIGEM, STAGING, DESTINO


# Armazenando a tupla retornada pela função
caminhos = definir_caminhos('/mnt/c/Users/BlueShift/OneDrive/AmazonFACE')
# print(caminhos)
# Nessa linha de código acontece o desempacotamento dos valores da tupla
origem, staging, destino = caminhos

print('Estes são os caminhos de pasta')
print(f'Pasta One: {origem}')
print(f'Pasta Staging: {staging}')
print(f'Pasta Destino: {destino}')


def verify_dat(folder: str) -> List[str]:
    """
    Verifica se há arquivos .dat presentes na pasta origem.

    Args:
        folder(str): Caminho da pasta a ser verificada.

    Return:
        nomes_arquivos (list): Uma lista contendo os nomes dos arquivos da pasta.

    Raises:
        FileNotFoundError: Se a pasta não existir.
        ValueError: Se não existirem arquivos .dat na pasta.
    """
    try:
        if not os.path.exists(folder):
            raise FileNotFoundError(f'A pasta {folder} não existe')

        files_folder = glob.glob(os.path.join(folder, '*.dat'))
        if not files_folder:
            raise ValueError('Erro: Não há arquivos .dat na pasta')
        else:
            # Para cada arquivo na pasta, retornar apenas o nome sem o caminho completo
            nomes_arquivos = [
                os.path.basename(arquivo) for arquivo in files_folder
            ]

        return nomes_arquivos

    except (FileNotFoundError, ValueError) as e:
        raise


try:
    arquivos = verify_dat(origem)
    # print(arquivos)
except (FileNotFoundError, ValueError) as e:
    print(e)


def definindo_arquivos_dat_1m():
    """
    Será retornado uma lista com o nome dos arquivos de 1 minuto

    Return:
        quantidade_1m (list): Lista com os arquivos de 1 minuto presentes na pasta
    """
    # Variável para armazenar parte do nome do arquivo
    METEO_1M = 'CR6_T1_meteo_'
    # Lista para armazenar a quantidade de arquivos 1m no One Drive
    METEO_30M = 'meteoMedia30'
    # Lista para armazenar a quantidade de arquivos 1m no One Drive
    quantidade_1m = []

    # Loop para iterar em cada arquivo na pasta
    for arquivo in arquivos:
        if METEO_30M in arquivo:
            pass
        elif METEO_1M in arquivo:
            quantidade_1m.append(arquivo)

    # Verificar se algum arquivo atende às condições
    if not quantidade_1m:
        raise ValueError('Nenhum arquivo de 1 minuto encontrado na pasta.')

    return quantidade_1m


try:
    resultados_1m = definindo_arquivos_dat_1m()
    print(f'Quantidade de arquivos 1m: {len(resultados_1m)}')
except ValueError as e:
    print(e)


def definindo_arquivos_dat_30m():
    """
    Define os nomes dos arquivos de 30 minutos na pasta.

     Returns:
        quantidade_30m (List[str]): Lista de arquivos de 30 minutos na pasta.
    """
    # Lista para armazenar a quantidade de arquivos 1m no One Drive
    METEO_30M = 'meteoMedia30'
    # Variável para armazenar parte do nome do arquivo
    METEO_1M = 'CR6_T1_meteo_'
    # Lista para armazenar a quantidade de arquivos 30m no One Drive
    quantidade_30m = []

    # Loop para iterar em cada arquivo na pasta
    for arquivo in arquivos:
        if METEO_30M in arquivo:
            quantidade_30m.append(arquivo)
        elif METEO_1M in arquivo:
            pass

    if not quantidade_30m:
        raise ValueError('Nenhum arquivo de 30 minutos encontrado na pasta.')

    return quantidade_30m


try:
    resultados_30m = definindo_arquivos_dat_30m()
    print(f'Quantidade de arquivos 30m: {len(resultados_30m)}')
except ValueError as e:
    print(e)
