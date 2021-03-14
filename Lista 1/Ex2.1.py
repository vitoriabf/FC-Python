pt = int(input('primeiro termo: '))
r = int(input('razao: '))
n = int(input('n primeiros termos: '))

for i in range(1,n):
    print((pt +((i-1)*r)))
