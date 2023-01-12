#VALOR ABSOLUTO NUMEROS
numero = int(input('Introduce un numero entero: '))

if numero < 0:
    numero *= -1

print('El valor absoluto es', numero)

#COINCIDENCIA LETRAS NOMBRES
nombre1 = input('Ingresa un nombre: ')
nombre2 = input('Ingresa otro nombre: ')

if nombre1[0] == nombre2[0]:
    print('Hay coincidencia')
elif nombre1[-1] == nombre2[-1]:
    print('Hay coincidencia')
else:
    print('No hay coincidencia')

#variante
nombre3 = input('Ingresa un nombre: ')
nombre4 = input('Ingresa otro nombre: ')

if nombre3[0] == nombre4[0] or nombre3[len(nombre3)-1] == nombre4[len(nombre4)-1]:
    print('Hay coincidencia')
else:
    print('No hay coincidencia')

