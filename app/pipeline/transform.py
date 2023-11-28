"""Pacote de transformação."""
import glob
import os

import pandas as pd

from extract import definir_caminhos
from load import conferir_arquivos_nao_enviados_1m, conferir_arquivos_nao_enviados_30m

caminhos = definir_caminhos()
print(caminhos)
# Definindo constantes globais
origem, staging, destino = definir_caminhos()

# Obter a lista de arquivos DAT na pasta raiz
arquivos_dat_1m = conferir_arquivos_nao_enviados_1m()
arquivos_dat_30m = conferir_arquivos_nao_enviados_30m()
