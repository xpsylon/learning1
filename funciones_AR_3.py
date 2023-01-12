#Solicitar numeros al usuario hasta que ingrese el 0
#Por cada uno, mostrar la suma de sus digitos.

#Funcion:
def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma


#programa global:
numero = int(input('Ingrese un numero: '))
while numero != 0:
    print('Suma de digitos:', sumaDigitos(numero))
    numero = int(input('Otro numero: '))
    
