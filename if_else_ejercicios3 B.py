#RECONOCIMIENTO VOCALES
check = True
while check:
    letra = input('Ingrese una letra: ')
    letra = letra.lower()

    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        check = False
        print('Es vocal')
    elif len(letra) != 1:
        print('Por favor ingrese UN SOLO caracter')
    elif letra not in 'abcdefghijklmnopqrstuvwxyz':
        print('Ingrese UNA LETRA!')
    else:
        check = False
        print('No es vocal')


print('bye')

