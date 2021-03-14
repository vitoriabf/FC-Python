'''Crie um algoritmo que apure os votos de uma eleição municipal, numa cidade com
20.000 eleitores, onde concorreram quatro candidatos. Um servidor da Justiça
Eleitoral digitará cada voto individualmente. Cada voto equivale a um número inteiro.
Os votos válidos podem ser 1, 2, 3 e 4, e estão relacionados aos seguintes candidatos:
1 – João da Silva
2 – José Ramalho
3 – Maria Mattos
4 – Pedro Américo
Votos com o valor 0 devem ser contabilizados como votos em branco, e votos com
qualquer outro valor (além de 0, 1, 2, 3 e 4), devem se considerados votos nulos.
Calcule e escreva o total de votos de cada candidato, o total de votos brancos e o total
de votos nulos'''
joao = 0
jose = 0
maria = 0
pedro = 0
branco = 0
nulo = 0

for vot in range(0,6):
    voto = int(input('Digite o número da pessoa que vai votar(0, nulo; 1, 2, 3 ou 4: '))

    if voto == 0:
        branco += 1
    elif voto == 1:
        joao += 1
    elif voto == 2:
        jose += 1
    elif voto == 3:
        maria += 1
    elif voto == 4:
        pedro += 1
    else:
        nulo += 1

print (f'Joao teve {joao} votos. \n Jose teve {jose} votos. \n Maria teve {maria} votos. \n Pedro teve {pedro}'
f' votos. \n Votos Nulos = {nulo}. \n Brancos = {branco}')

