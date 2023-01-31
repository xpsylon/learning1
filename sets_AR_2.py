##12.0 Conjuntos - Curso de programación desde cero (con Python)

conjA = {1,2,3}
conjB = {1,2,3,1,2,3,1,2,3}#las copias son eliminadas.
lista1 = [1,2,3,1,2,3,1,2,3]
lista1 = set(lista1) #pasa a ser un set, elimina las copias y pisan el valor de
#lista1
##Crear conjunto a partir de otro contenedor: set (contenedor)
#conjC = set(listaH)


##Longitud: 1en (conjunto)
print(len(conjB))

##Pertenencia: elemento in conjunto
print(3 in conjB) #retorna bool
print(4 in conjB) #retorna bool, False
print(5 not in conjB)# True

##Agregar elemento: conjunto. add (elemento) ó conjunto. update (contenedor)
conjA.add(4)
#conjA.add(5,6) error! takes just one argument.
#conjA.update(5,6,7) TypeError: 'int' object is not iterable
#conjA.update(5) TypeError: 'int' object is not iterable
conjA.update([5,6,7])

##Eliminar elemento: conjunto. remove (elemento) ó conjunto.discard (elemento) Vaciar conjunto: conjunto.clear()
conjA.remove(5)
#conjA.remove(8) #da error si el valor no existe
conjA.discard(2)
conjA.discard(8)#no da error si el valor no existe

##Igualdad: conjunto1==conjunto2
#devuelve booleano
conjA == conjB #returns False

##Unión de conjuntos: conjunto1 | conjunto2
conjA | conjB #returns ALL elements BOTH set discarding the repeated ones.

##Intersección de conjuntos: conjuntol & conjunto2
conjA & conjB #returns ONLY elements which are in BOTH sets

##Inclusión: conjunto1<conjunto2, conjuntol>conjunto2
conjA < conjB #False, conjA is bigger
conjA > conjB #False as well, conjA doesnt have 2
#conjA.add(2) then conjA > conjB True

##Diferencia: conjuntol-conjunto2
conjA - conjB # 4,6,7, valores que estan en un set, pero no en el otro.
conjB - conjA # 2

##Diferencia simétrica: conjuntol^conjunto2
conjA ^ conjB
conjB ^ conjA
#es lo mismo, muestra los valores opuestos a la interseccion

##dir (set) muestra operaciones posibles con conjuntos




