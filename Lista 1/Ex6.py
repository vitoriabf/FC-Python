'''Crie um algoritmo que leia a quantidade e o preço de 50 produtos comprados por
uma empresa. Ao final deve ser escrito o total gasto pela empresa.'''

total = 0
for i in range (0,5): #muda o 5 para 50
    preço = int(input('Digite o preço do produto: '))
    total += preço
print(f'o total de produtos é igual a {total}')