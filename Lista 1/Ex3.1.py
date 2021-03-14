nPar = []
nImpar = []
n = 1
while n != 0:
    n = int(input('digite um numero: '))
    if n == 0:
        break
    if n % 2 == 0:
        nPar.append(n)
    else:
        nImpar.append(n)
    

print (f'Qtd de par: {len(nPar)} \nQtd de impar: {len(nImpar)}')
if len(nPar) != 0:
    print(f'Media de num par: {sum(nPar)/len(nPar)}')