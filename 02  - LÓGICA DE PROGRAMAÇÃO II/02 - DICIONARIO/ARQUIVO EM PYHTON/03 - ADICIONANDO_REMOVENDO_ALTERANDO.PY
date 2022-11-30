## 03 - Para adicionar elementos ao dicionário, não precisamos de uma função pronta (como o append das listas). 
#Basta definir a nova chave como uma variável, e atribuir um novo valor a ela:

cadastro = {
    'nomes': ['Joãozinho', 'Mariazinha'],
    'idades': [32, 25],
    'cidades': ['Maua', 'Santo André'],
    'filhos': [0, 0],
    'alturas': [1.80, 1.65]
}

# Adicionando uma nova chave no dicionário `cadastro`

cadastro['pets'] = ['Bia', 'Luiza']

print(cadastro)


#**Adicione o par chave-valor "cor": "azul: no dicionário `carro` abaixo**



carro = {
    'marca': "Toyota",
    'modelo': "Yaris",
    "ano": 1964
}
carro['cor'] = 'azul' # PREENCHA AQUI!

print(carro)


#**__Para apagar uma chave, utilize o "pop"__**



pets = cadastro.pop('pets')

print(cadastro)


#**__Ou, utilize o "del"__**



cadastro['pets'] = pets
print(cadastro)
del cadastro['pets']
print('Dicionário após o `del`')
print(cadastro)


#**Drops**

#* Remova o campo (chave) "modelo" do dicionário `carro` abaixo



carro = {
    'marca': "Toyota",
    'modelo': "Yaris",
    "ano": 1964
}
# carro.pop('modelo')
del carro['modelo']

print(carro)



#* **Alterar os valores também é possível:**

#_Posso também alterar elementos individuais dos valores, os indexando_

#*(Lembre-se que, neste caso, os valores são listas! Então, devo indexá-las para alterar seus elementos!)*


cadastro['cidades'] = ['Paris', 'Londres']
print(cadastro)


# Alteração indevida de valor


cadastro['cidades'] = 1
print(cadastro)
print('-'*50,'\n')

cadastro['cidades'] = ['Paris', 'Londres']
print(cadastro)
print('-'*50,'\n')

#**Drops**

#*Modifique o ano de fabricação (campo `ano`) de 1964 para 2020 no dicionário abaixo*



cadastro['trabalho'] = ('Dentista', 'Cientista de Dados')
print(cadastro)
print('-'*50,'\n')

cadastro['trabalho'] = ['Dentista', 'Cientista de Dados']
print(cadastro)
print('-'*50,'\n')



cadastro['nomes'].append('Fulano')
cadastro['idades'].append(22)
cadastro['cidades'].append('Rio')
cadastro['filhos'].append(3)
cadastro['alturas'].append(1.75)
cadastro['trabalho'].append('Engenheiro')
print(cadastro)
print('-'*50,'\n')





nome, idade = cadastro['nomes'][1], cadastro['idades'][1]
print(nome, idade)
