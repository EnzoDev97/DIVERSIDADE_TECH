#** 07 - Percorra o seguinte array utilizando for encaixado:**

#```arr = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]```

#**Agora, percorra o mesmo array utilizando a função nditer de numpy.**



import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

shape = arr.shape

print("Com for encaixado: ")
for i in range(shape[0]):
    for j in range(shape[1]):
        for k in range(shape[2]):
            print(arr[i, j, k])

print('-'*100,'\n')
print("Com nditer: ")
for x in np.nditer(arr):
    print(x)
