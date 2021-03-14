'''Num frigorífico existem 90 bois. Cada boi traz preso em seu pescoço um cartão
contendo seu número de identificação e seu peso. Crie um algoritmo que escreva o
número e peso do boi mais gordo e do boi mais magro.
Além disso, responda: se houver dois ou mais bois com o mesmo peso, maior que
todos os demais, este algoritmo escreverá o número de qual deles?'''

boi = [0]*5
cartao = [0]*5
cont = contF = 0

for i in range (0,5):
    boi[i] = int(input('peso: '))
    cartao[i] = input('id: ')

contG = max(boi)
contM = min(boi)

for i in range (0,5):
    if contG == boi[i]:
        cont += 1
        cartG = cartao[i]
    if contM == boi[i]:
        contF += 1
        cartM = cartao[i]

print (f'Boi mais gordo: {contG} \n CardID: {cartG} \n Boi mais magro: {contM} \n CardID: {cartM} ')

print (f'Quantidade de boi gordo: {cont} \n Quantidade de boi magro: {contF}')