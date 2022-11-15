# 04 - Faça uma função que recebe duas entradas: um input dado pelo usuário e um string que informa o tipo de dado ("idade", "salário" ou "sexo"), e verifica se os dados digitados foram válidos, usando os seguintes critérios:

#a. Idade: entre 0 e 150;

#b. Salário: maior que 0;

#c. Sexo: M, F ou Outro.

def verificacao(entrada, tipo):
    if tipo == "idade" and entrada >= 0 and entrada <= 150:
        return True
    if tipo == "salário" and entrada > 0:
        return True
    if tipo == "sexo" and (entrada == 'M' or entrada == 'F' or entrada == 'Outro'):
        return True
    return False # Só chega se for inválido