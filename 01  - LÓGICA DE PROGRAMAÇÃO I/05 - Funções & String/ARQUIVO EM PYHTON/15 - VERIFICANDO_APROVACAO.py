#01 - Escreva um programa que peça a nota de 3 provas de um aluno e verifique se ele passou ou não de ano.
#Obs.: O aluno irá passar de ano se sua média for maior que 6.


def aprovacao():
    aluno = input('INFORME SEU NOME: ')
    nota_1 = float(input('NOTA 1: '))
    nota_2 = float(input('NOTA 2: '))
    nota_3 = float(input('NOTA 3: '))
    media = (nota_1 + nota_2  + nota_3)/3
    if media >6:
        print ('O ALUNO : {}  FOI APROVADO COM A MEDIA: {:.2f}'.format(aluno,media))
    else:
        print ('O ALUNO : {}  FOI REPROVADO COM A MEDIA: {:.2f}'.format(aluno,media))
    

aprovacao()
   
        