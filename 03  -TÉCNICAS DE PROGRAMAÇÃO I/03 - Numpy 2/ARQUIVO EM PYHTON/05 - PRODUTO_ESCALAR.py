##**Produto escalar (dot product)**

#https://www.mathsisfun.com/algebra/vectors-dot-product.html


import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 2, 3])

print('*', arr1*arr2)

print("dot", arr1.dot(arr2))

print("matmul", np.matmul(arr1, arr2))

print("@", arr1 @ arr2)  # Mais comum