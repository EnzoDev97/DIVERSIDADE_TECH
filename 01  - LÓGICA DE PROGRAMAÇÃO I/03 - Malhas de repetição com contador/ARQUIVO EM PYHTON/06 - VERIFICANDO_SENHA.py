#06 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

#Verifique se na senha existe uma exclamação e um número

nome = input('Digite seu nome')
senha = input('Digite sua senha')

verificador_exclamacao = False
verificador_numero = False

while nome == senha or not verificador_exclamacao or not verificador_numero:
    nome = input('Digite seu nome')
    senha = input('Digite sua senha')

    verificador_exclamacao = False
    verificador_numero = False

    i = 0

    'teo!123'

    while i < len(senha):
        if senha[i] == '!':
            verificador_exclamacao = True

        if senha[i].isdigit():
            verificador_numero = True
        i += 1

print(f'O nome é {nome} e  a senha é {senha} ')