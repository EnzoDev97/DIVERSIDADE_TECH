# 01 - SEPARANDO STRING UM POR UM

nome = 'ENZO CONCEIÇÃO DOS SANTOS'

i = 0

while i < len(nome):
    print(nome[i])
    i += 1

print('='*100)

#OU

print(len(nome))

for i in range(len(nome)):
    print(f'Indice {i} - letra {nome[i]}')