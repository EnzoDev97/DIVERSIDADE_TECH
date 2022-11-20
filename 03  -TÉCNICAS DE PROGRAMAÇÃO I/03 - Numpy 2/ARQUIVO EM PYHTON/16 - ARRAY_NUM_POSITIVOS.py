#16 - Lembra que você obteve o seno de um array na questão anterior?
#Agora, você deve obter um array apenas com os valores positivos do array resultante daquela operação do seno

import math
import numpy as np
from random import randint

Q5 = np.random.rand(40)
Q6 = Q5 * 12 
seno = np.sin(Q6)
print('SENO...')
print(seno)
print('-'*100)


maior_0 = seno > 0  
print(seno[maior_0])