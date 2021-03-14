'''Crie a função multiplica_matriz(mat1, mat2) que deve retornar o produto de duas
matrizes bidimensionais genéricas, sem alterar as matrizes originais. A função deve
imprimir uma mensagem de erro e retornar um vetor vazio ([]) caso não for possível
realizar o produto das duas matrizes.'''
def produto(mat1, mat2):
    novaMatriz = [[0,0],[0,0]]
    if len(mat1) == len(mat1[0]) and len(mat1) == len(mat2[0]) and len(mat1) == len(mat2):
        for j in range(0, 2):
            for i in range(0,2):
                print(i,j)
                elem = 0
                for k in range(0,2):
                    elem += (mat1[i][k] * mat2[k][j])
                novaMatriz[i][j] = elem


    return novaMatriz
      
mat = [[3,1],[2,1]]
mat3 = [[6,2],[2,2]]

print(produto(mat, mat3))
    
