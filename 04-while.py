x = 0

while x < 10:
    print(x)
    x = x + 1


'''
Operacion de multiplicacion de a x b utilizando sumas
a = 3

b = 4

salida: 3 + 3 + 3 + 3 = 12  

'''

a = int(input('Numero 1: '))

b = int(input('Numero 2: '))


cadena  = ""

contador = 1

while contador <= b:
    cadena = cadena + str(a)
    if contador < b:
        cadena = cadena + "+"

    contador = contador + 1


cadena = cadena + "=" + str(a * b)
print(cadena)




    
