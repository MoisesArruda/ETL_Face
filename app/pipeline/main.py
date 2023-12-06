"""Pacote principal de execução"""

from extract import definir_caminhos, verify_dat
from load import (
    conferir_arquivos_nao_enviados_1m,
    conferir_arquivos_nao_enviados_30m,
    enviar_arquivos_1m_para_staging,
    enviar_arquivos_30m_para_staging,
)
from transform import criar_arquivo_csv, criar_DataFrame, gerar_arquivo_csv


def main() -> None:
    """
    Função principal que orquestra a execução do programa.
    """

    # Definir caminhos dos arquivos
    origem, staging, destino = definir_caminhos()

    # Verificar e processar arquivos DAT
    arquivos = verify_dat(staging)

    # Pacote de Carregamento

    # Enviar arquivos para o Staging
    try:
        qntd_enviada_1m = enviar_arquivos_1m_para_staging(staging)
        print(f'Foi realizado o envio de {len(qntd_enviada_1m)} arquivos')
    except (FileNotFoundError, ValueError) as e:
        print(e)

    try:
        qntd_enviada_30m = enviar_arquivos_30m_para_staging(staging)
        print(f'Foi realizado o envio de {len(qntd_enviada_30m)} arquivos')
    except (FileNotFoundError, ValueError) as e:
        print(e)

    # Processar e criar CSV para arquivos de 1 minuto
    arquivos_dat_1m = conferir_arquivos_nao_enviados_1m()
    df_1m = criar_DataFrame(arquivos_dat_1m, staging)
    nome_csv_1m = 'csv_1m'
    criar_csv_1m = criar_arquivo_csv(destino, nome_csv_1m)
    gerar_csv_1m = gerar_arquivo_csv(df_1m, criar_csv_1m)

    # Processar e criar CSV para arquivos de 30 minutos
    arquivos_dat_30m = conferir_arquivos_nao_enviados_30m()
    df_30m = criar_DataFrame(arquivos_dat_30m, staging)
    nome_csv_30m = 'csv_30m'
    criar_csv_30m = criar_arquivo_csv(destino, nome_csv_30m)
    gerar_csv_30m = gerar_arquivo_csv(df_30m, criar_csv_30m)

    print('Execução da função concluída')


if __name__ == '__main__':
    main()
