'''Crie um algoritmo que calcule a soma dos primeiros 50 números pares. Os
primeiros números pares são: 2, 4, 6, ...'''
n = 0
soma = 0

while n <= 50:
    soma += n
    n += 2

print(f'A soma dos 50 primeiros números pares é {soma}')