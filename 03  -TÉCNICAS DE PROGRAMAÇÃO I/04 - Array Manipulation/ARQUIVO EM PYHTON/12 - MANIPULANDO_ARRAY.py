#DESAFIO:

#** 12 -  Utilizando manipulação de arrays, vamos seguir um conjunto de passos para organizar alguns dados. Teremos nesse seguinte array uma ordem que segue:**

#```[Nome do aluno, idade, 'gênero', signo, altura, nota do 1° semestre, nota do 2° bimestre, se está ou não inscrito no próximo ano da escola, nome do outro aluno, idade do outro aluno...]```

#```arr = ['Amélia', 13, 'F', 'peixes', 1.51, 9, 7, True, 'Bruno', 14, 'O', 'leão', 1.60, 4, 10, False, 'João', 14, 'M', 'escorpião', 1.58, 8, 9, True, 'Jordana', 13, 'F', 'escorpião', 1.72, 9, 9, False]```

#**a) Enumere os indexes de todas as informações que são do tipo string.**

#**b) Separe essas informações do objeto arr de forma que cada aluno tenha seu próprio array.**

#**c) Separe em duas colunas, a primeira com o nome, a idade, o gênero e o signo e a segunda com a altura, nota do primeiro bimestre, nota do segundo bimestre e se está ou não inscrito no próximo ano.**

#**d) Elimine o gênero de todos os arrays cujos alunos tem menos de 14 anos.**



import numpy as np

arr = np.array(['Amélia', 13, 'F', 'peixes', 1.51, 9, 7, True,
                'Bruno', 14, 'O', 'leão', 1.60, 4, 10, False,
                'João', 14, 'M', 'escorpião', 1.58, 8, 9, True,
                'Jordana', 13, 'F', 'escorpião', 1.72, 9, 9, False])

# a)
indices = np.where(np.char.isalpha(arr))[0]
print(indices)

# b)
alunos = np.split(arr, 4)
print(alunos)

# c)
coluna1, coluna2 = np.hsplit(arr.reshape(-1, 8), 2)
print(coluna1)
print(coluna2)

# d)
def delete_gender(x):
    if int(x[1]) < 14:
        x[2] = None
    return x

sem_genero = np.apply_along_axis(delete_gender, axis=1, arr=coluna1)
print(sem_genero)
