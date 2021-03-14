'''Uma empresa lançou um novo produto no mercado e fez uma pesquisa para saber
se os consumidores estavam satisfeitos, para isso eles deveriam responder sim ‘S’ ou
não ‘N’. Crie um algoritmo que leia a resposta de todas as pessoas e escreva a
porcentagem dos que disseram sim e dos que disseram não.
Obs: O final da leitura de dados é marcado pela resposta ‘F’'''

somaS = 0
somaN = 0
resposta = str(input('Digite S ou N: '))

while resposta != 'F':
    if resposta == 'S':
        somaS += 1
    else:
        somaN += 1

    resposta = str(input('Digite S ou N: '))

total = float(somaS + somaN)
if total != 0:

    print (f'Total de votos: {total}. \n Total de votos S: {(100*somaS) / total}%. \n Total' 
    f' de votos N {(100*somaN) / total}%.')

else:
    print('Não teve votos')



