# 10 - Crie um sistema de cadastro utilizando tuplas e crie 3 funções que pesam algumas informações: A menor idade , a maior idade e a media de idades


from typing import List
import statistics

def pegue_idade_minima(cadastros: List[Pessoa]) -> int:
  idades = [] # PREENCHA AQUI
  for pessoa in cadastros:
    idade = pessoa.idade # PREENCHA AQUI
    idades.append(idade) # PREENCHA AQUI
  idade_minima = min(idades) # PREENCHA AQUI
  return idade_minima # PREENCHA AQUI

def pegue_idade_maxima(cadastros: List[Pessoa]) -> int:
  idades = [] # PREENCHA AQUI
  for pessoa in cadastros:
    idade = pessoa.idade # PREENCHA AQUI
    idades.append(idade) # PREENCHA AQUI
  idade_maxima = max(idades) # PREENCHA AQUI
  return idade_maxima # PREENCHA AQUI

def pegue_idade_media(cadastros: List[Pessoa]) -> float:
  idades = [] # PREENCHA AQUI
  for pessoa in cadastros:
    idade = pessoa.idade # PREENCHA AQUI
    idades.append(idade) # PREENCHA AQUI
  idade_media = sum(idades) / len(idades) # Ou alternativa statistics.mean(idades) # PREENCHA AQUI
  return idade_media # PREENCHA AQUI
print(cadastros)

pegue_idade_minima(cadastros)
print('-'*100,'\n')

pegue_idade_maxima(cadastros)
print('-'*100,'\n')

pegue_idade_media(cadastros)
# Enumerate retorna uma tupla
tupla = (10, 20, 30, 'Alex')
for valor in enumerate(tupla):
  print(valor)

print('-'*30)
for valor in enumerate(tupla):
  print(valor[0], valor[1])

print('-'*30)
for idx, elemento in enumerate(tupla):
  print(idx, elemento)