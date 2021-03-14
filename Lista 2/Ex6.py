'''Um palíndromo é uma cadeia que pode ser lida de frente para trás e de trás para
frente. Ex: ‘SOMOS’ ‘1234321’. Implemente a função palindromo(palavra). O
parâmetro palavra é uma string. A função deverá retornar True se for um palíndromo e
False caso contrário.'''
def palindromo(palavra):
    palavraof = palavra
    palavra = palavra.lower()
    newPalavra = ''
    if ' ' in palavra:
        palavra = palavra.replace(' ', '')
    
    for i in range(-1, -len(palavra)-1, -1):
        newPalavra += palavra[i]
    print(newPalavra)
    if palavra == newPalavra:
        return (f'{palavraof} é Palíndroma')
    else:
        return (f'{palavraof} não é Palíndroma')

frase = input('Escreva uma frase: ')

print(palindromo(frase))



