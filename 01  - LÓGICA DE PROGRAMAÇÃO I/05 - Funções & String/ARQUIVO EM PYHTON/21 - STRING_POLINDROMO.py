# 07 - Agora faça uma função que recebe uma palavra e diz se ela é um palíndromo, ou seja, se ela é igual a ela mesma ao contrário.

#Dica: Use a função do exercício 6.
def inverte(palavra):
    return palavra[::-1]

# função ex. 07

def palindromo(palavra):
    palavra = palavra.lower() # Remove letras maiúsculas
    if palavra == inverte(palavra):
        print(palavra, "é um palíndromo.")
    else:
        print(palavra, "não é um palíndromo.")
        
palindromo('ABBA')     