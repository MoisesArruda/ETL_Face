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
        tuple: Uma tupla contendo os caminhos para a pasta One, Staging e Gdrive_1m.

    Example:
        >>> caminhos = definir_caminhos()
        >>> pasta_One, pasta_Staging, pasta_Gdrive_1m = caminhos
        >>> print(f'Pasta One: {pasta_One}')
        >>> print(f'Pasta Staging: {pasta_Staging}')
        >>> print(f'Pasta Gdrive 1m: {pasta_Gdrive_1m}')

    Note:
        Certifique-se de que os caminhos estejam corretamente
        configurados antes de chamar esta função.

    """
     # Onde os arquivos estão sendo disponibilizados
    pasta_One = '/mnt/c/Users/BlueShift/OneDrive/AmazonFACE'
    # Onde esses arquivos serão armazenados
    pasta_Staging = '/mnt/c/Users/BlueShift/Documents/AFace/staging'
    # Arquivos de 1 minuto
    pasta_Gdrive_1m = '/mnt/c/Users/BlueShift/Documents/AFace/1m'

    return pasta_One, pasta_Staging, pasta_Gdrive_1m


# Armazenando a tupla retornada pela função
caminhos = definir_caminhos()
# Nessa linha de código acontece o desempacotamento dos valores da tupla
origem, staging, destino = caminhos

print('Estes são os caminhos de pasta')
print(f'Pasta One: {origem}')
print(f'Pasta Staging: {staging}')
print(f'Pasta_Gdrive_1m: {destino}')


class NoDatFilesErros(Exception):
    """Exceção levantada quando não há arquivos .dat na pasta."""


def verify_dat(origem):
    """
    Verifica se há arquivos .dat presentes na pasta One_Drive.

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
        raise NoDatFilesErros(
            'A pasta {origem} não contém arquivos .dt'
        )   # Nenhum arquivo .dat encontrado na pasta
    else:
        # Para cada arquivo na pasta, me retornar apenas o nome sem o caminho completo
        nome_arquivos = [os.path.basename(arquivo) for arquivo in files_origem]
        print("Nomes de arquivos copiados")

        return nome_arquivos
