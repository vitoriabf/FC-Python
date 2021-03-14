'''Leia um vetor de 16 posições e troque as 8 primeiras posições pelas 8 últimas
posições. Imprima o vetor original e o vetor trocado'''
vet = [0]*16
for i in range(len(vet)):
    vet[i] = int(input('num: '))
print(vet)
for j in range(8):
    vet[j], vet[j+8] = vet[j+8], vet[j]
print(vet)