#2 - Faça uma função que receba dois números e uma operação matemática. A operação matemática pode ser SOMA, MULTIPLICAÇÃO, DIVISÃO e DIFERENÇA. Mostre o resultado da operação matemática na tela

#a) Para a divisão, verifique se um dos números digitados foi 0. Caso seja, o resultado deve ser 0

#b) Faça uma segunda função, que peça para o usuário na mesma linha (mesmo comando) os dois números e a operação que ele deseja fazer, e chame a primeira função criada.

#c) faça uma terceira função que deverá verificar se o texto digitado pelo usuário é um número. Exemplo: 5,6,multiplicação. Ele tem que verificar se o 5 é numero e se o 6 é numero

#Resumindo:

#São 3 funções
#Função 1 - Pedir os números para o usuário e a operação que ele quer fazer, na mesma linha
#Função 2 - Vai receber como parametro o valor digitado pelo usuário, e verificar se o valor pode ser convertido para número
#Função 3 - Calcular a operação para o usuário e exibir o resultado



# FUNÇÃO ONDE SELECIONA A OPERAÇÃO MAT E REALIZA O CALCULO

def calculadora (a,b,operacao):

    if operacao.upper() == 'SOMA':
        soma = a + b
        print('\033[1;32m O resultado da soma é : {} + {} = {}\033[0m'.format(a,b,soma))
    elif operacao.upper() == 'MULTIPLICAÇÃO':
        multi = a * b
        print('\033[1;34m O resultado da multiplicação é : {} * {} = {}\033[0m'.format(a,b,multi))
    elif operacao.upper() == 'DIVISÃO':
        if a == 0 or b == 0:
            divi = 0
            print('\033[1;35m O resultado da divisão é : {} / {} = {}\033[0m'.format(a,b,divi))
        else:
            divi = a / b
            print('\033[1;36m O resultado da divisão é : {} / {} = {}\033[0m'.format(a,b,divi))
    elif operacao.upper() == 'SUBTRAÇÃO':
        sub = a - b
        print('\033[1;36m O resultado da subtração é : {} - {} = {}\033[0m'.format(a,b,sub))
    else:
        print('\033[1;31m Operação inválida. Verifique se o termo foi digitado como solicitado e tente novamente.\033[0m')

def verifica_numero(num):
    if num.isdigit():  
        return True # O termo {num} digitado é de fato um número.
    else:
        print('O termo {} digitado não é um caracter válido.'.format(num))
        return False

def operar_calculadora():
    operar = input('Digite, separado por vírgula, o valor de A, B e a operação. op: SOMA, MULTIPLICAÇÃO, DIVISÃO, SUBTRAÇÃO')
    print('_'*100,'\n')

    operar = operar.split(',') # REMOVENDO AS VIRGULAS 

    a = operar[0]
    b = operar[1]

    if verifica_numero(a) and verifica_numero(b): # APLICANDO A  FUNÇÃO PARA VERIFICAR SE SÃO NUMEROS/OU CONVERTER PARA NUM
        a = int(operar[0])
        b = int(operar[1])
        op = operar[2]
        calculadora(a, b, op) # CHAMANDO A PRIMEIRA FUNÇÃO
    else:
        print('Já que um dos itens digitados é inválido, a operação foi cancelada.')

operar_calculadora()