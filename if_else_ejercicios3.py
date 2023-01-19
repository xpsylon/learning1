#RECONOCIMIENTO VOCALES
letra = input('Ingrese una letra: ')
letra = letra.lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Es vocal')
elif len(letra) != 1:
    print('Por favor ingrese UN caracter')

print('bye')

#otra variante para lenguajes que no tienen 'elif':
letra1 = input('Ingrese una letra: ')
letra1 = letra1.lower()

if len(letra1) != 1:
    print('Por favor ingrese UN caracter!')
else:
    if letra1 in 'aeiou':
        print('Es vocal')

print('bye')

#variante pyhton con 'if'...'in'...:
letra2 = input('Ingrese una letra: ')
letra2 = letra2.lower()

if len(letra2) != 1:
    print('Por favor ingrese UN caracter!')
elif letra2 in 'aeiou':
        print('Es vocal')

print('bye')

