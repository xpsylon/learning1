#Escribir una funcion que, dado un numero de DNI, retorne True si el numero es valido y False si no lo es.
#Para que un numero de DNI sea valido debe tener entre 7 y 8 digitos
def fnDNI(num):
    contadorDigitos = 0
    while num != 0:
        contadorDigitos += 1
        num //= 10
    return contadorDigitos == 7 or contadorDigitos == 8
#Es lo mismo que if contadorDigitos == 7 or contdorDigitos == 0, return True