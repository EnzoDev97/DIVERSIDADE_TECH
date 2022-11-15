# 07 - Faça uma função que recebe um número n de entrada, sorteia n números aleatórios entre 0 e 100 e retorna a média deles.

from random import randint

def sorteia(lista):
    qtd_num=(int(input('DIGITE A QUANTIDADE DE NUMEROS QUE VOCÊ QUER QUE SEJA SORTEADO: ')))
    print('\n')
    print('SORTEANDO {} NÚMEROS...\n'.format(qtd_num))
    for cont in range(qtd_num):   # ESCOLHENDO A QUANTIDADE DE NÚMEROS QUE DEVE SER SORTEADO
        lista.append(randint(1,100))  # INFORMANDO  QUAIS NUMEROS  PODEM SER SORTEADO
    print(numeros)
    print('_'*50,'\n')

numeros = list()
sorteia(numeros)

soma = sum(numeros)

media=soma/len(numeros)
print('A MEDIA É  {:.2f}'.format(media))