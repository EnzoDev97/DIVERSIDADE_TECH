import numpy as np
import random
from random import randint 
arr = np.random.randint(0, 100, 10)
n = 20
# map(<função>, <iteravel>) -> iteravel [lista, tupla, ...]
lista_20 = list(map(lambda x: x*n, arr))
print(lista_20)