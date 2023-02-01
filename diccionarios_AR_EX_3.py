##Crear un programa para gestionar datos de los socios de un club, permitiendo:

##Cargar información de los socios en un diccionario para acceder por número
##de socio (CLAVE). Los datos a almacenar son: número, nombre y apellido, fecha de
##ingreso (ddmmaaaa), cuota al día (s/n)(VALOR). El programa debe iniciar con los datos
##de los socios fundadores ya cargados:

##Socio no1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
##Socio no2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
##Socio no3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
socios = {1:['Amanda Nunez', '17/03/2009', True], 2:['Barbara Molina', '17/03/2009',
True], 3:['Lautaro Campos', '17/03/2009', True], 4:['Maria Galeri', '13/03/2018', False],
5:['Estela Campos', '13/03/2018', True]}
for i,j in socios.items():
    print('#', i, j)

print('AGREGAR NUEVO SOCIO')    
numero = int(input('Numero de socio: '))
while numero != 0:
    nombre = input('Nombre de socio: ')
    fecha_ingreso = input('Fecha ingreso dd/mm/yyyy: ')
    cuotas_ok = input('Cuota al dia?...SI NO: ')
    if cuotas_ok == 'si':
        cuotas_ok = True
    else:
        cuotas_ok = False
    #agrega socio usando numero como clave y las otras variables entran como lista en valor
    socios[numero] = [nombre, fecha_ingreso, cuotas_ok]
    numero = int(input('Otro numero de socio: '))

##Informar cantidad de socios del club.
print('Cantidad de socios:',len(socios))

##Solicitar al usuario el número de un socio y registrar que ha pagado todas
#las cuotas adeudadas.
print('ESTADO DE CUOTAS')
numero = int(input('Numero de socio: '))
while numero != 0:
    if socios[numero][2] == True:
        print('Cuotas al dia')
    else:
        print('El socio adeuda cuotas')
    numero = int(input('Otro numero de socio: '))

##Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018,
#para indicar que en realidad ingresaron el 14/03/2018.
print('MODIFICAR FECHA DE INGRESO')
##for valor in socios.values():
##    if valor[1] == '13/03/2018':
##        valor[1] = '14/03/2018'
def modificarFecha(dicc, old_date, new_date):
    for valor in dicc.values():
        if valor[1] == old_date:
            valor[1] = new_date
    return dicc

fecha_vieja = input('Fecha vieja dd/mm/yyyy: ')
fecha_nueva = input('Fecha nueva dd/mm/yyyy: ')

socios = modificarFecha(socios, fecha_vieja, fecha_nueva)

##Solicitar el nombre y apellido de un socio y darlo de baja
#(eliminarlo del listado). del diccionario[clave]
def eliminarSocio(dicc, name):
    for clave, valor in dicc.items():
        if name == dicc[clave][0]:
            return dicc[clave]
        
nombre = input('Nombre de socio a dar de baja: ')
numero = eliminarSocio(socios, nombre)
del numero

        

##Imprimir el listado de socios completo.



























