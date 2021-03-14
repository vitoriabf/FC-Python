'''Faça um programa para ler 50 valores de temperaturas em graus Celsius.
Transformar essas temperaturas em Farenheit e imprimir a media das temperaturas
em Celsius e Farenheit e quantas temperaturas ficaram acima da media em Farenheit.'''
cont = 0
celsius = [0.0]*50
farenheit = []
for i in range(0,5):
    celsius[i] = float(input('Digite temperatura em Celsius: '))

for i in range (0, 50):
    f = (((celsius[i]*9)/5) + 32)
    farenheit.append(f)
    
media = ((sum(celsius)+sum(farenheit))/100)
print (media)

for i in range (0,50):
    if farenheit[i] > media:
        cont += 1

print (f'Quantidade de temperaturas em Farenheit que ficaram acima da média: {cont}.')