'''Crie um algoritmo que leia 2 números inteiros positivos, A e B, e que calcule a soma
de todos os números múltiplos de 4 compreendidos entre eles. Os valores A e B não
devem ser considerados no somatório. Caso A seja maior do que B deve ser enviada
uma mensagem para o usuário informando que a soma não será realizada.'''

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))

soma = 0

if a > b:
    print('A soma não será realizada.')
else:
    for num in range(a+1, b):
        if num % 4 == 0:
            soma += num
    print (f'A soma dos múltiplos de 4 compreendidos entre {a} e {b} é {soma}')
