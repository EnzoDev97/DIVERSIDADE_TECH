import numpy as np

arr = np.random.randint(0, 100, 10_000)
print('arr', type(arr), arr)
# Para transformar em uma lista Python
lista = list(arr)
print('lista', type(lista), lista)
tupla = tuple(arr)
print('tupla', type(tupla), tupla)

# Podemos utiliza o `tolist`
lista_tolist = arr.tolist()
print("lista_tolist", type(lista_tolist), lista_tolist)