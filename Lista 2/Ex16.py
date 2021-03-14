'''Leia e escreva o nome e a altura das moças inscritas em um concurso de
beleza, até que seja digitada o nome ‘MARIA’, que marca o final da lista, mas é
para ser computada no concurso.
b) Calcule e escreva as duas maiores alturas e quantas moças as possuem'''

lista = []
mA = mAA = cont = cont2 = 0
nome = ''
while nome != 'MARIA':
    nome = input('Digite nome da guria: ')
    altura = float(input('Digite altura da guria: '))

    if (altura >= mA) and (altura > mAA):
        if mA == altura:
            cont += 1
        else:
            if altura > mAA:
                mAA = mA
                cont2 = cont
            cont = 1
            
        mA = altura
        lista.append(altura)
    elif (altura < mA) and (altura >= mAA):
        if mAA == altura:
            cont2 += 1
        else:
            cont2 = 1
        mAA = altura
        lista.append(altura)
    nome = input('Digite nome da guria: ')
    
print(f'As duas maiores alturas são {mA} e {mAA} e {cont}, {cont2} as possuem respectivamente.')

    
