"""Pacote de carregamento."""

from extract import verify_dat,definir_caminhos

def definindo_arquivos_dat():
    """
    Está sendo definido o nome dos arquivos de 1 minuto
    """
    METEO_1M = "CR6_T1_meteo_"
    # Lista para armazenar a quantidade de arquivos 1m no One Drive
    # Variável para armazenar parte do nome do arquivo
    METEO_30M = "meteoMedia30"
    quantidade_1m = []
    # Lista para armazenar a quantidade de arquivos 30m no One Drive
    quantidade_30m = []

    origem, staging, destino = definir_caminhos()

    # Chamando verify_dat para obter a lista de nomes de arquivos
    nome_arquivos = verify_dat(origem)

    # Loop para iterar em cada arquivo na pasta
    for arquivo in nome_arquivos:
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