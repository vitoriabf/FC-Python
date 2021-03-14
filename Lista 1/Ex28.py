n = input('Digite um número: ')
base = int(input('Escolha [2] Binário; [3] Ternária; [4]'))
n1 = int(n)

r = len(n)
s = 0

for i in range (0, r):
    s +=  int(n[i])* (base**i)

print (s)

