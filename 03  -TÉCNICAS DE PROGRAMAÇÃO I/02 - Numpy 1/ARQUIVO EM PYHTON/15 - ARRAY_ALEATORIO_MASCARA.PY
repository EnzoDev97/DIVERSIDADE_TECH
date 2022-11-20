#02 - Agora, vamos explorar os arrays aleatórios e máscaras. Faça o que se pede:

#a) Crie um array aleatório de 15 itens entre 0 e 100;

#b) Qual o maior número do array?

#c) Qual a sua posição?

#d) Verifique quais números do array são maior que 10;

#e) Salve em uma nova lista apenas os itens entre 10 e 30.


import numpy as np
import random
from random import randint 

#a) Crie um array aleatório de 15 itens entre 0 e 100;

lista1 = np.array([random.randint(0,100) for n in range(0,15)])
print('LISTA -> \033[32m  {}\033[m'.format(lista1))
print('-'*100,'\n')

#b) Qual o maior número do array?

maior = max(lista1)
print('MAIOR VALOR DA LISTA É : \033[34m  {}\033[m'.format(maior))
print('-'*100,'\n')

# c) Qual a sua posição?

lista1_nova = list(lista1)
maior_novo = max(lista1_nova)
posicao = lista1_nova.index(maior_novo)
print('A  POSIÇÃO DO MAIOR NÚMERO NA LISTA É ------>  {}'.format(posicao))
print('-'*100,'\n')

#d) Verifique quais números do array são maior que 10;

lista_10 = []
for num in lista1:
    if num > 10:
        lista_10.append(num)
        maior_10 = np.array(lista_10)

print('|LISTA  COM N > 10| -> \033[35m  {}\033[m'.format(maior_10))
print('-'*100,'\n')

#e) Salve em uma nova lista apenas os itens entre 10 e 30.

lista_10_30 = []

for n in lista1:
    if 10 < n < 30:
        lista_10_30.append(n)
        num_10_30 = np.array(lista_10_30)

print('|LISTA  COM N  ENTRE 10 E 30| -> \033[31m  {}\033[0m'.format(num_10_30))
print('_'*100,'\n')


#OUTRO MÉTODO



# a)
numeros = np.random.randint(0, 101, 15)
print(numeros)

# b)
maior = max(numeros)
print(maior)

# c)
indice = np.argmax(numeros)
print(indice)

# d)
maiores_que_10 = numeros[numeros > 10]
print(maiores_que_10)

# e)
entre_10_e_30 = numeros[(numeros >= 10) & (numeros <= 30)]
print(entre_10_e_30)