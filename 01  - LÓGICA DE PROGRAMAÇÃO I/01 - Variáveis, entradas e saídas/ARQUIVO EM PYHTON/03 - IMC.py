#3 - Crie um algoritmo que calcule o IMC (índice de massa corporal). 
#O IMC é calculado com a formula PESO/(ALTURA elevado a 2). 
#Para isso, coloque as informações nas variáveis e no final apresente o resultado como: "O IMC é [resultado]"

nome = input('INFORME SEU NOME: ')
altura = float(input('INFORME SUA ALTURA (em metros): '))
peso = float(input('INFOME SEU PESO (em kg):  '))
print('_'*100)
print('\n')

imc = peso/(altura**2)

print('OLÁ {}...\nSUA ALTURA É {} M E SEU PESO É {}KG...\nSEU ÍNDICE DE MASSA CORPORAL É {:.2f}'.format(nome,altura,peso,imc))
