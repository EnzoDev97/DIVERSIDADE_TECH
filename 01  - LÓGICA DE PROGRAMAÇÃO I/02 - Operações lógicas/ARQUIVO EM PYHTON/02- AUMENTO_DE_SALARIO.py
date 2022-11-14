#2 - Uma empresa decidiu dar um aumento de 5% no salário de uma pessoa se ela trabalha na mesma empresa a mais de 5 anos. 
# Faça um programa que receba o ano de contratação, o salário e mostre o novo salário. Considere o ano atual (2022) para o cálculo.


import datetime

data_now = str(datetime.datetime.today())

data_inicio = input('Digite o ano de sua contratação: ')
salario = float(input('Digite seu salário: '))
tempo_casa = int(data_now[:4]) - int(data_inicio)
print(f'Você tem {tempo_casa} anos de empresa. ',end='')
if tempo_casa > 5:
    salario = salario * 1.05
    print(f'Seu novo salário é R${salario}')
else:
    print(f'Seu salário permanecerá em R${salario}')