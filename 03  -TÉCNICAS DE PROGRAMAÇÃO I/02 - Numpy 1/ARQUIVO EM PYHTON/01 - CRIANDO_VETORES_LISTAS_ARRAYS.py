import numpy as np

lista = [2, 3, 4, 20, 31, 7]

print('lista', type(lista), lista)
print('-'*100,'\n')

# Matrizes com mais dimensões
red = [
    [0, 22, 32],
    [0, 45, 61],
    [0, 0, 0],
]
green = [
    [10, 27, 37],
    [12, 45, 61],
    [120, 10, 120],
]
blue = [
    [15, 45, 78],
    [10, 22, 64],
    [20, 20, 22],
]

rgb = np.asarray([red, green, blue])
print(type(rgb))
print(rgb)