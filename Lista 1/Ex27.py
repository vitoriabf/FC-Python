'''Crie um algoritmo que verifique se existe alguma raiz na equação Ax
3 + Bx2 + Cx+D no intervalor [-1.000, 1.000]. Seu algoritmo deve ser os coeficiente A, B, C e D.
Dica: incremente o valor de x de uma unidade a cada interação e verifique se houve
uma mudança de sinal no resultado da equação, se o sinal mudou, existe a ocorrência
de uma raiz (não é necessário calcular a raiz).'''

import math

A = int(input('digite um número: '))
B = int(input('digite um número: '))
C = int(input('digite um número: '))
D = int(input('digite um número: '))
i = -1000
n1 = ((A*(i**3)) + (B*(i**2)) + (C*i) + D) 
for i in range (-999, 1001):
    n2 = ((A*(i**3)) + (B*(i**2)) + (C*i) + D)
    if n1 * n2 <= 0:
        print('Tem raiz')
        print(i)
        break

    else:
        n1 = n2
