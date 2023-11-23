"""Pacote de carregamento."""
# Acessa o sistema operacional
import glob

# Irá retornar uma lista de arquivos
import os

# Manipulação de arquivos e diretórios
import shutil

from extract import definindo_arquivos_dat, definir_caminhos, verify_dat

# Definindo constantes globais
origem, staging, destino = definir_caminhos()

# Modificar para obter os arquivos da pasta origem
arquivos = verify_dat()


def conferir_arquivos_nao_enviados():
    """
    Este trecho tem o objetivo de verificar quais arquivos ainda
    não foram enviados para a pasta destino
    """

    arquivo_1m_apenas_origem = []

    quantidade_30m, quantidade_1m = definindo_arquivos_dat()

    # Loop que vai iterar sobre os arquivos 1m
    for arquivo in quantidade_1m:
        # Apenas o nome do arquivo, que não está na pasta 1m do drive
        if os.path.basename(arquivo) not in [
            os.path.basename(x) for x in destino
        ]:
            # Adicionar o nome do arquivo na lista
            arquivo_1m_apenas_origem.append(arquivo)

    # Retornar a quantidade de arquivo
    print(f'Arquivos de 1 minuto: {len(arquivo_1m_apenas_origem)}')
    return arquivo_1m_apenas_origem


arquivo_1m_apenas_origem = conferir_arquivos_nao_enviados()
print(arquivo_1m_apenas_origem)


def enviar_arquivos_para_staging():
    """
    Deve enviar os arquivos ainda não enviados da pasta Origem
    para a pasta staging
    """
    qntd_enviada = []

    # Loop para iterar os arquivos 30m que estão apenas no One
    for arquivos in arquivo_1m_apenas_origem:
        # Buscar o caminho desse arquivo no One Drive
        caminho_arquivo_origem = os.path.join(origem, arquivos)
        # Buscar a pasta Staging no GDrive
        caminho_arquivo_staging = os.path.join(staging, arquivos)
        # Copiar o arquivo de uma pasta para outra
        shutil.copy(caminho_arquivo_origem, caminho_arquivo_staging)
        # Para cada arquivo 1 mensagem
        print(f'Arquivo {arquivos} copiado para a pasta Staging')
        qntd_enviada.append(+1)

    return qntd_enviada


try:
    qntd_enviada = enviar_arquivos_para_staging()
    print(f'Foi realizado o envio de {len(qntd_enviada)} arquivos')
except (FileNotFoundError, ValueError) as e:
    print(e)
