lineas = 0
digitos = 0

titulos = input('Libro: ')

while titulos != '*':
    if titulos == '/':
        lineas += 1
        print('Linea completada. Hay', digitos, 'digitos en la linea')
        digitos = 0
    else:
        for i in titulos:
            if i in '0123456789':
                digitos += 1

    titulos = input('Otro libro: ')

print('La cantidad de lineas es', lineas)
        
