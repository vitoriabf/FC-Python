'''Uma certa firma fez uma pesquisa para saber se as pessoas gostaram ou não de um
novo produto lançado no mercado. Para isso, forneceu o sexo do entrevistado e sua
resposta (sim ou não). Sabendo-se que foram entrevistadas 2.000 pessoas, crie um
algoritmo que calcule e escreva:

a) o número de pessoas que responderam sim; 

b) o número de pessoas que responderam não;a porcentagem de pessoas do
sexo masculino que responderam não.'''

contS = contN = cont = contM = 0

for i in range (0,2000):
    sexo = input('digite seu sexo: ')
    resposta = input('você gostou do produto? [S/N]')
    cont+= 1

    if resposta in 'Ss':
        contS += 1
    else:
        contN += 1

    if resposta in 'Nn' and sexo in 'Mm':
        contM += 1
print (f'Número de pessoas que responderam sim[{contS}]. \n Número de pessoas que responderam não[{contN}]. \n'
    f'A porcentagem de pessoas do sexo masculino que responderam não[{(100*contM)/cont}].')
    

