'''Crie um algoritmo de caixa eletrônico que lê a quantidade de dinheiro a ser sacado
e imprime a menor quantidade de notas a ser dada ao usuário. Assume-se que existam
notas de 50, 20, 10, 5 e 1. Imprimir também a quantidade de cada nota a ser dada ao
usuário. O final da leitura é marcado pelo valor 0 que não deve ser calculado.
Exemplo: 98 = uma nota de 50, duas notas de 20, uma nota de 5, e três notas de 1.'''
c = v = d = cn = u = 0
while True:
    din = int(input('Digite o valor que você quer sacar: '))
    if din == 0:
        break
    else:
        c = (din // 50)
        v = ((din%50)//20)
        d = ((din%50)%20)//10
        cn = (((din%50)%20)%10)//5
        u = ((((din%50)%20)%10)%5)//1

        print(f'qntd de notas: R$50[{c}], R$20[{v}], R$10[{d}], R$5[{cn}] e R$1[{u}].')



