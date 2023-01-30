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

#itero por las claves:
for clave in traducciones.keys():
    print(clave)
#diccionario.keys() y diccionario.values() son listas:
traducciones.keys()
traducciones.values()
equipo.keys()
equipo.values()
traducciones.items()
equipo.items()

#itero por los valores:
for valor in traducciones.values():
    print(valor)

#itero por valor usando la clave como indice: diccionario[clave]
for clave in traducciones.keys():
    print(traducciones[clave])

#itero por clave Y valor utilizando items:
for clave, valor in traducciones.items():
    print(clave, valor)

#itero por clave y valor usando indices:
for par in traducciones.items():
    print(par[0], par[1])

#itero por los subvalores de valor:
for dato in equipo.values():
    print('nombre:', dato[0], 'edad:', dato[1], 'antiguedad:', dato[2])
    
    

