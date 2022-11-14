# 08 - Abaixo é definido um n-poligono. O objetivo é achar a area de um poligono dado n. Um 1-poligono é um quadrado com um tamanho 1. Um n-poligono é obtido pegando n-1-poligono e adicionado 1-poligonos a lateral, lado a lado.

#Por exemplo:

#para um n=2, a saida deve ser 5
#para um n=3, a saida deve ser 13
#para um n=4, a saida deve ser 25

n = int(input('Digite o valor de N: '))
poligono = 0

i = 0

while (n > 0):
    i += 1

    if i == 1:
        poligono += 1 + (n-1)*2
    else:
        poligono += (1 + (n-1)*2)*2

    n -= 1

print(f'O poligono tem tamanho: {poligono}')