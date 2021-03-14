'''Ler um vetor de números inteiros de 30 posições. Depois, ler um número inteiro X,
imprimir quantas vezes o número X aparece no vetor.'''
vet = [0]*30
for i in range(len(vet)):
    vet[i] = int(input('num: '))
busca = int(input('num buscar: '))
cont = 0
for num in vet:
    if num == busca:
        cont += 1
print(cont)

    