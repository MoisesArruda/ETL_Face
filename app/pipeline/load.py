"""Pacote de carregamento."""

from app.pipeline.extract import verify_dat

def definindo_arquivos_dat():
    """
    Está sendo definido o nome dos arquivos de 1 minuto
    """
    METEO_1M = "CR6_T1_meteo_"
    # Lista para armazenar a quantidade de arquivos 1m no One Drive
    # Variável para armazenar parte do nome do arquivo
    METEO_1M = "meteoMedia30"
    quantidade_1m = []
    # Lista para armazenar a quantidade de arquivos 30m no One Drive
    quantidade_30m = []

    # Loop para iterar em cada arquivo na pasta
    for arquivo in verify_dat(origem):
        if METEO_1M in nome_arquivos:
            quantidade_30m.append(nome_arquivos)
        elif METEO_1M in nome_arquivos:
            quantidade_1m.append(nome_arquivo) 
        else:
            print('Nenhum arquivo na pasta')

    return len(quantidade_30m), len(quantidade_1m)
