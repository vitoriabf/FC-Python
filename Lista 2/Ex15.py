'''Escreva uma função para condensar os elementos de uma lista ordenada L, que
contém inteiros repetidos. Por exemplo, para L = [3, 3, 3, 3, 7, 7, 13, 13, 23], a função
retorna ['3^4', '7^2', '13^2', '23'] (repare que são strings). Note-se que no caso de um
número aparecer uma única vez, não deve haver expoente unitário.
'''
L = [3, 3, 3, 3, 7, 7, 13, 13, 23]
lis = []
n = 0
cont = 0

while n <= len(L)-1:
    if n == len(L)-1:
        lis.append(L[n])
        n += 1
    else:
        for i in range(n, len(L)):
            if L[n] == L[i]:
                cont += 1
                
        lis.append(str(L[n]) + '^' + str(cont))
        n += cont
        cont = 0
print(lis)
    