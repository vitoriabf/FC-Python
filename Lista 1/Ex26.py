'''Crie um algoritmo que leia N números inteiros positivos e responda se é possível
formar um polígono com o mesmo (dica: maior número < soma dos demais números).'''
n1 = soma = 0
n = int(input('Quantos números você quer ler? '))
for i in range(0, n):
    x = int(input(f'Digite o {i+1}º número: '))
    if x > n1:
        n1 = x
    soma += x

soma -= n1
if n1 > soma:
    print('É possível formar um polígono: ')
else:
    print('Não é possível')