# 06 - Receba duas listas e faça um único for, onde o resultado da primeira lista deve ficar na ordem original e a segunda na ordem inversa:

#Dado: list1 = [10, 20, 30, 40]

#list2 = [100, 200, 300, 400]

lista1 = [10, 20, 30, 40]
lista2 = [100, 200, 300, 400]
#lista2.reverse()


for i in range(len(lista2)):
  print(f'{lista1[i]} {lista2[-i-1]}')