# 08 - Faça uma função que recebe uma lista de palavras e retorna uma lista contendo as mesmas palavras da lista anterior,
#porém escritas em caixa alta.
def caixa_alta(lista):
    caixa_alta = []
    for i in range(len(lista)):
        caixa_alta.append(lista[i].upper())

    return caixa_alta

listaQualquer = list(input('Digite um conjunto de palavras: '))

print(f'{caixa_alta(listaQualquer)}')