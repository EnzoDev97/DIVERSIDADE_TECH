# 04 - LISTA SEPARANDO ALUNOS APROVADOS E REPROVADOS 

alunos = ['Julia', 'Paulo', 'Luana', 'Guilherme', 'Ilmen', 'Elizabeth', 'Guilherme']
notas = [2,6,7,4,3,2,8]

aprovados = []
reprovados = []

for i in range(len(alunos)):

    if notas[i] > 6:
        aprovados.append(f'{alunos[i]},{notas[i]}')
    else:
        reprovados.append(f'{alunos[i]},{notas[i]}')

print(f'Aprovados: {aprovados}')
print(f'Reprovados: {reprovados}')