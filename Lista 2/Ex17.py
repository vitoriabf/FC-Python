'''Uma certa firma fez uma pesquisa para saber se as pessoas gostaram ou não de um
novo produto lançado no mercado. Para isso, forneceu o sexo do entrevistado e sua
resposta (sim ou não). Sabendo-se que foram entrevistadas 2.000 pessoas, crie um
algoritmo que calcule e escreva:
a) o número de pessoas que responderam sim;
b) o número de pessoas que responderam não;a porcentagem de pessoas do
sexo masculino que responderam não.
'''
contS = contN = contMN = 0

for i in range(0,5):
    sexo = input('sexo [F/M]: ')
    res = input('gostou do produto[S/N]: ')

    if sexo in 'Mm':
        contMN += 1

    if res in 'Ss':
        contS += 1
    if res in 'Nn':
        contN += 1
        
nome = (100*contMN)/(contS+contN)

print(contS, contN, nome)