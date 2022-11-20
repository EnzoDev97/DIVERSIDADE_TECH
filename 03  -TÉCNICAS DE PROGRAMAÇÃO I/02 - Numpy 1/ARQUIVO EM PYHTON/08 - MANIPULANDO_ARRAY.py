import numpy as np

# Matriz 3x3 de zeros
matrix_3x3 = np.zeros((3, 3))
print('Shape', matrix_3x3.shape)
print(matrix_3x3)
print('-'*100,'\n')

matriz_2x3x3 = np.zeros((2, 3, 3))
print('Shape', matriz_2x3x3.shape)
print(matriz_2x3x3)
print('-'*100,'\n')

vetor = np.arange(0, 12)
print(f'vetor, shape {vetor.shape}, {vetor}')
print('-'*100,'\n')

# Redimensionar a matriz utilizando o reshape
matriz_3x4 = vetor.reshape(3, 4)
print(f'matriz_3x4, shape {matriz_3x4.shape}')
print(matriz_3x4)
print('-'*100,'\n')


# Ou podemos ilimitar uma dimensão
# Queremos 3 colunas
matriz_nx3 = vetor.reshape(-1, 3)
print(f'matriz_nx3, shape {matriz_nx3.shape}')
print(matriz_nx3)
print('-'*100,'\n')

# Empilhando arrays
v1 = np.array([1, 2, 3])
v2 = np.array([40, 50, 60])
m1 = np.array([
    [7, 8, 9],
    [10, 11, 12],
])

m2 = np.zeros((2, 2))
# Empilhamento vertical
print(f"v1, shape {v1.shape}, {v1}")
print(f"v2, shape {v2.shape}, {v2}")
print(f"m1, shape {m1.shape}, {m1}")
print(f"m2, shape {m2.shape}, {m2}")

v1_v2 = np.vstack([v1, v2])
print(f"v1_v2, shape {v1_v2.shape}")
print('-'*100,'\n')


np.hstack([m1, m2])
print('-'*100,'\n')

