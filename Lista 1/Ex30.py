div = []
a = int(input('digite um número: '))
b = int(input('digite um número: '))

if a > b:

    for i in range(2, a+1):
        if (a%i == 0) and (b%i == 0):
            div.append(i)

else:
    for i in range (2, b+1):
        if (a%i == 0) and (b%i == 0):
            div.append(i)

print(max(div))