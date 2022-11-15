# 11 - Faça uma função que recebe um número x e uma lista numérica e retorna uma lista cujos elementos 
#são os itens da lista de entrada multiplicado por x.

#Exemplo:

#Se a função receber o número 5 e a lista [3,5,1], então a função deve retornar [5x3, 5x5, 5x1] = [15, 25, 5].

lista = [5,15,20]

def multiplicaListaPorEscalar(num, lista):
    saida = []
    for i in range(len(lista)):
        saida.append(lista[i] * num)
    return saida
multiplicaListaPorEscalar(5, lista)

# ou 
lista1 = [5,10,15]
lista2 = [20,25,30]
lista3 = []
def multiListas(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i] * lista2[i])
    return lista3

multiListas(lista1, lista2)