# Cadastro 
# - Nome
# - Idade
# - Estado

from collections import namedtuple

continuar_cadastro = True
Pessoa = namedtuple('Pessoa', ['nome', 'idade', 'estado'])
cadastros = []

while continuar_cadastro:
  cadastrar = input('Deseja inserir um novo cadastro? ')
  if cadastrar.lower() in ['sim', 's', 'yes', 'y']:
    nome = input('Insira o nome: ')
    idade = int(input('Insira a idade: '))
    estado = input('Insira o estado: ')
    # Criando uma tupla com as informações pessoais
    cadastro = Pessoa(nome, idade, estado)

    # Adicionando na lista cadastro a pessoa recem cadastrada
    cadastros.append(cadastro)

  elif cadastrar.lower() in ['não', 'nao', 'n', 'no']:
    print(f'Cadastro finalizado, inserido {len(cadastros)} novas pessoas')
    continuar_cadastro = False
  else:
    print(f'Opção invalida. Foi inserido "{cadastrar}"')
    print("Escolha entre ['sim', 's', 'yes', 'y'] para cadastrar uma nova pessoa ou ['não', 'nao', 'n', 'no'] para parar")

    # ------------------------------------------------------------------------------------------
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

# -------------------------------------------------------------------------------------------------------------

pegue_idade_minima(cadastros)
print('-'*100,'\n')

pegue_idade_maxima(cadastros)
print('-'*100,'\n')

pegue_idade_media(cadastros)

# -----------------------------------------------------------------------------------------------------

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

  # -----------------------------------------------------------------------------------------------------

#Outra utilidade de tuplas: fazer uma função retornar mais de um valor
  
#Outra utilidade de tuplas: fazer uma função retornar mais de um valor

def seq(x):
  return x, 2*x, 3*x

seq(2)

