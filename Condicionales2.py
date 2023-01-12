edad_usuario = int(input('Introduce tu edad: '))

if edad_usuario < 18: 
    print('No puedes pasar')
if edad_usuario > 100:
    print('Edad erronea')
else:
    print('Puedes pasar') #solo puede ir un else por if. Si hay mas de 1 if y un solo else, este ultimo se refiere
    # a su if inmediato superior

#edad: 36
#if 1: no cumple
#if 2: no cumple
#else: cumple

#edad: 101
#if 1: no cumple
#if 2: cumple
#else: no cumple

#edad: 15
#if 1: cumple
#if 2: no cumple
#else: cumple xq el else se refiere al if 2, entonces la ejecucion salta del if 1 al else

#manera correcta:
edad_usuario = int(input('Introduce tu edad: '))

if edad_usuario < 18:
    print('No puedes pasar')
elif edad_usuario > 100:
    print('Edad incorrecta')
else:
    print('Puedes pasar')

#otra manera:

edad_usuario1 = int(input('Introduce tu edad: '))

if edad_usuario1 > 18 and edad_usuario1 <= 100:
    print('Puede pasar')
elif edad_usuario1 > 100:
    print('Edad erronea')
else:
    print('No puede pasar')


#otra opcion: creando funcion:
edad = int(input('Introduce tu edad: '))
def edad_usuario(x):
    acceso = 'Puede pasar'
    if edad < 18:
        acceso = 'No puede pasar'
    return acceso
print(edad_usuario(edad))
















































    


    
