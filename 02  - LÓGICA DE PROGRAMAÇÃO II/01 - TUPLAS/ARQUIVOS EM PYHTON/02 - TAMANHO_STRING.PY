
#02 - Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas 
#seguido do seu comprimento. 
#Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

P1 = input('DIGITE A PRIMEIRA PALAVRA: ')
P2 = input('DIGITE A SEGUNDA PALAVRA: ')
p1 = P1.upper()
p2 = P2.upper()

c1 = len(p1)
c2 = len(p2)

if c1 == c2:
     print('AS PALAVRAS : {} E {}  POSSUEM A MESMA QUANTIDADE DE CARACTERES --- {}'.format(p1,p2,c1))
else:
     print('AS PALAVRAS : {} E {}   NÃO POSSUEM A MESMA QUANTIDADE DE CARACTERES --- {} E {} RESPECTIVAMENTE '.format(p1,p2,c1,c2))

if p1 ==p2:
    print('AS PALAVRAS : {} E {}  POSSUEM O MESMO SIGNIFICADO'.format(p1,p2))
else:
      print('AS PALAVRAS : {} E {}   NÃO POSSUEM O MESMO SIGNIFICADO'.format(p1,p2))