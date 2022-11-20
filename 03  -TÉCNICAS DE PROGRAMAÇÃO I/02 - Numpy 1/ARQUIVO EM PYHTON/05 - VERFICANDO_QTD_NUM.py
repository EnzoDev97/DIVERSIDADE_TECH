#05 - Receba um número de 1 a 100 (faça ifs para verificar se está dentro deste intervalo). 
# Verifique quantos números pares existem de 1 até o número digitado OU (Se der tempo) receba dois numeros que devem ser de 1 a 100 e verifique quantos números pares tem neste intervalo

numero = int(input('Digite um número de 1 a 100: '))
i = 1
par = 0

if numero >= 1 and numero <= 100:
    while i <= numero:
        if i % 2 == 0:
            par += 1
        i += 1
    print(par)
else:
    print('O numero tem que estar entre 1 e 100.')