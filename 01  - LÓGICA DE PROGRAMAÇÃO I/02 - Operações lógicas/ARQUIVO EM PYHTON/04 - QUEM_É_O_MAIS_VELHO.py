#4- Receba a idade de 3 pessoas e informe o mais velho e o mais novo entre eles. 
# Caso os 3 tenham a mesma idade, informe que todos tem a mesma idade.

idade_1 = int(input("Digita a idade a 1° idade: "))
idade_2 = int(input("Digita a idade a 2° idade: "))
idade_3 = int(input("Digita a idade a 3° idade: "))

if idade_1 == idade_2 and idade_2 == idade_3:
    print('Todas as idades são iguais')
elif idade_1 >= idade_2 and idade_1 >= idade_3:
    print(f'Usuário 1 tem a maior idade {idade_1}')
    if (idade_2 < idade_3):
        print(f'Usuário 2 tem a menor idade {idade_2}')
    elif (idade_2 > idade_3):
        print(f'Usuário 3 tem a menor idade {idade_3}')
    else:
        print(f'Usuário 2 e 3 tem a mesma idade')
    
elif idade_2 >= idade_1 and idade_2 >= idade_3:
    print(f'Usuário 2 tem a maior idade {idade_2}')

    if (idade_1 <= idade_3):
        print(f'Usuário 1 tem a menor idade {idade_1}')
    else:
        print(f'Usuário 3 tem a menor idade {idade_3}')

else:
    print(f'Usuário 3 tem a maior idade {idade_3}')

    if (idade_1 <= idade_2):
        print(f'Usuário 1 tem a menor idade {idade_1}')
    else:
        print(f'Usuário 2 tem a menor idade {idade_2}')