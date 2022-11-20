#Questão extra:

#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam 80.00 reais ou em galões de 3.6 litros, que custam 25.00 reais.

#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

#Comprar apenas latas de 18 litros; 
#Comprar apenas galões de 3.6 litros; 
#Misturar latas e galões de forma que o desperdício de tinta seja menor. 
#Podem considerar latas pela metade (valores decimais para quantidade de latas)


area = float(input('INFORME QUANTOS M2 TEM A ÁREA: '))
print('_'*100)
print('\n')
lata = 18
galao = 3.6
qtd_litros = round(area/6)


#LATAS
qtd_lata = round(qtd_litros/lata)
desperdicio_lata = qtd_lata* lata - qtd_litros
valor_lata = qtd_lata*80

print('='*20,'OPÇÃO LATA','='*20)
print('A ÁREA DE {:.2f} M2 IRÁ PRECISAR DE {} LATA(S) DE TINTA,\nTEREMOS UM DESPERDICIO DE {:.2f} LITROS E \nTEREMOS UM GASTO DE R${:.2f} REAIS'.format(area,qtd_lata,desperdicio_lata,valor_lata))
print('='*53)
print('\n')

#GALÕES
qtd_galao =round(qtd_litros/galao)
desperdicio_galao = qtd_galao* galao - qtd_litros
valor_galao = qtd_galao*25

print('='*20,'OPÇÃO GALÃO','='*20)
print('A ÁREA DE {:.2f} M2 IRÁ PRECISAR DE {} LATA(S) DE TINTA,\nTEREMOS UM DESPERDICIO DE {:.2f} LITROS E \nTEREMOS UM GASTO DE R${:.2f} REAIS'.format(area,qtd_galao,desperdicio_galao,valor_galao))
print('='*53)
print('\n')

#GALÕES E LATAS
qtd_latas = round(qtd_litros/lata)
restante = qtd_latas%lata
qtd_galoes = round(restante/galao)
desperdicio = qtd_latas*lata + qtd_galoes*galao - qtd_litros
valor_total = qtd_latas*80 + qtd_galoes* 25

print('='*28,'LATA & GALÃO','='*28)
print('A ÁREA DE {:.2f} M2 IRÁ PRECISAR DE {} LATA(S) E {} GALÃO(ÕES) DE TINTA  \nTEREMOS UM DESPERDICIO DE {:.2f} LITROS E \nTEREMOS UM GASTO DE R${:.2f} REAIS'.format(area,qtd_latas,qtd_galoes,desperdicio,valor_total))
print('='*70)
print('\n')