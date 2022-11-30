## 02 - Poderíamos, ao invés de um dicionário, usar uma lista de listas, como abaixo. 
#Porém, neste caso, fica bem menos intuitivo quando queremos selecionar os elementos que representam nomes ou cidades, porque somos obrigado a usar números para indexar, ao invés das chaves.


cadastro = {
    'nomes': ['Joãozinho', 'Mariazinha'],
    'idades': [32, 25],
    'cidades': ['Maua', 'Santo André'],
    'filhos': [0, 0],
    'alturas': [1.80, 1.65]
}

nomes = ['Joãozinho', 'Mariazinha']
idades = [32, 25]
alturas = [1.80, 1.65]

cadastro_listas = [
    nomes,
    idades,
    alturas
]

print(cadastro_listas)
