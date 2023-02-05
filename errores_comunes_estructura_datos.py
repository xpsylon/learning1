#manera correcta de hacerlo a traves de una iteracion. en este caso creamos una
#funcion:
def empleadoExiste(dicc, name):
    for valor in dicc.values():
        if name == valor[0]:
            return True #al poner return la funcion termina
    return False #pero agregamos otro return para el caso que no encuentre el nombre



empleados = {100: ['Jorge Millan', 'Administracion'], 200: ['Oriana Lopez',
'Gerencia'], 300: ['Guadalupe Rios', 'RR.HH'], 400: ['Lionel Campos', 'Ventas']}
empleados[500] = 'Gino Bogani' #este es el unico npmbre que va a encontrar con in


nombre = input('Nombre empleado: ')
#aca no va a imprimir el nombre del empleado, porque .values solo itera en los valores,
#pero no en las listas dentro de ellos. Estamos comparando strings con listas.
#lo cual es un error:

##if not nombre in empleados.values():
##print('Empleado no esta en nomina')
##else:
##print('ESTAAAA')

if not empleadoExiste(empleados, nombre): #funcion retorna True, con not se hace False
    print('Empleado no en nomina')
else:
    print(nombre, 'esta en nomina')#funcion retorna False, pero al ser el else de un False
    #es True


