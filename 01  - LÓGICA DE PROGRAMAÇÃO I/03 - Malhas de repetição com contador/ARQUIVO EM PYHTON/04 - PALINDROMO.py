# 04- Receba uma string e verifique se esta string é um palíndromo. Por ex: aabaa é um palindromo.

string = input("Digita uma palavra ou frase: ")
print(f"A palavra ou frase digitada foi: {string}")
i = 1
string = string.replace(' ','')
string_invertido = ''
while i <= len(string):
    string_invertido += string[-i]
    i += 1
print(string)
print(string_invertido)
if string_invertido == string:
    print("A palavra ou frase é um palíndromo")
else:
    print("A palavra ou frase não é um palíndromo")