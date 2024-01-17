'''
Una lista es una secuencia de elementos de diferente tipo*

Se declaran con corchetes 

[ ]
'''

lista1=["roberto",22,3.5,True,"Vargas",20,8]

print(lista1)
print(type(lista1))

'''Recorrer la Lista'''

print(lista1[:])
print(lista1[2])
print(lista1[-1])
print(lista1[0:3])
print(lista1[3:])

'''Agregar un elemento en la lista'''

lista1.append("Blancarte")
print(lista1)

lista1.insert(2,"Nadia")


'''Agregar una lista a la lista'''

lista1.extend(["Blancarte",1.1,False])


'''Eliminar elementos de la lista'''
lista1.remove(22)

'''eliminar el ultimo elemento de la lista'''
lista1.pop()

'''Sumar dos listas'''
lista2=["tres","cuatro"]
lista3=lista1+lista2

'''Multiplicar una lista'''
print(lista2 *4)

'''Ordenar Una lista'''
lista4=[2,1,5,3,4]
lista4.sort()

'''Eliminar un elemento de la lista basandoce en su indice'''

del lista4[0]
