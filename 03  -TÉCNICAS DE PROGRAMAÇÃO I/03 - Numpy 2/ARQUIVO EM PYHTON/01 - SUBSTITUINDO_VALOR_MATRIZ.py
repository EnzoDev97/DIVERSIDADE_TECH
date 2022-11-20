import numpy as np
arr = np.arange(0, 100, dtype="object")
arr2 = arr.copy()
print('arr', arr)
print('-'*32)

mascara_3 = (arr % 3 == 0)
print('Div 3', arr[mascara_3])
print('-'*32)

mascara_5 = (arr % 5 == 0)
print('Div 5', arr[mascara_5])
print('-'*32)
#**Drops**

##A partir da matriz `arr` substitua os valores com base nos seguintes critérios:
#- Divisivel por 3 -> fizz
#- Divisivel por 5 -> buzz
#- Divisivel por 3 e 5 -> fizzbuzz


# mascara_3x5 = ((arr % 3 == 0) & (arr % 5 == 0))
mascara_3x5 = ((mascara_3) & (mascara_5))
print('Div 3 e 5', arr[mascara_3x5])
print('-'*32)

arr[mascara_3] = "fizz"
print("arr depois de substituir com a `mascara_3`", arr)
print('-'*32)

arr[mascara_5] = "buzz"
print("arr depois de substituir com a `mascara_5`", arr)
print('-'*32)

arr[mascara_3x5] = "fizzbuzz"
print("arr depois de substituir com a `mascara_3x5`", arr)

for ele in arr2:
  if ele % 3 == 0 and ele % 5 == 0:
    arr2[ele] = 'fizzbuzz'
  elif ele % 3 == 0:
    arr2[ele] = 'fizz'
  elif ele % 5 == 0:
    arr2[ele] = 'buzz'

print('arr2', arr2)