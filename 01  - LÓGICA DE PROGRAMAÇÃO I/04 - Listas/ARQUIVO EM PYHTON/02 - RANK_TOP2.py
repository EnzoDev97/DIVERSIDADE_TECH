# 02 - IMPRIMA A MAIOR NOTA E A SEGUNDA MAIOR NOTA DA LISTA

notas = [10,2,6,3,10,6]
alunos = ['Julia', 'Teo', 'Elizabeth', 'Kaio', 'Ilmen', 'Guilherme']

maior_nota = max(notas)
print(maior_nota)

for i in range(len(notas)):

    if notas[i] == maior_nota:
        print(f'O aluno {alunos[i]} tirou a maior nota')