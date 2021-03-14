'''Crie um algoritmo que leia um número N e verifique se ele é primo.'''

primo = True
n = int(input('num: '))
for i in range (2, n):
    if n%i == 0:
        primo = False
if primo:
    print ('é primo')
else:
    print('não é')
