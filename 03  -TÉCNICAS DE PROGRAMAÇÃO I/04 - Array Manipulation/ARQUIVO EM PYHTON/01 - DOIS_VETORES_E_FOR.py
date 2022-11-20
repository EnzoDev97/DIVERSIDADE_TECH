# 01 - Printe os elementos dos seguintes dois vetores usando apenas um for:

#arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#Depois, faça o mesmo usando numpy (usando a função nditer) e deixe um comentário sobre a diferença dos dois métodos.

#arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])


# RESPOSTA !!

import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("Com for:")
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        for k in range(arr.shape[2]):
            print(arr[i,j,k])

print('-'*100,'\n')
print("Com nditer:")
for x in np.nditer(arr):
    print(x)

# A diferença é que utilizar o método nditer, que é otimizado
# para percorrer arrays, irá tornar o código mais eficiente.
# Podemos ver que com o nditer apenas um for foi necessário,
# enquanto do primeiro jeito foram necessários 3
