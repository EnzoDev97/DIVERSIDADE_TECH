# 04 - Dicionários podem ser percorridos com um for. 
#Ao fazer isso, **as chaves serão percorridas** 
#Porém, a partir da chave obtém-se o valor:


# Criando um dicionário de cadastros

cadastro = {
        'nomes': ['Joãozinho', 'Mariazinha', 'Fulano'],
 'idades': [32, 25, 22],
 'cidades': ['São Paulo', 'Londres', 'Rio'],
 'filhos': [0, 0, 3],
 'alturas': [1.8, 1.65, 1.75],
 'trabalho': ['Dentista', 'Cientista de Dados', 'Engenheiro']
}  

for chave in cadastro:
  print(chave)




cadastro['nomes']



for chave in cadastro:
  print(f'chave={chave}, valor={cadastro[chave]}')

  
for chave in cadastro:
  print('chave=', chave)
  for i, elemento in enumerate(cadastro[chave]):
    print('index:', i, 'valor:', elemento)
  print('-'*32)




for chave in cadastro:
  print('chave=', chave)
  valor = cadastro[chave]
  if isinstance(valor, (tuple, list)):
    for i, elemento in enumerate(cadastro[chave]):
      print('index:', i, 'valor:', elemento)
  elif isinstance(valor, (int, float)):
    print('O número é:', valor)
  elif isinstance(valor, str):
    print('A string é:', valor)
  print('-'*32)


nome = 'Joãozinho'
dados = []
index = cadastro['nomes'].index(nome)
for chave in cadastro:
  print("chave", chave)
  valor = cadastro[chave][index]
  print("valor", valor)
  dados.append(valor)




def pega_dados(cadastro, campo, valor):
  dados = []
  index = cadastro[campo].index(valor)
  for chave in cadastro:
    valor = cadastro[chave][index]
    dados.append(valor)
  return tuple(dados)

resultado = pega_dados(cadastro, 'nomes', 'Fulano')
resultado



nome = 'Fulano'
dados = []
index = cadastro['nomes'].index(nome)

for valor in cadastro.values():
  dados.append(valor[index])
  
dados = tuple(dados)
print(dados)

