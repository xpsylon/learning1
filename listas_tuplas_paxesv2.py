#Programa que permite procesar datos de paxes en una lista de tuplas con la siguiente forma: (nombre, dni, destino).
#En otra lista de tuplas se almacena: (ciudad, pais).
#Menu iterativo que permita:
from funciones_ARv2 import *
pasajeros = [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")]
ciudades = [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Lisboa", "Portugal"), ("Liverpool", "Inglaterra"), ("Madrid", "Espania")]
while True:
    print('1. Agregar pasajero')
    print('2. Agregar ciudad')
    print('3. Buscar ciudad de destino mediante DNI')
    print('4. Cantidad de pasajeros que viajan a una ciudad')
    print('5. Pais de destino mediante DNI')
    print('6. Cantidad de pasajeros que viajan a pais')
    print('7. Fin del programa')

    opcion = int(input('Ingrese el numero de opcion a ejecutar: '))

    if opcion == 1:
        print('AGREGAR PASAJEROS')
        pasajeros = agregarPasajero(pasajeros) #funcion que tiene como parametro la lista de pasajeros y los agrega a esa misma lista
    elif opcion == 2:
        print('AGREGAR CIUDADES')
        ciudades = agregarCiudad(ciudades) #funcion que tiene como parametro la lista de ciudades y los agrega a esa misma lista
    elif opcion == 3:
        dni = int(input('DNI: '))
        print('El pasajero viaja a:', buscarCiudad(pasajeros, dni)) #retorna ciudad
    elif opcion == 4:
        ciudad = input('Ciudad: ')
        print('A', ciudad, 'viajan', cantidadPasajerosCiudad(pasajeros, ciudad), 'pasajeros') #retorna q paxes
    elif opcion == 5:
        dni = int(input('DNI: '))
        print('El pasajero viaja a', paisDestino(pasajeros, ciudades, dni)) #retorna pais de destino. Necesita 3 parametros.
    elif opcion == 6:
        pais = input('Pais: ')
        print('Viajan', cantidadPasajerosPais(pasajeros, ciudades, pais), 'pasajeros')
    elif opcion == 7:
        break
    else:
        print('Opcion invalida')
            
