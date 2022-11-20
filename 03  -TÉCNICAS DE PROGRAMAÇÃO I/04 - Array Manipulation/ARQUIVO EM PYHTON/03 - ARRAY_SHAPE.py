#** 03 - Imprima a dimensão dos seguintes objetos numpy:**

#```a = np.array(2)```

#```b = np.array([1, 2, 3, 4, 5])```

#```c = np.array([[1, 2, 3], [4, 5, 6]])```

#```d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])```



import numpy as np

objetos_numpy = [
    np.array(2),
    np.array([1, 2, 3, 4, 5]),
    np.array([[1, 2, 3],[4, 5, 6]]),
    np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
]

for objeto_numpy in objetos_numpy:
    print('Array:\n', objeto_numpy)
    print('shape:', objeto_numpy.shape, '\n')
