#### Operações matemáticas com arrays

#A primeira funcionalidade é a capacidade de realizar operações elemento a elemento do array.

import numpy as np

arr = np.array([4, 6, 2, 8])
arr2 = np.array([2, 3, 1, 4])


# SOMA
arr = np.array([4, 6, 2, 8])
arr2 = np.array([2, 3, 1, 4])

print('SOMA.....')
print(arr + arr2)
print('_'*100,'\n')
# Em python puro seria
[ele1 + ele2 for ele1, ele2 in zip(arr, arr2)]



print('SUBTRAÇÃO...')
print(arr - arr2)
print('_'*100,'\n')

print('MULTIPLICAÇÃO...')
print(arr * arr2)
print('_'*100,'\n')

print('DIVISÃO...')
print(arr / arr2)

print('_'*100,'\n')
# Em python puro seria
#[ele1 - ele2 for ele1, ele2 in zip(arr, arr2)]
