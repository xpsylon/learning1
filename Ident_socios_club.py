from funciones_total import *
nombre = input('Ingrese su nombre: ')

while nombre != '':
    id_numb = int(input('Ingrese su DNI: '))

    while validar_dni(id_numb) == False:
        id_numb = int(input('El DNI tiene 7 u 8 digitos: '))

    numero_socio = identificador(nombre, id_numb)
    print(numero_socio)
    nombre = input('Siguiente nombre: ')