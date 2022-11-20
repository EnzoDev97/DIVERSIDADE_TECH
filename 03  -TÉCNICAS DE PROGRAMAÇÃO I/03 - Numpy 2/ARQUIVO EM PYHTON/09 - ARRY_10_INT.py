# 01 - Crie uma lista do Python que contenha 10 inteiros aleatórios (entre 0 e 100). 
# Em seguida, a partir da lista criada anteriormente, crie um array do Numpy, utilizando a função array.



import numpy as np
import random

lista1 = [random.randint(0, 100) for n in range(0, 10)]
print(lista1)
arry_1 = np.array(lista1)
arry_1

#OU

from random import randint 

lista = [randint(0, 100) for _ in range(10)]
array = np.array(lista)

array