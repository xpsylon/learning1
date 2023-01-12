#Ejercicio 8.2 Programacion desde cero
#Leer codigo ajeno e interpretarlo.


frase = input('Frase: ')
#quita espacios ppio y final:
frase = frase.strip()
#dos contadores:
cantidad = 0
len_p_mas_larga = 0

#bucle externo principal:
#MIENTRAS la frase no esta vacia:
while len(frase) != 0:
    cantidad += 1 #sumar 1 al contador
    i = frase.find(' ')#encontrar posicion espacio vacio, devuelve index (entero).
                       #SOLO DEVUELVE PRIMERO ENCONTRADO
    if i != -1: #si i NO ES -1, o sea q HAY un espacio vacio. Devuelve -1 cuando .find es FALSE
        palabra = frase[0:i]#la primera palabra, desde ppio a i (espacio)
        #bucle interno.
        #MIENTRAS la posicion de i es menor q len frase AND i es espacio vacio
        while i < len(frase) and frase[i] == ' ':
            i += 1 #sumar una posicion para chequear eliminar espacio vacio y arrancar desde primera letra 2da palabra.
        #fuera del bucle interno:
        frase = frase[i:] #ahora frase es 1 letra 2da palabra (i+1) hasta final. para ir encontrando TODOS los espacios
    else: #si no hay espacio vacio(i == -1)
        palabra = frase #frase pasa a llamarse palabra. logico, frase de una sola palabra
        frase = '' #frase queda valor vacio

    if len(palabra) > len_p_mas_larga: #si el len de la primera palabra es mayor que 0, len_palabra_mas_larga va tomando el mayor valor a medida que pasa el bucle
        len_p_mas_larga = len(palabra)
        p_mas_larga = palabra #cambio nombre variable para mayor claridad.

#ya fuera del bucle principal:
if cantidad > 0: # o sea que SI el bucle WHILE ppal al menos computo 1 palabra
    print('Palabra mas larga:', p_mas_larga)

print('Cantidad de palabras:', cantidad) # imprime aun si no se introdujo nada (0)
