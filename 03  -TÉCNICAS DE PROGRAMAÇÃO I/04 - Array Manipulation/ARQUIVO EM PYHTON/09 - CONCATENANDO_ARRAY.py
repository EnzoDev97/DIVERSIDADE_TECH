#** 09 - Junte os dois seguintes arrays na horizontal:**

#```arr1 = [1, 2, 3]```

#```arr2 = [4, 5, 6]```

#**Depois, os junte verticalmente.**



import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

horizontal = np.concatenate((arr1, arr2))
vertical = np.stack((arr1, arr2))

print("Horizontal:\n", horizontal)
print("Vertical:\n", vertical)