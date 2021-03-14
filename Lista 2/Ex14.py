import math
n = int(input('num: '))
soma = 0
for i in range(1, n):
    if (i % 2) == 1:
        soma += (1/(i**2))
    else:
        soma -= (1/(i**2))
result = math.sqrt((12*soma))
if result < 0:
    pass
else:
    print (result)