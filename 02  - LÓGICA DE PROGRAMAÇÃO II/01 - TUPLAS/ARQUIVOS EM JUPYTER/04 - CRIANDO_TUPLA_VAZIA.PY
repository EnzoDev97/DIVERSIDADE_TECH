
# Criando uma tupla vazia

tupla1 = tuple() # Uma tupla vazia
tupla2 = ()      # Outra tupla vazia
print(tupla1)
print(tupla2)
# Tupla de tuplas
tupla_de_tuplas = (
    ('Curso', 'Módulo I', 'Módulo II'),
    ('Data Science', 'Lógica de programação I', "Lógica de programação II"),
    ('Web', 'Front end Estático', 'Front end Dinâmico')
)
print(tupla_de_tuplas)
print('-'*50,'\n')

dados_variados = (20, 2.15, 'Ana', False) # Tupla com tipos diferentes
print('dados variados:', dados_variados)
print('-'*50,'\n')


linguagens = ('Python', 'SQL', 'R') # Tupla com três elementos
print(linguagens)
print('-'*50,'\n')

print(linguagens[0])  # O primeiro elemento da tupla
print(linguagens[1])  # Segundo elemento da tupla
print(dados_variados[2]) # Terceiro elemento da tupla
print(tupla_de_tuplas[1]) # Segundo elemento da tupla, que é outra tupla
print(tupla_de_tuplas[1][0]) # Segundo elemento da tupla, pegando o curso (primeiro elemento)