import numpy as np

arr1 = np.random.randint(0, 100, 10_000)
arr1

print('_'*100,'\n')


print('Primeiro elemento', arr1[0])
print('12 elemento', arr1[11])

print('_'*100,'\n')

# Conseguimos fatiar o array (slice) semelhante a listas
print('Pegando os quatro primeiros elementos', arr1[: 4], 'tamanho', len(arr1[: 4]))
print('Pegando os elementos internos', arr1[900: 8500], 'tamanho', len(arr1[900: 8500]))
print('_'*100,'\n')

mat = np.random.randint(0, 100, (3, 4))
mat
print('_'*100,'\n')

lista = list(mat)
col = []
for linha in lista:
  col.append(linha[0])

print(col)
print('_'*100,'\n')


# Pegando a primeira linha
print(mat[0])
print('-'*32)
# As duas últimas linhas
print(mat[1:])
print(mat[-2:])
print('-'*32)
# A primeira coluna
print(mat[ : , 0]) # O `:`significa todas as linhas, o zeo representa a coluna
print('-'*32)

# As três últimas colunas e duas últimas linhas
print(mat[-2: , -3: ])
print('-'*32)

# Podemos filtrar usando os indices
# Pegando a primeira e terceira linha e todas as colunas
print(mat[[0,2], :])
print('-'*32)
# Pegando a segunda e quarta coluna
print(mat[ : , [1, 3]])
