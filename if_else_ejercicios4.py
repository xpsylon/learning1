#AÑO BISIESTO
#es bisiesto si es:
#1 divisible por 4
#2 no divisible por 100 excepto que sea divisible por 400

anio = int(input('Introduzca un año: '))

if anio % 4 == 0 and anio % 100 != 0: #divisble por 4 y no divisible por 100
    print('Año bisiesto')
elif anio % 400 == 0: #divisible por 400
    print('AÑO BISIESTO')
else: #no divisble por 4, divisible por 100, no divisible por 400
    print('No es bisiesto')

print('bye')

#variante profesora, sin 'elif' para otros lenguajes aparte de phyton
anio1 = int(input('Introduzca un año: '))

if anio1 % 4 != 0: #no divisibles por 4 (no bisiestos)
    print('No es bisiesto')
else: #divisibles por 4
    if anio1 % 100 != 0 or anio1 % 400 == 0: # no divisibles por 100 o, si divisibles por 100, tambien divisibles por 400.
        print('Es bisiesto')
    else: # divisible por 4, divisible por 100, no divisible por 400
        print('No es BISIESTO')

print('bye') 
    


    
