'''. Faça a fatoração de um numero A inteiro, que é uma entrada do usuário. (leitura).
Supondo, por exemplo, que A seja igual a 12, sua saída de ser:
2 ^ 2
3 ^ 1'''
primo = True
primos = []
div = []

n = int(input('digite um numero: '))

for i in range(2, n):
    for j in range (2, i):
        if (i%j) == 0 :
            primo = False
    
    if primo == True:
        primos.append(i)
    primo = True

cont = 0
while n != 1:

    if (n % primos[cont]) == 0:
        div.append(primos[cont])
        n = (n / primos[cont])

        if n % primos[cont] == 0:
            continue       
        else:
            cont += 1
    else:
        cont += 1
            
print(div)



