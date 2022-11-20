#6 - Escreva um algoritmo que armazene um valor X em uma variável A e um valor Y em uma variável B. 
#Troque os valores das duas variáveis sem criar uma terceira e usando apenas operações matemáticas.


A = 100
B = 50

print('Variavel A: {}\nVariavel B: {}'.format(A,B))

A = A+B
B = A-B
A = (B-A)*-1 
print('Variavel A: {}\nVariavel B: {}'.format(A,B))