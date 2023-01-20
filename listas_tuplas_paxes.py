#Programa que permite procesar datos de paxes en una lista de tuplas con la siguiente forma: (nombre, dni, destino).
#En otra lista de tuplas se almacena: (ciudad, pais).
#Menu iterativo que permita:
pasajeros = []
ciudades = []
while True:
    print('1. Agregar pasajero')
    print('2. Agregar ciudad')
    print('3. Buscar ciudad de destino mediante DNI')
    print('4 Cantidad de pasajeros que viajan a una ciudad')
    print('5. Pais de destino mediante DNI')
    print('6. Pasajeros que viajan a pais')
    print('7. Fin del programa')

    opcion = int(input('Ingrese el numero de opcion a ejecutar'))