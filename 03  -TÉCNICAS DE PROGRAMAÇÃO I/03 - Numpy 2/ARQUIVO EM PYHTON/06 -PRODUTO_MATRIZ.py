#**Produto de matriz (matrix multiplication)**

#https://www.mathsisfun.com/algebra/matrix-multiplying.html

#Ps: note que **dot product** e **matrix multiplication** são duas operações distintas, em termos matemáticos

#A primeira é definida entre dois vetores (dot product) a segunda entre duas matrizes (matrix multiplication), são duas operações distintas em dois tipos de objetos distintos!

#```
#[a, b] @ [e, f]  = [a*e + b*g, a*f + b*h]  
#[c, d]   [g, h]    [c*e + d*g, c*f + d*h]  
#```

import numpy as np
mat1 = np.array([[1000, 200], [2, -7]])
mat2 = np.array([[0, 1], [1, 0]])

print(mat1)
print(mat2)
print('-'*32)
dot = mat1.dot(mat2)
print('dot')
print(dot)
print('-'*32)

matmult = np.matmul(mat1, mat2)
print('matmult')
print(matmult)
print('-'*32)

at = mat1 @ mat2  # Mais comum
print('at')
print(at)
print('-'*32)
mat1 = np.random.randint(0, 3, (3, 2))
mat2 = np.random.randint(0, 3, (2, 3))
print(mat1)
print(mat2)

# Erro
# De broadcast
# print(mat1 * mat2)

dot = mat1.dot(mat2)
print('dot')
print(dot)
print('-'*32)

matmul = np.matmul(mat1, mat2)
print('matmul')
print(matmul)
print('-'*32)

at = mat1 @ mat2  # Mais comum
print('at')
print(at)
print('-'*32)

print(f'''
mat1: {mat1.shape}
mat2: {mat2.shape}
dot: {dot.shape}
matmul: {matmul.shape}
at: {at.shape}
''')


mat1 = np.random.randint(0, 3, (3, 4, 2))
mat2 = np.random.randint(0, 3, (3, 2, 4))
print(mat1)
print(mat2)

# Erro
# De broadcast
# print(mat1 * mat2)

dot = mat1.dot(mat2)
print('dot')
print(dot)
print('-'*32)

matmul = np.matmul(mat1, mat2)
print('matmul')
print(matmul)
print('-'*32)

at = mat1 @ mat2  # Mais comum
print('at')
print(at)
print('-'*32)

print(f'''
mat1: {mat1.shape}
mat2: {mat2.shape}
dot: {dot.shape}
matmul: {matmul.shape}
at: {at.shape}
''')