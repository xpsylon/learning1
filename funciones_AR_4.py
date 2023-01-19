#De Programacion desde 0 AR, ejercicio 10.1
#idem funciones AR 3, pero agregamos:
#Mostrar la sumatoria de todos los numeros ingresados
# y la suma de sus digitos.


#Funcion sumar digitos ingresados:
def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma


#programa global:
sumatoria = 0
num = int(input('Ingrese un numero: '))
while num!= 0:
    print('Suma de digitos:', sumaDigitos(num))#por cada ingreso
    sumatoria += num
    num = int(input('Otro numero: '))
print('Sumatoria:', sumatoria)#variable global
print('Suma digitos sumatoria:', sumaDigitos(sumatoria))#misma funcion usando otro parametro

    
