def senha(palavra):
    palavracript = ''
    for i in range(0,len(palavra)):
        valorAscii = ord(palavra[i])
        if valorAscii % 2 == 0:
            valorAscii -= 1
        else:
            valorAscii += 1
        valorChar = chr(valorAscii)
        palavracript += valorChar
    return palavracript

pal = input("palavra:")
print (f'senha: {senha(pal)}')

        
        
