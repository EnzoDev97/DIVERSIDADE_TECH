# 09 - Faça uma função que recebe duas listas e retorna a soma item a item dessas listas.

#Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4].

lista1 = [5,10,15]
lista2 = [20,25,30]
lista3 = []
def somaListas(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i] + lista2[i])
    return lista3

somaListas(lista1, lista2)