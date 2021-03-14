'''Ver se uma palavra é palíndroma (fica igual de trás pra frente. Ex: ovo.) '''
palavra1 = ''
palavra = input('Digite uma palavra: ')
palavra2 = palavra
palavra = palavra.lower()

if (' ' in palavra):
    palavra = palavra.replace(' ', '')

for i in range(-1, -len(palavra)-1, -1):
    palavra1 += palavra[i]

if palavra == palavra1:
    print (f'A palavra/frase {palavra2} é Palíndroma.')
else:
    print (f'A palavra/frase {palavra2} não é Palíndroma')