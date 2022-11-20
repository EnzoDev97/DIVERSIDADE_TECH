#10 - Crie outro array aleatório, porém, dessa vez, com 25 elementos inteiros, no intervalo [50, 100). 
# Em seguida, converta esse array em uma matriz 5 x 5.

import math
import numpy as np
from random import randint


mtx = np.array([np.arange(6), np.arange(10, 16), np.arange(20, 26), np.arange(30, 36), np.arange(40, 46), np.arange(50, 56)])

vermelho = mtx[0,3:5]
print('\033[31m {}\033[m'.format(vermelho))
print('-'*100,'\n')

azul = mtx[:,2]
print('\033[36m {}\033[m'.format(azul))
print('-'*100,'\n')

roxo = mtx[2::2,::2]
print('\033[35m {}\033[m'.format(roxo))
print('-'*100,'\n')

verde = mtx[4:,4:]

print('\033[32m {}\033[m'.format(verde ))
print('-'*100,'\n')

np.random.seed(0)
n_linhas = 5
n_cols = 5
matrix_5x5  = np.random.randint(50, 100, (n_linhas, n_cols))
print('\033[34m {}\033[m'.format(matrix_5x5))
print('-'*100,'\n')

# OUTRA FORMA
matriz = np.linspace(50, 100, 25).reshape(5, 5)
print(matriz)
print('-'*100,'\n')
# OUTRA FORMA

matri_z = np.random.randint(50, 100, 25).reshape(5, 5)
print(matri_z)