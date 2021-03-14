'''35. Jogo da subtração. Seu algoritmo deverá ler uma variável positiva T e
posteriormente mais três variáveis positivas S1, S2 e S3, sendo que estas variáveis são
obrigatoriamente menores que T. O jogo consiste de dois jogadores, J1 e J2. A cada
rodada a variável T é subtraída por uma das variáveis S1 ou S2 ou S3, escolhida pelo
jogador da rodada. Perde o jogo quando o jogador ao executar sua subtração, obtém
um valor menor do que zero. O seu programa deve apontar o jogador VENCEDOR'''

T = int(input('Digite um número: '))
s1 = int(input('Digite um número: '))
s2 = int(input('Digite um número: '))
s3 = int(input('Digite um número: '))
var = [s1, s2, s3]
j1 = False
j2 = False


while T >= 0:
    jogada = int(input('Jogador1 faça a sua jogada [1/2/3]: '))
    T = T - var[jogada-1]
    if T < 0:
        j1 = True
        break
    jogada = int(input('Jogador2 faça a sua jogada [1/2/3]: '))
    T = T - var[jogada-1]
    if T < 0:
        j2 = True
        break

if j1:
    print('Jogador 2 venceu')
if j2:
    print('Jogador 1 venceu')

