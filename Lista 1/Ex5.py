'''Crie um algoritmo que imprima o peso total que será carregado por um caminhão.
Sabe-se que este caminhão carrega 25 caixas. O peso de cada caixa deve ser informado
pelo usuário.'''

soma = 0

for pos in range(1,26):
    peso = int(input(f'Insira o peso da caixa {pos}: '))
    soma += peso

print (f'O peso total que será carregado pelo caminhão é {soma}')
