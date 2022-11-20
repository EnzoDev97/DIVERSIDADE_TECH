#** 04 - Transforme o array em uma matriz 4 por 3 utilizando numpy.**

#```arr = [1, 2, 3, 4, 'Amelia, 'Bruna, 'Carolina', 'Débora', True, False, False, True]```

#**Depois, faça o mesmo para uma matriz 3 por 4.**



import numpy as np

arr = [1, 2, 3, 4, 'Amelia', 'Bruna', 'Carolina', 'Débora', True, False, False, True]

arr_4_por_3 = np.array(arr).reshape(4, 3)
print(arr_4_por_3)
print('-'*100,'\n')

arr_3_por_4 = np.array(arr).reshape(3, 4)
print(arr_3_por_4)
