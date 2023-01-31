from funciones_AR import *

primaria = set()
secundaria = set()

print('ALUMNOS DE PRIMARIA')
#la profe lo guarda otra vez. para mi no es necesario.
primaria = cargarAlumnos(primaria)

print('ALUMNOS DE SECUNDARIA')
secundaria = cargarAlumnos(secundaria)

#print TODOS LOS ALUMNOS (inclusion). Se itera para que imprima nombre a nombre
print('NOMBRE DE TODOS LOS ALUMNOS')
for i in primaria | secundaria:
    print(i)

#INTERSECCION
print('NOMBRES COMUNES')
for i in primaria & secundaria:
    print(i)

#RESTA o DIFERENCIA de uno respecto a otro
print('NOMBRES DE PRIMARIA QUE NO ESTAN EN SECUNDARIA')
for i in primaria - secundaria:
    print(i)
