# 07 - Faça uma função que sorteia 10 números aleatórios entre 0 e 100 e retorna o maior entre eles.

from random import randint

def sorteia(lista):
    print('SORTEANDO 10 NÚMEROS...\n')
    for cont in range(0,10):   # ESCOLHENDO A QUANTIDADE DE NÚMEROS QUE DEVE SER SORTEADO
        lista.append(randint(1,100))  # INFORMANDO  QUAIS NUMEROS  PODEM SER SORTEADO
    print(numeros)
    print('_'*50,'\n')

numeros = list()

sorteia(numeros)

maior =max(numeros)
print('O MAIOR NÚMERO SORTEADO foi {}'.format(maior))