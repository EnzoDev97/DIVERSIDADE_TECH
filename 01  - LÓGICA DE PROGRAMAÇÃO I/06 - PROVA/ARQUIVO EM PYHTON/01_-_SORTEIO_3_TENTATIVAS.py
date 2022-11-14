#1 - Faça um programa que:

#a) Pegue um número aleatório entre 1 a 10

#b) Peça para o usuário adivinhar o número. Ele deverá tentar NO MÁXIMO 3 vezes - caso ele tente mais que isso o programa deverá mostrar: "Você não acertou o número. Ganhou 0 pontos"

#c) Para cada tentativa, caso não tenha acertado, o programa deverá mostrar se o número aleatório é mais alto ou mais baixo. Por ex, o número aleatório foi 4. O usuário digitou 6, então o programa deverá mostrar "O número aleatório é menor".

#d) No final, se o usuário acertou de primeira mostrar: "Você ganhou 100 pontos". Se foi na segunda tentativa mostrar: "Você ganhou 60 pontos". E se foi a terceira tentativa: "Você ganhou 30 pontos"






from random import randint
#from time import sleep

print('\n' + '\033[1;37m-=-'*18)
print('\033[34m    Vou pensar em um número aleatório entre 0 e 10')
print('\033[37m-=-'*18)
print('\033[4;97mVocê vai ter 3 chances para tentar advinhar...')

n = 1

try:
    while n == 1:   # ENQUANTO N =  1 CONTINUE O PROCESSO
        n1 = randint(0, 10)   # CÓDIGO PARA SORTEAR UM NÚMERO DE 'X 'ATÉ 'Y '
        n2 = int(input('\n\033[mEm que número eu pensei? '))
        if n2 > 10:    # CASO SEJA MAIOR QUE NUMERO 'Y' INFORME QUE É ERRADO 
            print('\n\033[4mNúmero Inválido')
            exit() 

        cont = 0      
        lim = 2
        while n1 != n2 and cont != lim:   # ENQUANTO O NÚMERO SORTEADO NÃO FOR O NÚMERO DIGITADO 
            if n2 < n1:  # SE O NÚMERO DIGITADO FOR MENOR QUE O NÚMERO SORTEADO 
                print('\033[1;31mERROU! É mais...')
            else:  # SE O NÚMERO DIGITADO FOR MAIOR QUE O NÚMERO SORTEADO 
                print('\033[1;31mERROU! É menos...')
            
            # INFORMAMOS QUE VOCE ERROU E CALCULA QUANTAS CHANCES VOCE AINDA TEM
            n2 = int(input('\033[m({} chances) Tente mais uma vez: '.format(lim - cont))) 
            
            
            if n2 > 10:
                print('\n\033[4mNúmero Inválido')
                exit()
            cont += 1
        if cont == 0 and n1 == n2:
            print('\033[1;32mACERTOU! Você Ganhou 100 Pontos Por Ter Acertado com {} Tentativa !'.format(cont+1))
        elif cont == 1 and n1 == n2:
            print('\033[1;32mACERTOU!Você Ganhou 60 Pontos Por Ter Acertado com {} Tentativas !'.format(cont+1))    
        elif cont == 2 and n1 == n2:
              print('\033[1;32mACERTOU!Você Ganhou 30 Pontos Por Ter Acertado com {} Tentativas !'.format(cont+1))
        elif cont == lim and n1 != n2:
            print(f'\033[1;31mSuas chances acabaram, você perdeu!\033[m)\n(O número que eu pensei era o {n1})\n')
        else:
            print(f'\033[1;32mACERTOU! Você precisou de {cont + 1} tentativas para vencer! ')
            
        
        print('''\033[1;37mVocê quer continuar jogando?\033[m
    [\033[36m1\033[m] Sim
    [\033[36m0\033[m] Não''')
        n = int(input('Digite a sua opção: '))
        if n != 0:
            while n != 0 and n != 1:
                print('''\033[4;31mResposta Inválida\033[m
    \033[1;37mVocê quer continuar jogando?\033[m
    [\033[36m1\033[m] Sim
    [\033[36m0\033[m] Não''')
                n = int(input('Digite a sua opção: '))
        print('\033[37m-'*25)
except ValueError:
    print('\033[4;31mResposta Inválida\033[m')
print('\033[mAté mais!')