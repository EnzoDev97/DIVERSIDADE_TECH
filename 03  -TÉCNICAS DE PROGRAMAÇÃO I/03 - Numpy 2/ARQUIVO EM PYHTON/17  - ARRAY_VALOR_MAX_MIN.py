#17- Para os dados contidos no array da Q6, obtenha:

#* O valor mínimo
#* O valor máximo
#* A posição do valor mínimo
#* A posição do valor máximo
#* A média dos dados
#* A mediana
#* A moda
#* A variância
#* O desvio padrão
#* O array ordenado (forma crescente)

import math
import numpy as np
from random import randint

Q5 = np.random.rand(40)
Q6 = Q5 * 12 

menor = Q6.min()
maior = Q6.max()
pos_menor = Q6.argmin()
pos_maior = Q6.argmax()
media = Q6.mean()
variancia = Q6.var()
desvio = Q6.std()
Q6.sort()

print(menor)
print('-'*20)

print(maior)
print('-'*20)

print(pos_menor)
print('-'*20)

print(pos_maior)
print('-'*20)

print(media)
print('-'*20)

print(variancia)
print('-'*20)

print(desvio)
print('-'*20)

print(Q6)