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
    pasta_One = r'Caminho\One'
    # Onde esses arquivos serão armazenados
    pasta_Staging = r'Caminho\Staging'
    # Arquivos de 1 minuto
    pasta_Gdrive_1m = r'Caminho\1m'

    return pasta_One, pasta_Staging, pasta_Gdrive_1m


# Armazenando a tupla retornada pela função
caminhos = definir_caminhos()
# Nessa linha de código acontece o desempacotamento dos valores da tupla
origem, staging, destino = caminhos

print('Estes são os caminhos de pasta')
print(f'Pasta One: {origem}')
print(f'Pasta Staging: {staging}')
print(f'Pasta_Gdrive_1m: {destino}')