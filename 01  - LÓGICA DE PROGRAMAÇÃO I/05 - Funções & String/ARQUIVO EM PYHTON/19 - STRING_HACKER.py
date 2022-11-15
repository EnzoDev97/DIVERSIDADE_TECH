# 05 - Faça uma função que receba uma string e retorne uma nova string substituindo:

#'a' por '4'

#'e' por '3'

#'I' por '1'

#'t' por '7'

def H4CK3R(palavra):
    nova_string = ""
    for letra in palavra:
        if letra.lower() == 'a':
            nova_string += '4'
        elif letra.lower() == 'e':
            nova_string += '3'
        elif letra.lower() == 'i':
            nova_string += '1'
        elif letra.lower() == 't':
            nova_string += '7'
        else:
            nova_string += letra

    return (nova_string)

print(H4CK3R("Apenas testando"))