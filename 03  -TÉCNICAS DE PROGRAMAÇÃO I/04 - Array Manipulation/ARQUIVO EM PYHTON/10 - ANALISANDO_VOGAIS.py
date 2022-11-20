#DESAFIO: 

#**10 - Utilizando manipulação de arrays, ache os indexes do array cujo valor possua apenas 2 vogais no nome usando numpy.**

#```frutas = ['banana', 'morango, 'uva', 'pitaia', 'abacate', 'abacaxi', 'acerola', 'jenipapo', 'kiwi']```



import numpy as np

frutas = np.array([
    'banana',
    'morango',
    'uva',
    'pitaia',
    'abacate',
    'abacaxi',
    'acerola',
    'jenipapo',
    'kiwi'
])

vogais = ['a', 'e', 'i', 'o', 'u']

contagens = sum([np.char.count(frutas, vogal) for vogal in vogais])
indices = np.where(contagens == 2)[0]

print(indices)