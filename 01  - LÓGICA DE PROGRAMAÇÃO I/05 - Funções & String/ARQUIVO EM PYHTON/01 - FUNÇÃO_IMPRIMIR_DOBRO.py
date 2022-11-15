# 01 - Faça uma função que recebe um número e imprime seu dobro.
def dobro_num(): 
    num = int(input('DIGITE UM NÚMERO')) 
    print('_'*100) 
    print('\n') 
    dobro = num*num 
    print('O DOBRO DO NÚMERO {} É {}'.format(num,dobro))
dobro_num()