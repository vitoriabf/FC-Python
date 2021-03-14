'''Implemente o jogo Blackjack ou 21. No caso temos apenas dois jogadores, o cliente
(humano) e a banca (computador). O ás pode valer 1 ou 11, de acordo com as cartas
que o jogador possui. O valete (J), a dama (Q) e o rei (K) valem 10. A simulação da
obtenção das cartas deve ser feita com o uso de números aleatórios
(Dica: carta  RAND(12) +1, isto é, variando de 1 a 13).'''
import random
#JOGADOR1
jogador1 = []
carta = random.randint(1, 13)
jogador1.append(carta)
carta = random.randint(1, 13)
jogador1.append(carta)

while True:
    escolha = input('Deseja receber outra cartar? [S/N]')
    if escolha in 'Ss':
        carta = random.randint(1, 13)
        jogador1.append(carta)
        for i in range (0, len(jogador1)):
            if ((jogador1[i]) == 11) or ((jogador1[i]) == 12) or ((jogador1[i]) == 13):
                jogador1[i] = 10

        break
    else:
        for i in range (0, len(jogador1)):
            if ((jogador1[i]) == 11) or ((jogador1[i]) == 12) or ((jogador1[i]) == 13):
                jogador1[i] = 10
        break
print('Jogador1')
print(jogador1)

     #COMPUTADOR
jogador2 = []
carta = random.randint(1, 13)
jogador2.append(carta)
carta = random.randint(1, 13)
jogador2.append(carta)
for i in range (0, len(jogador2)):
    if ((jogador2[i]) == 11) or ((jogador2[i]) == 12) or ((jogador2[i]) == 13):
        jogador2[i] = 10
print('Computador1')
print (jogador2)

if sum(jogador1) >= 21:
    print('O computador venceu')
    
elif sum(jogador2) >= 21:
    print('O jogador1 venceu')

elif (sum(jogador1)) and (sum(jogador2)) >= 21:
    print ('Empate')

elif sum(jogador1) == sum(jogador2):
    print ('Empate')

elif sum(jogador1) > sum(jogador2):
    print ('Jogador1 venceu')
        
else:
    print ('Computador venceu')

            
    
    
    
