# 05 - Faça uma função que recebe um nome e um horário e imprime “Bom dia, [nome]”, caso seja antes de 12h, “Boa Tarde, [nome]”, caso seja entre 12h e 18h e “Boa noite, [nome]” se for após às 18h.

import datetime

H = datetime.datetime.now()
data = H.strftime('%x')
horario = H.strftime('%X')
hora = H.strftime('%H')
turno = H.strftime('%p')

conversao = int(H.strftime('%H'))

if turno == 'AM' and  6<= conversao <=12:
    print('OLÁ, BOM DIA ! HOJE É {} E SÃO {} DA MANHÃ'.format(data,horario))
elif turno == 'PM' and  12 <=  conversao <= 18:
    print('OLÁ, BOM TARDE ! HOJE É {} E SÃO {} DA TARDE'.format(data,horario))
elif turno == 'PM' and  18 <= conversao <= 23:
    print('OLÁ, BOM NOITE ! HOJE É {} E SÃO {} DA NOITE'.format(data,horario))
else:
    print('OLÁ, BOM MADRUGADA ! HOJE É {} E SÃO {} DA MADRUGADA'.format(data,horario))