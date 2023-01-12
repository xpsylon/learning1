#funcion que valida que el dni tenga 7 u 8 digitos:
def validar_dni(dni):
    counter = 0
    while dni != 0:
        dni //= 10
        counter += 1
    return counter == 7 or counter == 8

#funcion que da el len de la ultima palabra:
def lenUltimaPalabra(cadena):
    longitud = len(cadena) #int
    if longitud == 0: #int
        return 0
    counter = 0
    for i in range (longitud): #int
        if cadena[i] != ' ': #valor index 
            counter += 1
        else:
            if cadena[i] == ' ' and i < longitud-1 and cadena[i+1]!= ' ':
                counter = 0
    return counter   

#funcion que obtiene los primeros 3 digitos de un numero. Se obtiene dividiendo un 
#numero por diez sucesivamente hasta que tenga 3 digitos. O sea que es un while
#para numeros >= 1000:
def primerosTresDigitos(numero):
    while numero >= 1000:
        numero /= 10
    return int(numero) 

    

#funcion que obtiene el identificador del socio: nombre + len apellido
#(en este caso ultima palabra) + primeros 3 digitos del dni:
def identificador(nomb, id):
    nomb = nomb.strip()
    i = nomb[0:nomb.find(' ')] #desde ppio cadena hasta espacio vacio (vorname)
    i += str(lenUltimaPalabra(nomb))#como parametro se usa la variable de ESTA funcion
    i += str(primerosTresDigitos(id))
    return i