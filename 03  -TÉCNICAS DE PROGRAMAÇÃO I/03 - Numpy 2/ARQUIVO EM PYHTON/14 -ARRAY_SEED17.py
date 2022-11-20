#14 - Crie um array com 40 números aleatórios, distribuídos uniformemente, entre [0, 5). Em seguida, some-o com o array obtido na Questão 5.

#OBS.: Utilize a seed 17 para a criação do array aleatório.

import numpy as np
from random import randint

np.random.seed(17)

Qr = np.random.rand(40) * 5
Q5 = np.random.rand(40) 
Q6 = Qr + Q5
Q6


lista6 =np.linspace(0,5,40)
print('LISTA 6...\n')
print(lista6)
print('_'*100,'\n')
lista4 = np.random.rand(40) 

print('LISTA NOVA...\n')
print(lista6 +lista4)