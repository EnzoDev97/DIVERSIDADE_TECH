#**Drops**

#Crie um array aleatório de 10.000 elementos de cada distribuição:
#- [Normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#) (média: 5, desvio: 10)
#- [Poisson](https://numpy.org/doc/stable/reference/random/generated/numpy.random.poisson.html) (use lam (lambda) de 5)
#- [Exponencial](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html) (use scale: 5)

#Casos de uso:
#- Normal
#  - Altura
#  - Jogar um dado
 # - Preço de ações
#- Poisson
 # - Número de clientes numa fila em um determinado tempo (uma hora por exemplo)
 # - Número de inadiplências por mês
 # - Venda de um item por mês
# Exponencial
 # - Predizer quando um terremoto irá acontecer
 # - Duração de uma ligação
 # - Vendas esperadas ao abrir uma nova loja


import numpy as np

# Distribuição normal utilizando Numpy
normal = np.random.normal(5, 10, 300_000)

# Distribuição de Poisson
# média = lambda e o desvio padrão = lambda
poisson = np.random.poisson(5, 300_000)

# Distribuição exponencial
exponential = np.random.exponential(5, 300_000)

# Distribuição weibull
weibull = np.random.weibull(5, 300_000)

print('normal', 'tamanho', normal.shape)
print(normal)
print('poisson', 'tamanho', poisson.shape)
print(poisson)
print('exponential', 'tamanho', exponential.shape)
print(exponential)
print('\n')

import matplotlib.pyplot as plt
import seaborn as sns

# sns.histplot(normal, bins=30)
# sns.histplot(poisson, bins=19, color ='orange')
# sns.histplot(exponential, bins=25, color='red')

sns.histplot(weibull, bins=25, color=sns.color_palette()[0]) # sns.color_palette()[0] -> Azul

