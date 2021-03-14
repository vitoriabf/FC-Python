'''a) Leia a idade de várias pessoas. O final da lista contém o valor da idade igual a
-1 que deverá ser computado.
b) Calcule e mostre a idade média desse grupo de indivíduos. Escreva também a
porcentagem de pessoas entre 21 e 65 anos inclusive'''

idade = soma = cont = conT = 0

while idade >= 0:
    idade = int(input('Digite sua idade: '))
    soma += idade
    conT += 1

    if (idade > 21) and (idade < 65):
        cont += 1

print (f'A média das idades é {(soma/conT)}. \n A porcentagem de pessoas entre 21 e 65 anos é {((100*cont)/conT)}%.')
    


