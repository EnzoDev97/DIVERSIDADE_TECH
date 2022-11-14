# 07 -  Faça um programa que peça para o usuário digitar o nome e a nota. O nome e a nota devem estar em um único input, e os valores digitados separados por , (por ex: teo,8).
#O usuário deverá digitar pelo menos 3 nome/notas, e escrever PARE caso não queira digitar mais nome e notas. As duas condições tem que ser verdadeiras, ter ao menos 3 nome e só parar ao digitar PARE
#Após a inclusão dos nome e notas, calcule a média, e mostre o nome dos nome que ficaram acima da média.

#Regras:
#a) As notas devem estar entre 0 e 10. Caso não estejam, exiba uma mensagem e peça para que seja digitado novamente

#b) O nome do aluno deve ter pelo menos 3 caracteres. Caso não esteja, peça para ser digitado novamente

controle = False
lista_sala = []
count = 0

# PREENCHENDO AS INFORMAÇÕES ATÉ O LIMTE

while controle != True:
    dado = input('DIGITE O NOME E A NOTA (separando os dados por virgulas): ')
    
    lista_alunos = []
    if dado =='pare' and count >=3: 
        controle = True
        break # A LISTA SE ENCERRA
        
    lista_alunos = dado.split(',')
    
    lista_alunos[1]=float(lista_alunos[1]) # CONVERTEU A NOTA STRING PARA FLOAT
    
    # ADD OS DADOS NA LISTA SALA
    lista_sala.append(lista_alunos)
    count +=1
print('_'*100,'\n')
print('LISTA ----> {}'.format(lista_sala))
print('_'*100,'\n')   
media = 6

for i in range(len(lista_alunos)):
    media+= lista_sala[i][1]

media/= len(lista_sala)
aprovados = []

for i in range(len(lista_sala)):
    if lista_sala[i][1] >= 6:
        aprovados.append(lista_sala[i][0])
print('OS ALUNOS QUE OBTIVERAM NOTAS ACIMA DE MÉDIA FORAM: {}'.format(aprovados)) 