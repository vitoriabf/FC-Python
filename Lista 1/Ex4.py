'''Crie um algoritmo que leia os nomes e os preços dos produtos de uma loja e que
escreva o nome do produto mais caro. Considere que o final da lista é marcado pelo
produto ‘XXX’ e que não existem preços repetidos.'''

nome = str(input('Digite o nome do Produto: '))
preçoMC = 0
nomeMaisCaro = ' '
while nome != 'XXX':
    preço = int(input('Digite o preço do produto: '))

    if preçoMC < preço:
        nomeMaisCaro = nome
        preçoMC = preço
    nome = str(input('Digite o nome do Produto: '))

if preçoMC != 0:
    print(f'O produto mais caro é {nomeMaisCaro}')

print('Programa Encerrado')
