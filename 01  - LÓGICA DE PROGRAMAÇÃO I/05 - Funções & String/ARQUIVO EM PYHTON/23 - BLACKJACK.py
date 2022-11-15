#Super Desafio! - Faça um jogo de BlackJack usando funções: o BlackJack, ou Vinte e Um, é um jogo em que os jogadores podem comprar cartas livremente, enquanto tiverem menos de 21 pontos. No nosso jogo, o Ás vale um ponto; as cartas de 2 a 10 valem o número de pontos que elas representam; e Valete, Dama e Rei valem 10 pontos cada. Ganha o jogador que tiver o maior número de pontos, desde que este seja menor ou igual a 21. Nosso jogo deve ter as seguintes funções:

#a. Função principal: a função que vamos chamar para iniciar o jogo. Essa função não irá receber nem retornar nenhuma variável. Ela deve perguntar o número de jogadores participantes e o nome de cada um. Em seguida ela chama as outras funções do jogo.

#b. Função para criar o baralho: essa função deve criar um baralho (uma lista) com as cartas do baralho.

#c. Função para a jogada: essa função deve receber o nome do jogador que irá realizar a jogada e, caso ele ainda esteja ativo (tenha menos de 21 pontos e ainda não tenha desistido de comprar cartas) deve perguntar se ele quer comprar uma carta. Se ele responder que sim, a função deve chamar a próxima função para sortear uma carta e somar o valor retornado na pontuação do jogador; se ele responder que não, a função deve desativar o jogador para que ele não possa mais comprar cartas; Essa função só deve ser chamada enquanto houver jogadores ativos.

#d. Função para o sorteio: essa função retira uma carta aleatória do baralho e retorna o número de pontos que essa carta vale.

#e. Função verificação: verifica e indica qual/quais jogador/jogadores tem o maior número de pontos, que seja menor ou igual a 21.

#----------------------------------------------------------------------------------------------------------------------

# b. Função para criar o baralho: essa função deve criar um baralho 
# (uma lista) com as cartas do baralho.

# No nosso jogo, o Ás vale um ponto; as cartas de 2 a 10 valem o 
# número de pontos que elas representam; 
# e Valete, Dama e Rei valem 10 pontos cada

def criar_baralho():

    naipes = ['COPAS', 'OURO','PAUS','ESPADAS']
    #naipes = ['♥','♦','♣','♠']

    # inicializar meu baralho
    baralho = []

    for naipe in naipes:

        for i in range(1,14):
            
            # carta = [naipe, numero, valor]
            if i >= 2 and i <= 10:
                carta = [naipe, str(i), i]
            elif (i == 1):
                carta = [naipe, 'AS', 1]
            elif(i == 11):
                carta = [naipe, 'Valete', 10]
            elif(i == 12):
                carta = [naipe, 'Dama', 10]
            elif(i == 13):
                carta = [naipe, 'Rei', 10]
            
            baralho.append(carta)
    
    return baralho

import random

#numero = random.randint(1,10)
#print(numero)

def sorteio(baralho):
    # pop - removeu um item da lista e salvou em uma variável carta
    carta = baralho.pop(random.randint(0,len(baralho)-1))

    print(f'A carta sorteada foi {carta[1]} de {carta[0]} que vale {carta[2]} pontos ')

    return carta

# c. Função para a jogada: essa função deve receber 
# o nome do jogador que irá realizar a jogada e, 
# caso ele ainda esteja ativo (tenha menos de 21 pontos e ainda não tenha 
# desistido de comprar cartas) deve perguntar se ele quer comprar uma carta.
# responder que sim, a função deve chamar a próxima função para sortear uma 
# carta e somar o valor retornado na pontuação do jogador; 
# se ele responder que não, a função deve desativar o jogador para que 
# ele não possa mais comprar cartas; Essa função só deve ser chamada
#  enquanto houver jogadores ativos.

#jogador = [nome (string), ativo (booleano), pontuacao (inteiro)]

def jogada (jogador, baralho, mesa=False):
        
    if mesa:
        resposta = 'S'
    else:
        resposta = ''   

    while(resposta!= 'N' and resposta != 'S'):    
        resposta = input(f'Jogador {jogador[0]}, deseja comprar uma carta (S/N): ').upper()

    if resposta == 'S':
        carta = sorteio(baralho)

        jogador[2] += int(carta[2])

        if jogador[2] >= 21:
            jogador[1] = False
            print(f'O jogador {jogador[0]} não pode mais comprar cartas. Pontuação atual: {jogador[2]}')
        else:
            print(f'Pontuação atual do jogador {jogador[0]}: {jogador[2]}')
        
    else:
        print(f'O jogador {jogador[0]} decidiu não comprar mais cartas. Pontuação atual: {jogador[2]}')
        jogador[1] = False

        # jogador[1] = not jogador [2] > 21


        # e. Função verificação: verifica e indica qual/quais jogador/jogadores 
# tem o maior número de pontos, que seja menor ou igual a 21.

# jogador = nome, status, pontuacao

def pontuacao(jogadores):

    maior_pontuacao = []
    maior_jogador = []

    for jogador in jogadores:

        if jogador[2] <= 21:
            maior_pontuacao.append(jogador[2])
            maior_jogador.append(jogador[0])

    pontuacao_maxima = max(maior_pontuacao)

    for i in range(len(maior_pontuacao)):
        if (maior_pontuacao[i] == pontuacao_maxima):
            print(f'O jogador {maior_jogador[i]} teve a maior pontuação: {maior_pontuacao[i]}')

