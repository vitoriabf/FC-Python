def transposta(mat):
    trans = []
    for i in range(0,len(mat[0])):
        trans.append([])
        for j in range(0,len(mat)):
            if i == j:
                trans[i].append(0)
                trans[i][j] = mat[i][j]
            else:
                trans[i].append(0)
                trans[i][j] = mat[j][i]
    return trans

matriz = [[1,0,1]]
print(transposta(matriz))
