'''
Una lista es una secuencia de elementos.
Se crea con []
'''

lista = ["Dario",33,9.5,True,"German",20.08]

print(lista)
print(lista[:])
print(lista[2])
print(lista[-1])
print(lista[0:3])
print(lista[3:])


lista.append("Vargas")
print(lista)

lista.insert(2,"Nadia")
print(lista)

lista.extend(["uno", 1 , .1, False ])
print(lista)

lista.remove(33)
print(lista)

lista.pop()
print(lista)


lista2 = ["tres", "cuatro"]

lista3 = lista2 + lista

print(lista3)

print(lista2 * 4)

lista4 = [2 , 1, 5, 4, 3]
print(lista4)

print(lista4.sort())

del lista4[0]
print(lista4)