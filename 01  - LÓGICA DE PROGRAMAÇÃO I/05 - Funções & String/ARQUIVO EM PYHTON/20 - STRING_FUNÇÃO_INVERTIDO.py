# 06 - Faça uma função que recebe uma string e retorna ela ao contrário.

#Exemplo: Recebe "teste" e retorna "etset".

def inverte(palavra):
    string = ""
    for letra in palavra:
        string = letra + string
    return string

print(inverte("teste"))

# OU

def inverte(palavra):
    return palavra[::-1]

palavra = "teste"
print(inverte(palavra))