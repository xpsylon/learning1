#Ejercicio mensaje

abc = 'abcdefghijklmnopqrstuvwxyz'
corrimiento = int(input('Introduce el corrimiento: '))

for j in range(5):
    mensaje = input('Mensaje: ')
    cripto = ''
    for i in mensaje:
        if i in abc:
            posicion = abc.find(i) #index original
            pos_cripto = (posicion + corrimiento) % 26
            cripto += abc[pos_cripto]
        else:
            cripto += i
    print('Cripto:', cripto)
 




