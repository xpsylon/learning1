print('Programa de acceso')

edad_usuario = int(input('Introduzca su edad: '))

if edad_usuario >= 18 and edad_usuario < 100:
    print('Acceso permitido')
elif edad_usuario >= 100:
    print('Edad erronea')
    int(input('Edad debe ser menor a 100, reintroduzca...: '))
else:
    print('Acceso denegado')
