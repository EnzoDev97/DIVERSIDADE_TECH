#** 06 - Tente transformar o seguinte array em uma matriz 3x3x3**

#```arr = [1, 2, 3, 4, 5, 6, 7, 8]```

#**Funciona? Se sim, explique o motivo. Se não, explique o erro.**

import numpy as np
arr = [1, 2, 3, 4, 5, 6, 7, 8]
np_arr = np.array(arr).reshape(3, 3, 3)
print(np_arr)

# Não funciona: Irá imprimir um erro
# O motivo é que para ser 3x3x3, é necessário
# que possua 3x3x3=27 elementos, e só há 8