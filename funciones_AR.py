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

def sumatoria(numeros):
    summa = 0
    for elemento in numeros:
        summa += elemento
    return summa

#funcion que retorna en una lista los numeros menores a un numero dado por el usuario de una
#lista anterior:
def numeros_menores(lista, limite):
    lista_menores_limite = []
    for i in lista:
        if i < limite:
            lista_menores_limite.append(i)
    return lista_menores_limite

#funcion que da el numero de apariciones de un numero en una lista. Tuplas (numero, frec):
def frecuencia_numero_lista(lista):
    lista_veces = []
    for i in lista:
        tupleta = (i, lista.count(i))
        if tupleta not in lista_veces:
            lista_veces.append(tupleta)
    return lista_veces
                   
    
                   
    
    



