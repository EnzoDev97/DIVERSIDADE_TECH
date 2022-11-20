#13 - Divida o array obtido na Questão 4 por 3 e, em seguida, multiplique-o pelo array obtido na Questão 3.

import numpy as np
from random import randint

Q3_L = [randint(0, 50) for _ in range(10)]
Q4_L = [randint(50, 100) for _ in range(10)]
Q3 = np.array(Q3_L)
print('ARRAY 1 - {}'.format(Q3))
Q4 = np.array(Q4_L)
print('ARRAY 2 - {}'.format(Q4))
print('-'*50,'\n')

Qa = Q4 / 3
print(Qa)
print('_'*100,'\n')

Q5 = Qa * Q3
print(Q5)