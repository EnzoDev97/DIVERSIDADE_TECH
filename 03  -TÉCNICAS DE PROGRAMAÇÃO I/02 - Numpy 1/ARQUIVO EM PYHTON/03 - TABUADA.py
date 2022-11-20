# 03 - TABUADA

n = int(input('DIGITE QUANTAS TABUADAS É PARA SEREM FEITAS: '))
print('\n')

print('=' * 55)
print( '|\033[42m{:^53}|\033[0m'.format('TABUADA'))
print('=' * 55)
print('\n')

print('=' * 48)
print('|\033[44m{:^10}\033[0m x \033[41m{:^15}\033[0m = \033[43m{:^15}\033[0m|'.format('NÚMERO','MULTIPLICADOR','RESULTADO'))
print('=' * 48)


for c in range(1,11):
    print('|{:^10} x {:^15} = {:^15}|'.format( n, c, n*c))
    pass

print('-' * 48)
print('\n')

