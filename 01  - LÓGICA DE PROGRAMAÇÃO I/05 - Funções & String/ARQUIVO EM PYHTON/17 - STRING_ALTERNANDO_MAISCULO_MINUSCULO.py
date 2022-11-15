# 03 - Altere o exercício anterior para que a string copiada alterne entre letras maiúsculas e minúsculas.

#Exemplo: se o usuário digitar "latex" o programa deve imprimir "LaTeX".

palavra = input("Digite uma palavra: ")
print('_'*100,'\n')
nova_palavra = ""
for i in range(len(palavra)):
    letra = palavra[i]
    if i%2 == 0:
        nova_palavra += letra.upper()
    else:
        nova_palavra += letra.lower()
print(nova_palavra)