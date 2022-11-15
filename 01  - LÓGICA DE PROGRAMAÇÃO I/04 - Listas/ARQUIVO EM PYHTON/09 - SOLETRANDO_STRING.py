#  09 - Faça um programa que peça para o usuário digitar uma palavra e imprima cada letra em uma linha.


nome = 'ENZO CONCEIÇÃO DOS SANTOS'

print(len(nome))

for i in range(len(nome)):
    print(f'Indice {i} - letra {nome[i]}')