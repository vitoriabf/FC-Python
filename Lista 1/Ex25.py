'''Crie um algoritmo que leia as taxas de juros (r) de um financiamento price (1% é
igual a 0,01), os valores das parcelas (pmt) e o número de parcelas (n). Em seguida,
calcule o valor presente do financiamento que é feito pela seguinte fórmula: '''

r = (int(input('taxa de juros: '))/100)
pmt = float(input('digite o valor das parcelas: '))
n = int(input('número de parcelas: '))
soma = 0

for i in range (1, n+1):
    soma += (pmt/((1+r)**i))
print(f'O valor presente do financiamento é R${soma:.2f}.')

