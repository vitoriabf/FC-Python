precos = []
nome = []
p = -1
n = 'a'

while n != 'XXX':
    n = input('nome produto: ')
    p = float(input('preço: '))
    nome.append(n)
    precos.append(p)

for i in range (0, len(precos)):
    if precos[i] > p:
        p = precos[i]
        n = i
print(f'O produto mais caro é: {nome[n]}.')
