#01 - Receba o ano (comecando com 1). Informe qual o século que aquele ano pertence, 

from datetime import datetime

ano_atual = str(datetime.now())[0:4]
mes_atual = str(datetime.now())[5:7]
dia_atual = str(datetime.now())[8:11]

print(f'O ano é {ano_atual}, o mês é {mes_atual} e dia é {dia_atual} ')


# Século 

ano = 5 #int(input('Digite um ano: '))

if (ano % 100 == 0):
    seculo =  ano // 100
else:
    
    seculo = ano // 100 + 1
print(f'O ano {ano} pertence ao século {seculo}')


# OU

ano = int(input("Digite um ano para saber o século: "))

resto1 = ano % 10
parte_restante = ano // 10
resto2 = parte_restante % 10

if resto1 == 0 and resto2 == 0:
    seculo = ano//100
    print(f"{ano} pertence ao século {(seculo)}")
else:
    seculo = ano//100 + 1
    print(f"{ano} pertence ao século {(seculo)}")