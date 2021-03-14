'''Crie um algoritmo que leia um número N e imprima se ele é perfeito ou não. Um
número é perfeito quando a soma dos seus divisores é igual a ele mesmo, e.g., 6 = 3 +
2 + 1.'''

n = int(input('Digite um número: '))
soma = 0
for i in range (1, n):
    if n % i == 0:
        soma += i

if soma == n:
    print(f'O número {n} é perfeito.')
else:
    print(f'O número {n} não é perfeito.')
