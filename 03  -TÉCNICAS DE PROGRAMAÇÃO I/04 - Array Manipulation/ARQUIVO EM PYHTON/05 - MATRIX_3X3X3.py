#** 05 - Transforme o seguinte array em uma matriz 3D 3x3x3:**

#```arr = range(27)```

#**Deixe um comentário explicando o que significa uma matriz 3D.**


import numpy as np

arr = range(27)
np_arr = np.array(arr).reshape(3, 3, 3)
print(np_arr)

# Da mesma forma que uma matriz (2D) é uma lista
# de linhas, uma matriz 3D é uma lista de matrizes.
# Pode imaginar como se fossem várias matrizes
# uma atrás da outra, cada uma constituindo uma camada
# de um cubo