n = int(input('Digite um número: '))
soma = 0
for j in range(1, n+1):
    for i in range (1, j):
        if j % i == 0:
            soma += i
    
    if soma == j:
        print(f'O número {j} é perfeito.')
    soma = 0