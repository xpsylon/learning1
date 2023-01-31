##Crear un programa para gestionar datos de los socios de un club, permitiendo:

##Cargar información de los socios en un diccionario para acceder por número
##de socio (CLAVE). Los datos a almacenar son: número, nombre y apellido, fecha de
##ingreso (ddmmaaaa), cuota al día (s/n)(VALOR). El programa debe iniciar con los datos
##de los socios fundadores ya cargados:

##Socio no1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
##Socio no2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
##Socio no3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
socios = {1:['Amanda Nunez', '17/03/2009', True], 2:['Barbara Molina', '17/03/2009',
True], 3:['Lautaro Campos', '17/03/2009', True]}
for i,j in socios.items():
    print('#', i, j)
numero = int(input('Numero de socio: '))
nombre = input('Nombre de socio: ')
fecha_ingreso = input('Fecha ingreso dd/mm/yyyy: ')
cuotas_ok = input('Cuota al dia?...SI NO: ')
if cuotas_ok == 'si':
    cuotas_ok = True
else:
    cuotas_ok = False

socios[numero] = [nombre, fecha_ingreso, cuotas_ok]
##Informar cantidad de socios del club.

##Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.

##Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018.

##Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).

##Imprimir el listado de socios completo.
