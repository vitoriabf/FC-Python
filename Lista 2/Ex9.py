'''Crie uma matriz 5x5 com 1 na diagonal principal e 0 nas outras posições. Imprima a
matriz no formato tradicional de linhas e colunas'''
def formatoTradicional(matriz):
    for linha in matriz:
        print(tuple(linha))

ma = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
print(formatoTradicional(ma))