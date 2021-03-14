'''Crie um algoritmo que calcule a soma dos primeiros 50 números pares. Os
primeiros números pares são: 2, 4, 6, ...'''
soma = 0
for i in range(0, 51, 2):
    print(i)
    soma += i
print(soma)