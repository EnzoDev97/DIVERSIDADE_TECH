#** 02  - Peça para o usuário uma lista com as comidas favoritas dele, depois transforme isso em um objeto numpy. Agora transformado, elimine todas as comidas que começam com uma vogal. Mostre o resultado.** 

#Exemplo:

#```Entrada: [maçã, uva, morango, melancia, acelga]```

#```Saída: [maçã, morango, melancia]```



import numpy as np

print("Por favor, informe suas comidas favoritas.")
comidas_favoritas = []

resposta = input("Digite uma comida favorita (digite 'fim' para encerrar): ")
while resposta != 'fim':
    comidas_favoritas.append(resposta)
    resposta = input("Digite uma comida favorita (digite 'fim' para encerrar): ")

print('_'*100,'\n')
print('LISTA DE COMIDAS FAVORITAS...')
print(comidas_favoritas)
print('-'*100,'\n')
comidas_favoritas = np.array(comidas_favoritas)

vogais = ['a', 'e', 'i', 'o', 'u']

letras_iniciais = np.char.rjust(comidas_favoritas, 1)
indices_para_excluir = np.where(np.in1d(letras_iniciais, vogais))
comidas_favoritas = np.delete(comidas_favoritas, indices_para_excluir)

print(comidas_favoritas)
