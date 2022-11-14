# 05 -  - Concatene duas listas pelo seu indice. Por exemplo, dado duas listas abaixo:

#list1 = ["Me", "n", "", "Teodor "]
#list2 = ["u", "ome", "é", "Henrique"]

#o resultado esperado é
#['Meu', 'nome', é, 'Teodor Henrique']

list1 = ["Me", "n", "", "Ana "]

list2 = ["u", "ome", "é", "Carolina"]

concatenada = []

for i in range(len(list1)):
    concatenada.append(f'{list1[i]}{list2[i]}')
    
print(concatenada)
