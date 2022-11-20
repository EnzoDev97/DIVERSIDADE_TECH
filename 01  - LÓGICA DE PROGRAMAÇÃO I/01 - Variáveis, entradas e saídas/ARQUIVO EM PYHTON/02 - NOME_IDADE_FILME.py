#2- Escreva um programa que receba seu nome, sua idade e filme predileto, e escreva uma unica sentença que seja
#"Meu nome é 'nome', tenho 'anos' anos e meu filme predileto é ''

nome = input('INFORME SEU NOME: ')
idade = int(input('DIGITE SUA IDADE: '))
filme = input('QUAL É O SEU FILME FAVORITO? ')
print('_'*100)
print('\n')

print('MEU NOME É \033[42m{}\033[0m EU TENHO \033[42m{}\033[0m ANOS E MEU FILME FAVORITO É \033[42m{}\033[0m'.format(nome,idade,filme))