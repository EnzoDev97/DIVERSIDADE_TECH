import numpy as np


# Linha para permitir a reprodutibilidade do exercício
np.random.seed(0)
n_linhas = 10
n_cols = 8
mat = np.random.randint(0, 10, (n_linhas, n_cols))
print('Shape', mat.shape)
print('-'*32)
print(mat)
print('-'*32)
col_impar = list(filter(lambda x: x%2 != 0, range(n_cols)))
linha_par = list(filter(lambda x: x%2 == 0, range(n_linhas)))
print('col_impar', col_impar)
print('linha_par', linha_par)
print('-'*32)

# Quando queremos filtrar por duas listas
# Devemos fazer de forma sequencial
filtrando_linhas = mat[linha_par, :]
filtrando_colunas = filtrando_linhas[:, col_impar] 