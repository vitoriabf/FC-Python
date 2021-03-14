contI = 0
contP = 0
somaP = 0

n = int(input('Digite um numero: '))

while n != 0:

    if n % 2 == 1:
        contI += 1
    else:
        contP += 1
        somaP += n

    n = int(input('Digite um numero: '))

if contP != 0:
    print(f'A média aritmética de números pares é {somaP/contP}')
    print(f'A quantidade de números pares é igual a {contP}')

if contI != 0:
    
    print(f'A quantidade de números ímpares é igual a {contI}')

print ('Fim do Programa')

