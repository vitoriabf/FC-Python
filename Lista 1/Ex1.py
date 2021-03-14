somaf = 0
somam = 0
contF = 0
contM = 0
maiorSalario = 0

idade = int(input('Digite sua idade: '))

while idade >= 0:

    sexo = str(input('Digite seu sexo: '))
    salario = int(input('Digite seu salario: '))

    if sexo == 'f':
        somaf += salario
        contF += 1

    elif sexo == 'm':
        somam += salario
        contM += 1

    if idade < 30 and salario > maiorSalario:
        maiorSalario = salario

    idade = int(input('Digite sua idade: '))

if maiorSalario != 0:
    print(f'Maior salario de pessoas com menos de 30 anos é {maiorSalario}')
else:
    print('Maior salario de pessoas com menos de 30 anos é 0')

if contF != 0:
    print(f'A media salarial das mulheres é {somaf/contF}')

if contM != 0:
    print(f'A media salarial dos homens é {somam/contM}')

print('Saiu do programa')