#3 - Dada a seguinte lista abaixo: [['Teo', 8], ['João', 5], ['Marília', 7], ['Jonathan',9]]

#a) Peça para o usuário informar quantas pessoas ele quer adicionar a lista. Ele pode adicionar de 1 a 5 no total. Verifique se o número digitado está no intervalo

#b) Inclua a quantidade de pessoas informada anteriormente. como regra, a nota deverá ser entre 0 a 10, e o nome digitado não pode estar previamente cadastrado (ou seja, não pode inserir Teo, ou João, ou Marília, ou Jonathan, nem repetir os nomes no cadastro). Inclua os valores na lista acima. Ou seja, a lista acima é fixa, e o usuário poderá incluir novos itens na lista. Observe a lista como é feita.

#c) Após a inclusão dos nomes na lista, calcule a média

#d) Mostre o Nome e Nota dos alunos que ficaram acima da média



lista = [['Teo', 8], ['João', 5], ['Marília', 7], ['Jonathan',9]]

qtd_pessoas= int(input('DIGITE QUANTOS ALUNOS DESEJA ADICIONAR: '))

while qtd_pessoas >= 6: 
    qtd_pessoas= int(input('O MÁXIMO DE ALUNOS QUE PODEMOS ADICIONAR É 5--> DIGITE QUANTOS ALUNOS DESEJA ADICIONAR: '))

for x in range(qtd_pessoas): 
    print('\n') 
    print(' '*15, 'ALUNO {:^}'.format(x + 1),' '*8)
    nome = input('NOME: ')
    nota = float(input( 'NOTA: '))
    if  nota < 1  or nota > 10:
        print('Nota Inválida, digite novamente:')
        nota = float(input( 'NOTA: '))
            
    for i in range(len(lista)):
        if nome == lista[i][0]: # VERFICANDO SE TEM NOME IGUAIS
            print('Aluno já inserido. Favor digitar novamente.')
            nome = input('NOME: ')
                
    alunos = [nome,nota]
    lista.append(alunos)
    
print('_'*100,'\n')   

print('ESTÁ É A LISTA COM AS INFORMAÇÕES DO ALUNOS E SUAS NOTAS...\n') 

print('-=-'*42 )
print('\033[1;35m LISTAS DOS ALUNOS --> {}\033[0m'.format(lista)) 
print('-=-'*42,'\n' )

aprovado = 0 

print('LISTA COM OS ALUNOS APROVADOS ...') 
print('='*40)
for media in lista: 
    if media[1] >= 6: 
        aprovado = media[1] 
        alunos = media[0]
        print ('{}  - \033[1;32mAPROVADO\033[0m COM NOTA:  {}'.format(alunos,aprovado))
        
print('='*40)
print('\n')

print('LISTA COM OS ALUNOS REPROVADOS ...')  
print('='*40)
 
for media in lista:     
    if media[1] < 6:
        reprovado = media[1]
        alunos = media[0]
        print ('{}  - \033[1;31m REPROVADOS\033[0m COM NOTA {}'.format(alunos,reprovado))
        
print('='*40)