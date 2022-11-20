#** 08 - Percorra os indexes do seguinte array utilizando for encaixado:**

#```arr = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]```

#**Agora faça o mesmo trabalho utilizando a função ndenumerate.**


import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

shape = arr.shape

print("Com for encaixado: ")
for i in range(shape[0]):
    for j in range(shape[1]):
        for k in range(shape[2]):
            print(arr[i, j, k])
            
print('-'*100,'\n')
print("Com np.ndenumerate: ")
for index, value in np.ndenumerate(arr):
    print(arr[index])
