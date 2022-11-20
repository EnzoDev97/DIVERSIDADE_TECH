### Criando vetores de zeros

n = 10
lista_zeros = [0] * n
print('----\033[36m{}\033[0m----  TAMANHO: {}'.format(lista_zeros,len(lista_zeros)))
print(type(lista_zeros))
print('\n')   
 
import numpy as np
#  Utilizando o numpy

zeros = np.zeros(n)
print('----\033[33m{}\033[0m----  TAMANHO: {}'.format(zeros,len(zeros)))
print(type(zeros))
print('\n')

uns= np.ones(n)
print('----\033[32m{}\033[0m----  TAMANHO: {}'.format(uns,len(uns)))
print(type(uns))