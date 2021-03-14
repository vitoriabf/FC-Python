'''Crie um algoritmo que escreva os N primeiros termos de uma progressão aritmética
(PA). O primeiro termo e a razão da PA devem ser informados pelo usuário'''

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

print(a1, end = " ")

for N in range (1, 8):
    
    a1 = a1 + r
    print (f'{a1}', end = " ")

print('\n Fim do programa')