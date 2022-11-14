#6 - Um aluno não pode fazer a prova se a porcentagem de comparecimento nas aulas dele for menor que 75%.
# Receba o número de aulas de um módulo, o número de aulas que o aluno participou.
# Mostre o % de participação e se o estudante pode fazer a prova ou não.
# Inclua regras de preenchimento não explícitas no exercício

Aulas_totais = int(input('Insira o número total de aulas: '))
Aulas_comparecidas = int(input('Insira o número de aulas comparecidas: '))
Percentual = Aulas_comparecidas*100/Aulas_totais

if Aulas_totais >= Aulas_comparecidas:
    if Percentual >= 75:
        print(f'O aluno compareceu a {Percentual}% das aulas e pode realizar a prova!')
    else:
        print(f'O aluno compareceu a {Percentual}% das aulas e não pode realizar a prova!')
else:
    print('Não é possível faltar mais aulas do que a quantidade de aulas')