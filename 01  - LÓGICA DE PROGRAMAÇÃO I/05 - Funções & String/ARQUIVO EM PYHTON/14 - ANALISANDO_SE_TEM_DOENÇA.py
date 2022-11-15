#03 - Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um questionário de sintomas, tendo as perguntas abaixo, faça um programa que faça o diagnóstico deste hospital:

#a. Sente dor no corpo?

#b. Você tem febre?

#c. Você tem tosse?

#d. Está com congestão nasal?

#e. Tem manchas pelo corpo?

#A    B    C    D    E    Resultado
#Sim    Sim    Não    Não    Sim    Dengue
#Sim    Sim    Sim    Sim    Não    Gripe
#Não    Sim    Sim    Sim    Não    Gripe
#Sim    Não    Não    Não    Não    Sem doenças
#Não    Não    Não    Não    Não    Sem doenças

questao_1 = input(' Sente dor no corpo ?(S/N) ---> ') 
questao_2 = input(' Você tem febre ?(S/N) ---> ') 
questao_3 = input(' Você tem tosse ?(S/N) ---> ') 
questao_4 = input(' Está com congestão nasal ?(S/N)---> ') 
questao_5 = input(' Está com congestão nasal ?(S/N) ---> ') 
print('_'*100) 
print('\n')

if questao_1 =='S' and questao_2 == 'S' and questao_3 == 'N' and questao_4 == 'N' and questao_5 =='S': 
    print('DENGUE') 
elif questao_1 =='S' and questao_2 == 'S' and questao_3 == 'S' and questao_4 == 'S' and questao_5 =='N': 
    print('GRIPE') 
elif questao_1 =='N' and questao_2 == 'S' and questao_3 == 'S' and questao_4 == 'S' and questao_5 =='N': 
    print('GRIPE') 
elif questao_1 =='S' and questao_2 == 'N' and questao_3 == 'N' and questao_4 == 'N' and questao_5 =='N': 
    print('SEM DOENÇAS') 
elif questao_1 =='N' and questao_2 == 'N' and questao_3 == 'N' and questao_4 == 'N' and questao_5 =='N': 
    print('SEM DOENÇAS') 
else: 
    print('PRECISAMOS DE MAIS INFORMAÇÕES')