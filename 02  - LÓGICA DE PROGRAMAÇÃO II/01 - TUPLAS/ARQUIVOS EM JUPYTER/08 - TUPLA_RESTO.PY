#08 - Utilize o operador * para o resto como o exemplo abaixo!
#Assim garantindo que não seja levantado um erro


linguagens = ('Python', 'JavaScript', 'HTML', 'CSS', 'R')

primeira, *resto = linguagens
print('Primeiro elemento:', primeira)
print('Resto, a partir do segundo elemento:', resto)

*resto, ultimo = linguagens
print('Resto, até o penúltimo elemento:', resto)
print('Último elemento:', ultimo)

primeiro, *resto, ultimo = linguagens
print('Primeiro elemento:', primeiro)
print('Resto, meio:', resto)
print('Último elemento:', ultimo)