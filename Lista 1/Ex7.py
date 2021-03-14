'''Crie um algoritmo que leia 2 números inteiros positivos, A e B, e que calcule a soma
de todos os números compreendidos entre eles. Os valores A e B não devem ser
considerados no somatório. Caso A seja maior do que B deve ser enviada uma
mensagem para o usuário informando que a soma não será realizada'''

a = int(input('digite um numero:  '))
b = int(input('digite um numero:  '))

somaAB = 0

if a > b:
    print('A soma não será realizada.')

else:   
    for num in range(a+1, b):
        somaAB += num

    print(f'A soma entre dos números entre {a} e {b} é igual a {somaAB}')
