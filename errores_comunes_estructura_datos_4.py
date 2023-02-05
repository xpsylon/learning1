#NO MODIFICAR (AGREGAR O ELIMINAR) ELEMENTOS DURANTE LA ITERACION.

#Modificar la cantidad de elementos de la estructura que se esta iterando:
##a = [1,2,3,4]
##for i in range(len(a)):
##    if i == 2:
##        del a[3]
##    print(a[i])

#va a querer iterar al a[3] y habra sido eliminado. INDEX OUT OF RANGE.

#2
##b = {'a': [1, 2, 3], 'b': [], 'c': [8, 6], 'd': [], 'e':[4]}
##for clave in b.keys():
##    if b[clave] == []:
##        del b[clave]
#Runtime Error: dictionary changed size during iteration.


b = {'a': [1, 2, 3], 'b': [], 'c': [8, 6], 'd': [], 'e':[4]}
#list of the keys of dictionary b. es una copia de las claves originales
#del diccionario.
claves = list(b.keys())
#list with a single element, which is a view of the keys of dictionary b:
claves1 = [b.keys()]
#with list comprehension:
claves2 = [clave for clave in b.keys()]
##for clave in b.keys():
##    if b[clave] == []:
##        del b[clave]

#ahora, vamos a iterar por una lista, mientras que se elimina el elemento
#del diccionario. la lista es una copia de las claves del diccionario.
##for clave in claves:
##    if b[clave] == []:
##        del b[clave]
