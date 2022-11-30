# 06 - Outra forma de acessar os valores do dicionário é utilizando o método `get`

#* A estrutura do `get` é `get(<chave>, <default>)`

#*Ou seja, podemos definir um valor padrão caso a chave não esteja presente*

#* A vantagem do método `get` é quando tentamos acessar uma chave que não está presente no dicionário



# Criando um dicionário de cadastros
cadastro = {
'nomes': ['Joãozinho', 'Mariazinha', 'Fulano'],
 'idades': [32, 25, 22],
 'cidades': ['São Paulo', 'Londres', 'Rio'],
 'filhos': [0, 0, 3],
 'alturas': [1.8, 1.65, 1.75],
 'trabalho': ['Dentista', 'Cientista de Dados', 'Engenheiro']
}
print(cadastro)

#----------------------------------------------------------------

cadastro.get('nomes')



#**Drops**

#* Utilize o método `get` de dicionário para imprimir o valor da chave "cor" de ambos os dicionários (carro_toyota, carro_ford), e caso a chave não esteja presente retorne o valor preto.



carro_toyota = {
    "modelo": "Yaris",
    "marca": "Toyota",
    "ano": 2020
}

carro_ford = {
    "modelo": "Mustang",
    "marca": "Ford",
    "ano": 1964,
    "cor": "amarelo"
}

print('toyota', carro_toyota.get('cor', 'preto'))
print('ford', carro_ford.get('cor', 'preto'))



