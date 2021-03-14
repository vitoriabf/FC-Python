'''Crie um algoritmo que calcule a soma dos N primeiros números inteiros ímpares e
positivos. O valor de N deve ser lido do usuário.'''
soma = 0
n = int(input('Digite um número: '))
for num in range (0, n):
    if num % 2 == 1:
        soma += num

print (f'A soma dos {n} primeiros números é igual a {soma}')
