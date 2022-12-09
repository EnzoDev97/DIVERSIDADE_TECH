#09 - Crie um cadastro em formato tupla utilizando namedtuple com as seguintes informações: NOME , IDADE , ESTADO

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