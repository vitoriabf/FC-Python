'''def fatorial(fat):
    if fat == 0:
        return 1
    return fat*fatorial(fat-1)
                
fat = int(input('num: '))    
print(fatorial(fat))'''


fat = int(input('num: '))
fatorial = 0
cont = fat
while cont >= 0:
    fatorial += fat * fat-1
    cont-=1
print(fatorial)
