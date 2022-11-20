
import numpy as np

# O where funciona para cada elemento da lista (array)!
# Com Python puro seria como compreensão de lista
mat = np.random.randint(0, 100, (3, 3))
print('mat')
print(mat)
print('-'*21)
np.where(mat%2 == 0, mat**2, -100)

#%%time
arr = np.arange(0, 10_000)
_ = [x**2 if x%2 == 0 else -100 for x in arr]

# Podemos encadear funções where
# Muito parecido com o excel IF(cond2, IF(cond, TRUE, FALSE), FALSE)
arr = np.random.randint(0, 100, 1_000)
filtro_lista = [0, 20, 30]
np.where((arr%2==0),
         np.where(arr > 50, # Verificando se o número par é maior que 50
                  -1000,    # Se for maior que 50 e par, coloque -1000
                  -10       # Se for par e menor ou igual a 50 coloque -10
                ),
         arr # Se impar volta o número
  )