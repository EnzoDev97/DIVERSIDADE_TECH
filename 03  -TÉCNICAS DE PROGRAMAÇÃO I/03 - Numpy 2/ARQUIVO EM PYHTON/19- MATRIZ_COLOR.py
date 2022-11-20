
#11 - Construa a matriz ilustrada pela figura abaixo. Em seguida, obtenha os slices (fatiamentos) destacados em cada cor. 
# Em outras palavras, utilizando o conceito de slices, crie um novo array que contenha os dados destacados em vermelho, azul, roxo e verde.

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



print('MATRIX 1 ')
matrix_1 = np.arange(0, 6)
print('\033[34m {}\033[m'.format(matrix_1))
print('-'*100,'\n')

print('MATRIX 2 ')
matrix_2 = np.arange(10, 16)
print('\033[34m {}\033[m'.format(matrix_2))
print('-'*100,'\n')

print('MATRIX 3 ')
matrix_3 = np.arange(20, 26)
print('\033[34m {}\033[m'.format(matrix_3))
print('-'*100,'\n')


print('MATRIX 4 ')
matrix_4 = np.arange(30, 36)
print('\033[34m {}\033[m'.format(matrix_4))
print('-'*100,'\n')

print('MATRIX 5 ')
matrix_5 = np.arange(40, 46)
print('\033[34m {}\033[m'.format(matrix_5))

