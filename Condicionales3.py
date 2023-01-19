#if elif else

nota = int(input('Introduce tu nota: '))

if nota < 4:
    print('Insuficiente')
if nota < 6:
    print('Suficiente')
if nota < 7:
    print('Bien')
if nota < 9:
    print('Notable')
else:
    print('Sobresaliente')

#sale mal porque por ejemplo 3 es a la vez < a 4, 6, 7 y 9. O sea que devuelve insuficiente, suficiente, bien y notabl
#a la vez.
#manera correcta con elif:
nota = int(input('Introduce tu nota: '))


if nota < 4:
    print('Insuficiente')
elif nota < 6:
    print('Suficiente')
elif nota < 7:
    print('Bien')
elif nota < 9:
    print('Notable')
else:
    print('Sobresaliente')
