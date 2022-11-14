# 07 - Faça um programa que receba um número. Verifique quantos números primos existe entre 1 e o número digitado (lembrando que 1 não é primo)

#Por ex: 12 Existem 3 números primos entre 1 e 12

number = int(input('Numero: '))

p = 0

for i in range (2, number+1):
    for k in range(2, i):
        if i % k == 0:
            p += 1
            break
q_numeros_primos = number - (p + 1)

print(q_numeros_primos)