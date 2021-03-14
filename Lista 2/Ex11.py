'''Crie a função mat_maior_10(matriz). A função deve receber uma matriz genérica,
de qualquer tamanho (não necessariamente quadrada) e retornar a quantidade de
elementos da matriz maiores que dez.'''

def matMaior10(matriz):
    cont = 0
    for i in range(0,len(matriz)):
        for j in range(0, len(matriz)):
            if matriz[i][j] > 10:
                cont += 1
    return cont

mat = [[0,10],[45,10]]

print (matMaior10(mat))