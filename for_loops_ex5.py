#CREAR UN PROGRAMA QUE PERMITA GENERAR LA TABLA DE MULTIPLICAR:
#El numero debe ser un entero positivo. Si es negativo, debe dar error y la
#oportunidad de reingresar el numero.

check = True # creamos variable bool con valor inicial True

while check == True: # el programa se ejecuta mientras check sea True

    numero = int(input('Numero entero positivo: '))
    if numero > 0:
        check = False # false para parar la reejecucion del programa luego de
        #haber ingresado un numero correcto.
        for i in range(1, 11):
            print(numero, 'por', i, 'es igual a', numero * i)

    else:
        print('El numero ingresado no es correcto')
            
