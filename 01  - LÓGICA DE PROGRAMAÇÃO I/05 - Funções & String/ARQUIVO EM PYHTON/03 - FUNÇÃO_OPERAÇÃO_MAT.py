# 03 - Faça uma função para cada operação matemática básica (soma, subtração, multiplicação e divisão). 
#As funções devem receber dois números e retornar o resultado da operação.
# 03 - Faça uma função para cada operação matemática básica (soma, subtração, multiplicação e divisão). 
#As funções devem receber dois números e retornar o resultado da operação.

def soma():
    A = int(input('DIGITE O PRIMEIRO NÚMERO: '))
    B = int(input('DIGITE O SEGUNDO NÚMERO:' ))
    C= A+ B
    print('-'*40)
    print('\n')
    print('*'*20,'SOMA','*'*20)
    print('{} + {} = {}'.format(A,B,C))
    print('_'*30)
    print('\n')

def subtracao(): 
    A = int(input('DIGITE O PRIMEIRO NÚMERO: ')) 
    B = int(input('DIGITE O SEGUNDO NÚMERO: ' ))
    C= A - B
    print('-'*40)
    print('\n')
    print('*'*20,'SUBTRAÇÃO','*'*20)
    print('{} - {} = {}'.format(A,B,C))
    print('_'*30)
    print('\n')

def multiplicacao(): 
    A = int(input('DIGITE O PRIMEIRO NÚMERO: ')) 
    B = int(input('DIGITE O SEGUNDO NÚMERO: ' ))
    C= A * B
    print('-'*40)
    print('\n')
    
    print('*'*20,'MULTIPLICAÇÃO','*'*20)
    print('{} x {} = {}'.format(A,B,C))
    print('_'*30)
    print('\n')   
    
def divisao(): 
    A = int(input('DIGITE O PRIMEIRO NÚMERO: '))
    B = int(input('DIGITE O SEGUNDO NÚMERO: ' )) 
    C= A / B
    print('-'*40)
    print('\n')
    print('*'*20,'DIVISÃO','*'*20)
    print('{} / {} = {}'.format(A,B,C))
    print('_'*30)
    print('\n')   
    
soma()
subtracao()
multiplicacao()
divisao()
