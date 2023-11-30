"""
Criando pacote de testes
"""

# Criação da função que aceita os dois parâmetros
def test_all_col_exists(df_1, cols):
    # Compreensão de lista que percorre cada elemento da lista
    missing_cols = [col for col in cols if col not in df_1.columns]

    # O print irá trazer as colunas que não estão presentes no DF
    if missing_cols:
        print(
            f'A seguintes colunas não foram encontradas no {df_1}: {missing_cols}'
        )
    else:
        print('Todas as colunas foram encontradas no DF')


# Colunas para verificação
colunas_verificadas = [
    'TIMESTAMP',
    'RECORD',
    'WindSpeed_1',
    'WindDir_1',
    'WindSpeed_2',
    'WindDir_2',
    'WindSpeed_3',
    'WindDir_3',
    'WindSpeed_4',
    'WindDir_4',
    'temp_1_Avg',
    'temp_2_Avg',
    'temp_3_Avg',
    'temp_4_Avg',
    'humid_1_Avg',
    'humid_2_Avg',
    'humid_3_Avg',
    'humid_4_Avg',
    'par1_in_Avg',
    'par2_in_Avg',
    'par3_in_Avg',
    'par4_in_Avg',
    'chuva_Tot',
    'SBTempC_1_Avg',
    'TargTempC_1_Avg',
    'SBTempC_2_Avg',
    'TargTempC_2_Avg',
    'SBTempC_3_Avg',
    'TargTempC_3_Avg',
    'SBTempC_4_Avg',
    'TargTempC_4_Avg',
    'pressao_Avg',
    'rad_total_Avg',
    'rad_diff_Avg',
]

# Variável para armazenar parte do nome do arquivo
meteo_30m = 'meteoMedia30'
# Lista dos arquivos verificados para ser utilizada posteriormente
arquivos_verificados = []

for arquivo in arquivos_staging:
    # Retornando apenas o nome do arquivo sem o caminho da pasta
    nome_arquivo = os.path.basename(arquivo)

    if meteo_30m in nome_arquivo:
        df_1 = pd.read_csv(arquivo, sep=',', skiprows=[0, 2, 3])   # header=1)
        # Chama a função para verificar a presença das colunas
        test_all_col_exists(df_1, colunas_verificadas)
        arquivos_verificados.append(nome_arquivo)
print(f'{len(arquivos_verificados)} arquivos foram verificados')
