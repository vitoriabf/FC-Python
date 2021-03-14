'''Leia um vetor de 40 posições e conte quantos elementos pares se encontram no
vetor.'''
cont = 0
vetor = [0]*5
for i in range(0,5):
    vetor[i] = int(input('Digite um numero: '))
print(vetor)
for i in range (0, 5):
    if vetor[i] % 2 == 0:
        cont+=1

print(cont)