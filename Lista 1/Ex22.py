'''Crie um algoritmo que leia um número N e calcule:'''

n = int(input('Digite um número: '))
soma = 0

for i in range (1,n):
    soma += (1/i)

print(f'{soma:.2f}')
