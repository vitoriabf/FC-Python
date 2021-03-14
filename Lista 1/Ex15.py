'''Num frigorífico existem 90 bois. 
Cada boi traz preso em seu pescoço um cartão
contendo seu número de identificação e seu peso. 

Crie um algoritmo que escreva o
número e peso do boi mais gordo e do boi mais magro.
Além disso, responda: se houver dois ou mais bois com o mesmo peso, maior que
todos os demais, este algoritmo escreverá o número de qual deles?'''

boiM = boiG = 0
cartM = cartG = cartG1 = ''
contG = 1

for i in range(0,5):

    ID = input('Digite o número de ID: ')
    peso = float(input('Digite o peso: '))

    if peso == boiG:
        cartG += ', '
        cartG += ID
        contG += 1
        cartG1 = ID
    
    if peso > boiG:
        boiG = peso
        contG = 1
        cartG = ''
        cartG = ID

    if (peso < boiM) or (boiM == 0):
        boiM = peso
        cartM = ID

cartG = cartG.split(',')

if contG >= 2:
    print(f'O boi mais gordo é o {cartG1}: {boiG}kg e o boi mais magro é o {cartM}: {boiM}kg \n Mais de um boi têm o mesmo peso e são os: {cartG}'
    f'total de {contG}.')

else:
   print (f'O boi mais gordo é o {cartG1}: {boiG}kg e o boi mais magro é o {cartM}: {boiM}')