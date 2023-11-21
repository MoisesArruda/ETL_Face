"""Pacote de carregamento."""

from extract import verify_dat,definir_caminhos

# Definindo constantes globais
# ORIGEM, STAGING, DESTINO = definir_caminhos()


def conferir_arquivos_nao_enviados(origem,destino):
    """
    Este trecho tem o objetivo de verificar quais arquivos ainda
    não foram enviados para a pasta destino
    """
    arquivo_1m_apenas_origem = []
    
    quantidade_1m = definindo_arquivos_dat()
    

    # Loop que vai iterar sobre os arquivos 1m
    for arquivo in quantidade_1m:
        # Apenas o nome do arquivo, que não está na pasta 1m do drive
         if os.path.basename(arquivo) not in [os.path.basename(x) for x in destino]:
         # Adicionar o nome do arquivo na lista
            arquivo_1m_apenas_origem.append(arquivo)

    # Retornar a quantidade de arquivo
    print(f'Arquivos de 1 minuto {len(arquivo_1m_apenas_origem)}')
    return arquivo_1m_apenas_origem

def enviar_arquivos_para_staging(origem,staging):
    """
    Deve enviar os arquivos ainda não enviados da pasta Origem
    para a pasta staging"""
    
    arquivo_1m_apenas_origem = conferir_arquivos_nao_enviados()
    
    # Loop para iterar os arquivos 30m que estão apenas no One
    for nome_arquivo in arquivo_1m_apenas_origem:
        # Buscar o caminho desse arquivo no One Drive
        caminho_arquivo_origem = f'{ORIGEM}\\{nome_arquivo}'
        # Buscar a pasta Staging no GDrive
        caminho_arquivo_staging = f'{STAGING}\\{nome_arquivo}'
        # Copiar o arquivo de uma pasta para outra
        shutil.copy(caminho_arquivo_origem, caminho_arquivo_staging)
        # Para cada arquivo 1 mensagem
        print (f'Arquivo {nome_arquivo} copiado para a pasta Staging')
        qntd_enviada += 1

        print(len(qntd_enviada))

