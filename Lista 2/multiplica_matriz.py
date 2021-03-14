def multiplica(mat1,mat2):
    matriz = []
    if len(mat1[0]) == len(mat2):
        for i in range(0,len(mat1)):
            matriz.append([])
            for j in range(0, len(mat2[0])):
                matriz[i].append(0)
                for k in range(0, len(mat2)):
                    matriz[i][j] += mat1[i][k] * mat2[k][j]
        return matriz
    else:
        print('não foi possivel')
    return matriz


matriz = [[2,1,2],[1,2,1],[2,1,2]]
matriz1 = [[1,1],[2,2],[1,1]]

print(multiplica(matriz,matriz1))
matriz2 = multiplica(matriz,matriz1)
print(matriz2)
arq = open('teste.txt', 'w')
for i in range(len(matriz2)):
    for j in range(len(matriz2[0])):
        arq.write(str(matriz2[i][j]) + ' ')
    arq.write('\n')
arq.close()
