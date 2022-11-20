import numpy as np
import random
from random import randint 

arr = np.random.randint(0, 100, 10)
print(arr)
print('-'*100)
mat = arr
# Somando uma constante
print(arr + 892)
print('-'*100)
# Subtraindo uma constante
print(arr - 1000)
print('-'*100)
# Divisão com uma constante
print(arr / 100)
print('-'*100)
# Divisões por zero gera infinito
# print(arr / 0)

# Log (utilizando np.log)
print(np.log(arr + 0.0000001)) # Adicionando um valor muito muito pequeno para evitar log de zero (0)
print('-'*100)
# Exponencial
print(np.square(arr))
print(arr**2)
print('-'*100)

# Raiz quadrada
print(arr)
print(np.sqrt(arr))
print('-'*100)

mat  = np.random.randint(0, 100, (3, 5))


print("Max valor:", mat.max())
# Valor máximo por coluna
print("Max coluna:", mat.max(axis=0))
# Valor máximo por linha
print("Max linha:", mat.max(axis=1))
print('-'*100)

# Indice cujo valor é o minimo (`argmin`)
# -> Volta o index na matriz considerando que ela é unidimensional
print("Min valor:", mat.argmin())
# Para pegar o valor, precisamos achatar a matriz e para tal utilizamos o reshape
print(mat.reshape(-1, 1)[0])

# Indice cujo valor é o minimo por coluna
print('Min col:', mat.argmin(axis=0))

# Indice cujo valor é o minimo por linha
print('Min linha:', mat.argmin(axis=1))
print('-'*100)


# Soma total
print('Valor total:', mat.sum())
# Soma por coluna
print('Valor coluna:', mat.sum(axis=0))
# Soma por linha
print('Valor linha:', mat.sum(axis=1))
print('-'*100)


# Média total
print('Média valor:', mat.mean())

# Média por coluna
print('Média coluna:', mat.mean(axis=0))

# Média por linha
print('Média linha:', mat.mean(axis=1))
print('-'*100)


# Desvio padrão total
print('Desvio padrão:', mat.std())

# Desvio padrão coluna
print('Desvio padrão por coluna:', mat.std(axis=0))

# Desvio padrão linha
print('Desvio padrão por linha:', mat.std(axis=1))