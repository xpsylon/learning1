dicc_vacio = {}
dicc_vacio2 = dict()
dicc_elementos = {'hola':'hello', 'adios':'bye'}
#diccionario desde lista que contiene tuplas (clave, valor)
dicc_desde_contenedor = dict([('hola','hello'), ('adios','bye')])

calendario = [('enero', 1), ('febrero', 2), ('marzo', 3)]
meses = dict(calendario)
traducciones = {'hola':'hello', 'adios':'bye', 'dia':'day', 'noche':'night'}

#la clave debe ser unica pero los valores pueden tener el nivel de anidamiento que se necesite
equipo = {10: ['Javier', 60, 5], 8: ['Lucia', 45, 2], 5: ['Titus', 23, 2], 7: ['Asia', 52, 3]}

#solo python imprime los contenedores poniendo el nombre de la variable, para el resto de
#los lenguajes hay que iterar.
len(calendario) #cantidad de pares(clave, valor)--3 en este caso.

#retorno booleano
#para clave:
'hola' in traducciones
#u opcional
'hola' in traducciones.keys()
#para valor:
'bye' in traducciones.values()
#para verificar valor dentro de lista:
'Javier' in equipo[10]


##Obtener valor: diccionario [clave]  
meses['enero']
equipo[10][0]#el valor de equipo[10] es una lista, asi q [0] retorna 'Javier'
#diccionario.get (clave, valor). Valor es opcional y es lo que devuelve en caso q la clave
#no exista:
traducciones.get('reloj', 'clave no existe')

##Modificar valor: diccionario [clave]=nuevo valor
traducciones['adios'] = 'good bye'

##Agregar elemento: diccionario [clave] =valor. La clave va a ser nueva, obviamente.
traducciones['gracias'] = 'thank you'

##Agregar elementos: diccionario. update ((c1: v1, c2: v2, c3: v3})
meses.update({'abril':4, 'mayo':5, 'junio':6})

##Eliminar elemento: del diccionario [clave]. Elimina todo el par(clave:valor)
del meses['junio']

##Vaciar diccionario: diccionario.clear()
dicc_elementos.clear()


##dir(dict) muestra operaciones posibles con diccionarios
