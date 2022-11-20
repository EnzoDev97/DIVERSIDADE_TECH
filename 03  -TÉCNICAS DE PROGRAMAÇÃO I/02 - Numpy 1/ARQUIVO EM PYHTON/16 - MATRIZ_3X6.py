#03 - Nosso próximo foco serão as matrizes. Faça o que se pede:

#a) Gere uma matriz (3,2) com números linearmente espaçados entre 0 e 100 e intervalos de 20, usando o np.linspace();

#b) Gere uma matriz aleatória (5,2) com números entre 0 e 100;

#c) Crie um array com as dimensões apropriadas que, quando multiplicado pela matriz do item a), devolva essa mesma matriz. Use o método np.matmul().


import numpy as np
import random
from random import randint 

np.random.seed(0)
n_linha = 3
n_col = 2
matrix_3x2  = np.random.randint(0, 100, (n_linha, n_col))
print('\033[35m  {}\033[m'.format(matrix_3x2))
print('-'*100,'\n')

#b) Gere uma matriz aleatória (5,2) com números entre 0 e 100;

print('MATRIX 5X2\n')
matrix_5x2 = np.random.randint(0,100,(5,2))
print('\033[31m{}\033[m'.format(matrix_5x2))
print('-'*100,'\n')


#c) Crie um array com as dimensões apropriadas que, quando multiplicado pela matriz do item a), 
#devolva essa mesma matriz. Use o método np.matmul().

np.random.seed(0)
n_linhas = 2
n_cols = 3
matrix_nova  = np.random.randint(0, 100, (n_linhas, n_cols))
print('\033[34m {}\033[m'.format(matrix_nova))
print('-'*100,'\n')

# APLICANDO A FUNÇÃO

matmult = np.matmul(matrix_3x2, matrix_nova)
print(matmult)

#OUTRO MÉTODO

import numpy as np

# a)
matriz = np.linspace(0, 100, 6).reshape(3, 2)
print(matriz)

# b)
matriz_aleatoria = np.random.randint(0, 101, size=(5, 2))
print(matriz_aleatoria)

# c)
array = np.identity(2)
print(array)
print(np.matmul(matriz, array))