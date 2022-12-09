# Cadastro 
# - Nome
# - Idade
# - Estado

continuar_cadastro = True

cadastros = []

while continuar_cadastro:
  cadastrar = input('Deseja inserir um novo cadastro? ')
  if cadastrar.lower() in ['sim', 's', 'yes', 'y']:
    nome = input('Insira o nome: ')
    idade = int(input('Insira a idade: '))
    estado = input('Insira o estado: ')
    # Criando uma tupla com as informações pessoais
    cadastro = (nome, idade, estado)

    # Adicionando na lista cadastro a pessoa recem cadastrada
    cadastros.append(cadastro)

  elif cadastrar.lower() in ['não', 'nao', 'n', 'no']:
    print(f'Cadastro finalizado, inserido {len(cadastros)} novas pessoas')
    continuar_cadastro = False
else:
    print(f'Opção invalida. Foi inserido "{cadastrar}"')
    print("Escolha entre ['sim', 's', 'yes', 'y'] para cadastrar uma nova pessoa ou ['não', 'nao', 'n', 'no'] para parar")


    #Conseguimos desempactor os elementos tanto de tuplas como de listas (do inglês *unpacking*).


pessoa = cadastros[0]
print(pessoa)
nome, idade, estado = pessoa
print(nome)
print(idade)
print(estado)