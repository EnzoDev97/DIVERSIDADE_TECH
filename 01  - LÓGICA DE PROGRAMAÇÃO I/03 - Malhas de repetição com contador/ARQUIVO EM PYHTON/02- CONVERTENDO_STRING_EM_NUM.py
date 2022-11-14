# 02 - CONVERTENDO STRING EM NUMERO

variavel = input('Digite qualquer coisa')
print(type(variavel))

if variavel.isdigit():
    variavel = int(variavel)

print(type(variavel))
print('-'*100)

# OU 

idade = input('Digite sua idade')

while idade.isdigit() == False:
    idade = input('Digite sua idade')

print(f'A sua idade é {int(idade)}')
