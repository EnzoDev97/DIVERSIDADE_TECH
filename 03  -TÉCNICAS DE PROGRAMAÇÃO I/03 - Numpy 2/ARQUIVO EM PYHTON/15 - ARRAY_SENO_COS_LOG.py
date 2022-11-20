#15 - Para cada elemento do array da questão anterior, calcule:

#* O seno
#* O cosseno
#* O log na base 10
#* O valor arredondado para inteiro


import math
import numpy as np
from random import randint

Q5 = np.random.rand(40)
Q6 = Q5 * 12
seno = np.sin(Q6)
cosseno = np.cos(Q6)
log = np.log10(Q6)
inteiro = np.round(Q6)

print('SENO...')
print(seno)
print('-'*100)

print('COSSENO...')
print(cosseno)
print('-'*100)

print('LOG...')
print(log)
print('-'*100)

print('INTEIRO...')
print(inteiro)
print('-'*100)