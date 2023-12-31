"""Pacote de carregamento."""
# Acessa o sistema operacional
import glob

# Irá retornar uma lista de arquivos
import os

# Manipulação de arquivos e diretórios
import shutil

from extract import (
    definindo_arquivos_dat_1m,
    definindo_arquivos_dat_30m,
    definir_caminhos,
    verify_dat,
)

from typing import List

# Definindo constantes globais
origem, staging, destino = definir_caminhos()

# Modificar para obter os arquivos da pasta origem
arquivos = verify_dat(origem)


def conferir_arquivos_nao_enviados_1m() -> List[str]:
    """
    Verifica quais arquivos de 1 minuto ainda não foram enviados para a pasta de destino.

    Return:
       arquivo_1m_apenas_origem (List[str]): Lista com arquivos de 1 minuto que ainda não foram enviados para a pasta destino.
    """

    arquivo_1m_apenas_origem = []

    quantidade_1m = definindo_arquivos_dat_1m()

    # Loop que vai iterar sobre os arquivos 1m
    for arquivo in quantidade_1m:
        # Apenas o nome do arquivo, que não está na pasta destino
        if os.path.basename(arquivo) not in [
            os.path.basename(x) for x in destino
        ]:
            # Adicionar o nome do arquivo na lista
            arquivo_1m_apenas_origem.append(arquivo)

    return arquivo_1m_apenas_origem


arquivo_1m_apenas_origem = conferir_arquivos_nao_enviados_1m()
# Retornar a quantidade de arquivos
print(f'Arquivos de 1 minuto: {len(arquivo_1m_apenas_origem)}')
# print(arquivo_1m_apenas_origem)


def conferir_arquivos_nao_enviados_30m():
    """
    Verifica quais arquivos de 30 minutos ainda não foram enviados para a pasta de destino.

    Return:
    arquivo_30m_apenas_origem (list): Lista com arquivos de 30 minutos que ainda não foram enviados para a pasta de destino.
    """

    arquivo_30m_apenas_origem = []

    quantidade_30m = definindo_arquivos_dat_30m()

    # Loop que vai iterar sobre os arquivos 1m
    for arquivo in quantidade_30m:
        # Apenas o nome do arquivo, que não está na pasta 1m do drive
        if os.path.basename(arquivo) not in [
            os.path.basename(x) for x in destino
        ]:
            # Adicionar o nome do arquivo na lista
            arquivo_30m_apenas_origem.append(arquivo)

    return arquivo_30m_apenas_origem


arquivo_30m_apenas_origem = conferir_arquivos_nao_enviados_30m()
# Retornar a quantidade de arquivos
print(f'Arquivos de 30 minutos: {len(arquivo_30m_apenas_origem)}')
# print(arquivo_30m_apenas_origem)


def enviar_arquivos_1m(folder: str) -> List[str]:
    """
    Esta função envia os arquivos que ainda não foram enviados da pasta 'Origem' para a pasta 'staging'.

    Args:
        folder (str): O caminho da pasta 'staging'.

    Returns:
        List[str]: Uma lista com os nomes dos arquivos que foram enviados para a pasta 'staging'.
    """
    qntd_enviada_1m = []

    # Loop para iterar os arquivos 1m que estão apenas no One
    for arquivos in arquivo_1m_apenas_origem:
        # Buscar o caminho desse arquivo no One Drive
        caminho_arquivo_origem = os.path.join(origem, arquivos)
        # Buscar a pasta Staging no GDrive
        caminho_arquivo_staging = os.path.join(folder, arquivos)
        # Copiar o arquivo de uma pasta para outra
        shutil.copy(caminho_arquivo_origem, caminho_arquivo_staging)
        # Para cada arquivo 1 mensagem
        print(f'Arquivo {arquivos} copiado para a pasta {folder}')
        qntd_enviada_1m.append(+1)

    return qntd_enviada_1m


try:
    qntd_enviada_1m = enviar_arquivos_1m(staging)
    print(f'Foi realizado o envio de {len(qntd_enviada_1m)} arquivos')
except (FileNotFoundError, ValueError) as e:
    print(e)


def enviar_arquivos_30m(folder: str):
    """
    Copia os arquivos da pasta 'Origem' para a pasta 'staging'.

    Args:
        folder (str): O caminho para a pasta 'staging'.

    Returns:
        qntd_enviada_30m (list): Uma lista com os nomes dos arquivos que foram copiados para a pasta 'staging'.
    """
    qntd_enviada_30m = []

    # Loop para iterar os arquivos 30m que estão apenas no One
    for arquivos in arquivo_30m_apenas_origem:
        # Buscar o caminho desse arquivo no One Drive
        caminho_arquivo_origem = os.path.join(origem, arquivos)
        # Buscar a pasta Staging no GDrive
        caminho_arquivo_staging = os.path.join(folder, arquivos)
        # Copiar o arquivo de uma pasta para outra
        shutil.copy(caminho_arquivo_origem, caminho_arquivo_staging)
        # Para cada arquivo 1 mensagem
        print(f'Arquivo {arquivos} copiado para a pasta {folder}')
        qntd_enviada_30m.append(+1)

    return qntd_enviada_30m


try:
    qntd_enviada_30m = enviar_arquivos_30m(staging)
    print(f'Foi realizado o envio de {len(qntd_enviada_30m)} arquivos')
except (FileNotFoundError, ValueError) as e:
    print(e)



def excluir_arquivos_enviados_1m(folder=staging) -> List[str]:
    """
    Os arquivos que foram enviados para a pasta destino serão excluidos desta pasta temporária
    
    Args:
        folder: O caminho da pasta 'staging'.

    Returns:
        qntd_excluida_1m (list): Uma lista com os nomes dos arquivos que foram excluidos da pasta 'staging'.
    """
    qntd_excluida_1m = []
    for arquivo in qntd_enviada_1m:
        caminho_arquivo = os.path.join(staging, arquivo)
        os.remove(caminho_arquivo)
        # print(f'Arquivo {arquivo} excluído')
        qntd_excluida_1m.append(+1)

    return qntd_excluida_1m


def excluir_arquivos_enviados_30m(folder=staging) -> List[str]:
    """
    Os arquivos que foram enviados para a pasta destino serão excluidos desta pasta temporária
    
    Args:
        folder: O caminho da pasta 'staging'.

    Returns:
        qntd_excluida_30m (list): Uma lista com os nomes dos arquivos que foram excluidos da pasta 'staging'.
    """
    qntd_excluida_30m = []
    for arquivo in qntd_enviada_30m:
        caminho_arquivo = os.path.join(staging, arquivo)
        os.remove(caminho_arquivo)
        # print(f'Arquivo {arquivo} excluído')
        qntd_excluida_30m.append(+1)

    return qntd_excluida_30m

