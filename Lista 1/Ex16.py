nome = ''
altura = m1 = m2 = 0
cont = conT = 1

while nome != 'MARIA':
    
    nome = str(input('Digite nome '))
    altura = float(input('Digite sua altura '))
    
    if altura == m1:
        cont+=1
    if altura == m2:
        conT +=1

    if (altura > m1) and (m1 > m2):
        m2 = m1
        m1 = altura
        conT = cont
        cont = 1

    if altura > m1:
        m1 = altura

    if (m2 < altura < m1):
        m2 = altura
        conT = 1
    
print (f'Quantidade da Primeira maior: {cont} Qntidade Segunda maior: {conT}')
print(f'Primeira maior: {m1} \n Segunda maior: {m2}')