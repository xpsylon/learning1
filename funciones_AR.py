#Solicitar ingreso numeros primos
#Lectura finaliza cuando ingreso no primo

#Mostrar suma digitos cada numero
#Solicitar digito y mostrar frecuencia

#Al finalizar programa mostrar factorial mayor numero ingresado.



def primos(numero):
    num_primo = True
    for i in range (2, numero):
        if numero % i == 0:
            num_primo = False
            break
    return num_primo #retorna True o False

#version mas elegante funcion primos:
def primo(numero):
    for i in range (2, numero):
        if numero % i == 0:
            return False
    return True
            
def suma_digitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

def frecuencia(digito, numero):
    cantidad = 0
    while numero != 0:
        dixit = numero % 10
        if dixit == digito:
            cantidad += 1
        numero //= 10
    return cantidad

def factorial(numero):
    f = 1
    for i in range(1, numero +1):
        f *= i
    return f
    