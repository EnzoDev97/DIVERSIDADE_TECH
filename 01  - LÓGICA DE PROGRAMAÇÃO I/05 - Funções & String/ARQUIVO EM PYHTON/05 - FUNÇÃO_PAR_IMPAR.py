# 06 - Faça uma função que recebe um número e retorna True se ele é par ou False, se ele é ímpar.

def par_impa(num):
    par = num%2
    if par == 0:
        print('O NÚMERO {} É PAR'.format(num))
    else:
        print('O NÚMERO {} É IMPAR'.format(num))

par_impa(2)