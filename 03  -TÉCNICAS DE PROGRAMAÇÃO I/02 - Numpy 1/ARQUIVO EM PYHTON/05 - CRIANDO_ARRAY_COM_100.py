#Escreva um programa que crie um array de tamanho 100 e atualize os indices pares com o número do indice ao quadrado

#Por exemplo:

#array(0, 0, 1, 0, 4, 0, 16, ...)

#Explicação

#0 -> 0**2  -> 0
#1 -> impar -> 0
#2 -> 2**2  -> 4
#3 -> impar -> 0
#4 -> 4**2  -> 16

import numpy as np

arr = np.zeros(100)
# np.set_printoptions(suppress=True)  # Suprimindo a anotação científica, suppress=True!
for idx, valor in enumerate(arr):
  if idx % 2 == 0:
    arr[idx] = idx**2
  else:
    arr[idx] = 0
print(arr)