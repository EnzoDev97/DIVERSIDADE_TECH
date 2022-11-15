# Desafio 3 - A sequência Fibonacci é a sequência cujos dois primeiros termos são 1 e os demais são obtidos através da soma de seus dois antecessores, isso é:

#a. Fibonacci(1) = 1 e Fibonacci(2) = 2;

#b. dado qualquer número n >= 3, Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)

#Assim, os 10 primeiros termos da sequência Fibonacci são:

#1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
#Faça uma função que receba um número n e calcule o termo de número n da sequência Fibonacci.


# Podemos usar listas
def fibonacci(N):
    numeros = [1, 1]
    for i in range(2,N):
        numeros.append(numeros[i-2] + numeros[i-1])
    return numeros[-1] # Último número da lista

'''
Ou podemos só guardar os 2 ultimos valores(mais eficiente).
Apesar de parecer mais confuso, essa estrutura é bem comum, calculamos o valor da iteração, e então atualizamos os valores antigos
'''

def fibonacci2(N):
    n2 = 1 # 2 números atrás
    n1 = 1 # 1 número atrás
    n = 1 # Inicializa em 1 para caso N seja menor que 2
    for i in range(2, N):
        n = n2 + n1 # Calculamos o número i
        n2 = n1 # Atualiza o número 2 posições atrás
        n1 = n # Atualiza o número 1 posição atrás para próxima iteração
    return n


fibonacci2(10)