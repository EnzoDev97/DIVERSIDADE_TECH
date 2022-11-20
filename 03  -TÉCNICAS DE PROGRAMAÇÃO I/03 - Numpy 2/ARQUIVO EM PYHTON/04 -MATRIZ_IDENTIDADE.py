


import numpy as np
# Matriz identidade
mat_identidade = np.identity(10)
mat_identidade
# ou
mat_identidade = np.eye(10)
mat_identidade


matriz_quadrada = np.array([[1000, 200], [2, -7]])
inv_matriz_quadrada = np.linalg.inv(matriz_quadrada)
inv_matriz_quadrada

# Achando a determinante
np.linalg.det(matriz_quadrada)