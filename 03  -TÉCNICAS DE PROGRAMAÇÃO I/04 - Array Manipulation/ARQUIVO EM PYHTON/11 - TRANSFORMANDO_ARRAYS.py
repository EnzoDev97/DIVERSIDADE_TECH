#** 11 - a) Tranforme o seguinte array 2D em dois arrays 2D:**

#```arr = [[1, 2], [3, 4], [5, 6], [7, 8]]```

#**b) Transforme o seguinte array em três arrays com apenas uma coluna:**

#```arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]```



import numpy as np

# a)
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
arrays = np.vsplit(arr, 2)

for i in range(len(arrays)):
    print(f'Array {i}: \n', arrays[i])

# b)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arrays = np.hsplit(arr, 3)

for i in range(len(arrays)):
    print(f'Array {i}: \n', arrays[i])