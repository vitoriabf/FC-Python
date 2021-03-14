'''Jogo de dados. Dois jogadores estão confrontando-se entre si, usando dois dados,
numerados de 1 até 6 (dado RAND(5) + 1). 
Vence uma rodada quem obtiver o maior
número no lançamento. 

Entretanto, caso um jogador obtiver um lançamento com dois
dados iguais (por exemplo, 1 e 1, 2 e 2,....) e o outro jogador não, o jogador que tiver
lançado a dupla ganha. 

Caso os dois jogadores fizerem o lançamento e o resultado for
de duas duplas para os dois jogadores, ganha o jogador com a dupla maior. A disputa é
em 11 lançamentos. Indique o jogador vencedor ou se houve empate.'''
import random
dado = random.randint(1, 6)
dado1 = random.randint(1, 6)
cont = v2 = v1 = 0

while cont <= 11:
    print (f'Partida {cont}')
    jogador1 = []
    jogador2 = []
    #JOGADOR1
    dado = random.randint(1, 6)
    dado1 = random.randint(1, 6)
    jogador1.append(dado)
    jogador1.append(dado1)
    print(jogador1)
    #JOGADOR2
    dado = random.randint(1, 6)
    dado1 = random.randint(1, 6)
    jogador2.append(dado)
    jogador2.append(dado1)
    print(jogador2)

    if (jogador1[0] == jogador1[1]) and (jogador2[0] != jogador2[1]):
        v1 += 1
        print('Jogador 1 venceu')
    elif (jogador2[0] == jogador2[1]) and (jogador1[0] != jogador1[1]):
        v2 += 1
        print ('Jogador 2 venceu')
    elif (jogador2[0] == jogador2[1]) and (jogador1[0] == jogador1[1]) and (jogador1[0] > jogador2[0]):
        v1 += 1
        print('Jogador 1 venceu')
    elif (jogador1[0] == jogador1[1]) and (jogador2[0] == jogador2[1]) and (jogador1[0] < jogador2[0]):
        v2 += 1
        print ('Jogador 2 venceu')
    elif (jogador1[0] + jogador1[1]) > (jogador2[0] + jogador2[1]):
        v1 += 1
        print('Jogador 1 venceu')
    else:
        v2 += 1
        print ('Jogador 2 venceu')

    cont += 1

if v1 > v2:
    print('Jogador 1 venceu')
if v1 == v2:
    print('Empate')
else:
    print ('Jogador 2 venceu')