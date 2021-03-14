'''Crie um algoritmo para calcular a área de um triângulo qualquer, considerando que
são fornecidos os comprimentos dos seus lados. Esse programa não pode permitir a
entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.'''
import math
a = int(input('Digite o comprimento 1º: '))
b = int(input('Digite o comprimento 2º: '))
c = int(input('Digite o comprimento 3º: '))
p = (a + b + c)/2

if (a or b or c) <= 0:
    print('Não será possível fazer o cálculo.')
else:
    d = (p*(p-a)*(p-b)*(p-c))
    if d < 0:
        print('Essa raiz é menor que zero')
    else:
        d = math.sqrt(d)
        print(f'O valor da área do triângulo é {d}')


    

