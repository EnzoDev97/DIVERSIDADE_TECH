# 07 - ATUALIZANDO DADOS DENTRO DE UM DICIONARIO



carro_1 = {
    "modelo": "Yaris",
    "marca": "Toyota",
    "ano": 2020
}

carro_2 = {
    "cor": "amarelo"
}
print(carro_1)

#----------------------------------------------------------


carro_1 = {
    "modelo": "Yaris",
    "marca": "Toyota",
    "ano": 2020
}

carro_2 = {
    "cor": "amarelo",
    "ano": 2016
}

carro_1.update(carro_2)

print(carro_1)
