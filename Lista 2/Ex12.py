import random
n = 4*(10**6)
cont = 0
for i in range (n):
    x = random.randint(0,2)
    y = random.randint(0,2)
    if ((x**2) + (y**2)) <= 4:
        cont += 1
result = (cont / (10**6))
print(result)
