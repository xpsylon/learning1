#Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel
#primario de una escuela, finalizando al ingresar 'x'. A continuacion, solicitar
#que ingrese los nombres de alumnos de nivel secundario, finalizando al ingresar
#'x'.
primarios = set()
secundarios = set()

nombre_prim = input('Nombre alumno primaria: ')
while nombre_prim != 'x':
    primarios.add(nombre_prim)
    nombre_prim = input('Otro nombre de primaria: ')

nombre_sec = input('Nombre alumno secundaria: ')
while nombre_sec != 'x':
    secundarios.add(nombre_sec)
    nombre_sec = input('Otro nombre de secundaria: ')

##Informar los nombres de todos los alumnos de nivel primario y los de nivel
##secundario, sin repeticiones.
print('Alumnos de primaria:', primarios)
print('Alumnos de secundaria:', secundarios)



##Informar que nombres se repiten entre los alumnos de nivel primario y los de
##secundario
nombres_repetidos = primarios & secundarios
print('Los nombres que se repiten son:', nombres_repetidos)

##Informar que nombres de nivel primario no se repiten en los de nivel secundario
nombres_primario_no_secundario = primarios - secundarios
print('Nombres unicos de primario:', nombres_primario_no_secundario)

##Informar que nombres de nivel primario no se repiten en los de nivel secundario
nombres_secundario_no_primario = secundarios - primarios
print('Nombres unicos de secundario:', nombres_secundario_no_primario)
