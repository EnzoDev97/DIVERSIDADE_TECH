# 05 - É possível obter chaves e valores separadamente.
#Para isso, usamos os métodos `keys()` e `values()`.

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

nome = 'Fulano'
dados = []
index = cadastro['nomes'].index(nome)

for valor in cadastro.values():
  dados.append(valor[index])
dados = tuple(dados)
print(dados)

# ------------------------------------------------------
print('chaves:', cadastro.keys())

print('-'*100)

print('valores:', cadastro.values())

# ------------------------------------------------------

# dict.items() retorna uma tupla
for item in cadastro.items():
  print(f'item={item}')
  print('-'*32)

# ------------------------------------------------------

# Desempacotando a tupla proveniente do `dict.items()` em (<chave>, <valor>)

for k, v in cadastro.items():
  print(f'chave={k}')
  print(f'valor={v}')
  print('-'*32)

# ------------------------------------------------------

for k, (primeiro, segundo, terceiro) in cadastro.items():
  print(f'chave={k}')
  print('primeiro',primeiro)
  print('segundo',segundo)
  print('terceiro',terceiro)
  print('-'*32)
# ------------------------------------------------------

for k, (primeiro, *resto) in cadastro.items():
  print(f'chave={k}')
  print('primeiro',primeiro)
  print('resto', resto)
  print('-'*32)