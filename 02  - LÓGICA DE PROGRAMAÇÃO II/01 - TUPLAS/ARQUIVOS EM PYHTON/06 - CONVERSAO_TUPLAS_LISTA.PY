# 06 - Tuplas podem virar listas, e listas podem virar tuplas!

lista_frutas = ['abacate', 'banana', 'maca']
print(type(lista_frutas))
print('DADOS DA LISTA : \033[35m {}\033[0m'.format(lista_frutas))
print('-'*70,'\n')

tupla_frutas = tuple(lista_frutas)
print(type(tupla_frutas))
print('DADOS DA LISTA : \033[33m {}\033[0m'.format(tupla_frutas))
print('-'*70,'\n')
lista_frutas = list(tupla_frutas)
print(type(lista_frutas))
print('DADOS DA LISTA : \033[32m {}\033[0m'.format(lista_frutas))