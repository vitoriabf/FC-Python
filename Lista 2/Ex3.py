'''Leia uma frase e imprima o total de vogais, o total de brancos e o total do resto'''

frase = input('Digite uma frase: ')
frase = frase.lower()
contV = contB = contR = 0

for i in range(0,len(frase)):
    
    if frase[i] in 'aeiou':
        contV += 1
        
    elif frase[i] in ' ':
        contB += 1
        
    else:
        contR += 1

print (f'Quantidade de vogais: {contV}.')
print (f'Quantidade de espaços em branco: {contB}.')
print (f'Quantidade do resto: {contR}.')