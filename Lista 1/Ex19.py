'''Crie um algoritmo que leia um número N e imprima os N primeiros números
primos.'''

primo = True
primos = []

n = int(input('digite um numero: '))

for i in range(2, n):
    for j in range (2, i):
        if (i%j) == 0 :
            primo = False
    
    if primo == True:
        primos.append(i)
    primo = True

print(primos)