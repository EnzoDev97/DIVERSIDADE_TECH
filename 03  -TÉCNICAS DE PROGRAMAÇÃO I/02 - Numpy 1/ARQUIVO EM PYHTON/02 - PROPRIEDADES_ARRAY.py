import numpy as np

lista_de_lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
bi_matrix = np.array(lista_de_lista)
print('MATRIZ 01...')
print('\033[34m {} \033[0m'.format(bi_matrix))

print('-'*100,'\n')

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
print('MATRIZ 02...')

print('\033[35m {} \033[0m'.format(rgb))

print('-'*100,'\n')





print('\033[31m INFORMAÇÕES DAS PROPRIEDAS DO ARRAY LOGO ABAIXO...\033[0m \n')

vetor_numpy = np.array([1, 2, 3, 4, 5])
print('Vetor ndim', vetor_numpy.ndim)    # Unidimensional
print('Vetor shape', vetor_numpy.shape)  # 5 elementos
print('Vetor size', vetor_numpy.size)    # Número de elementos totais
print('-' * 32)

print('Matriz bidimensional ndim', bi_matrix.ndim)    # Bidimensional
print('Matriz bidimensional shape', bi_matrix.shape)  # (3, 3) elementos (Linha/Coluna)
print('Matriz bidimensional size', bi_matrix.size)    # Número de elementos totais
print('-' * 32)

print('Matriz tridimensional ndim', rgb.ndim)    # Tridimensional
print('Matriz tridimensional shape', rgb.shape)  # (3, 3, 3) elementos (Canais/Linha/Coluna)
print('Matriz tridimensional size', rgb.size)    # Número de elementos totais
print('-' * 32)