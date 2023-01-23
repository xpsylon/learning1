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



#FUNCIONES DE listas_tuplas_paxes.py
#agrega pasajeros a la lista y la retorna
def agregarPasajero(pasajeros):
    nombre = input('Pasajeros "espacio vacio para cortar": ')
    while nombre != '':
        dni = int(input('DNI: '))
        ciudad = input('Ciudad a la q viaja: ')
        pasajeros.append((nombre, dni, ciudad))
        nombre = input('Otro pasajero: ')
    return pasajeros

#agrega ciudades a la lista y la retorna
def agregarCiudad(ciudades):
    ciudad = input('Agregar ciudad "espacio vacio para cortar": ')
    while ciudad != '':
        pais = input('Pais')
        ciudades.append((ciudad, pais))
        ciudad = input('Otra ciudad: ')
    return ciudades

#dado dni pax, busca al pax en la lista y retorna la ciudad a la que viaja
#en la lista pasajeros tenemos tuplas (nombre, dni, ciudad)
def buscarCiudad(pasajeros, dni):
    for i in pasajeros:
        if dni == i[1]:
            return i[2]
    return 'dni not found'

#dada una lista de pax y una ciudad, retorna la q de pax q viajan 
#a esa ciudad
def cantidadPasajerosCiudad(pasajeros, ciudad):
    cantidad = 0
    for i in pasajeros:
        if ciudad == i[2]:
            cantidad += 1
    return cantidad 
    
#dada una lista de paxes, una de ciudades y un dni, retorna el pais al q viaja
#el pax con dicho dni.
def paisDestino (pasajeros, ciudades, dni):
    #usamos para encontrar primero la ciudad la funcion buscarCiudad
    #y la guardamos en variable:
    ciudad_buscada = buscarCiudad(pasajeros, dni)
    #y ahora con la ciudad encontrar el pais en la lista ciudades:
    for i in ciudades:
        if ciudad_buscada == i[0]:
            return i[1] #idem pais
    return 'i not found'

#dada una lista de paxes, una de ciudades y un pais, retorna la q de paxes q 
#viajan al dicho pais
def cantidadPasajerosPais(pasajeros, ciudades, pais):
    for i in ciudades:
        if pais == i[1]:
            ciudad = i[0]
    return cantidadPasajerosCiudad(pasajeros, ciudad)
    
