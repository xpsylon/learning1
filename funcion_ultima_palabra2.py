def fnUltimaPalabra(frase):
    longitud = len(frase)
    if longitud == 0:
        return 0
    cantidadLetras = 0
    for i in range(longitud): #se necesita indexar la cadena para poder tener acceso al valor del 
        #siguiente caracter en la misma iteracion.
        if frase[i] != ' ': #si NO ES un espacio vacio. OJO que i es un int
            #asi que usarlo como index de frase
            cantidadLetras += 1
        else:
            if frase[i] == ' ' and i < (longitud - 1) and frase[i+1] != ' ':
            #si ES un espacio vacio y NO LLEGO al final de la cadena y el SIGUIENTE caracter NO es un espacio vacio...
                cantidadLetras = 0
    return cantidadLetras
#LOGICA:
#Si se encuentra en un espacio vacio previo a la siguiente palabra, pone el contador a
#cero para en la siguiente iteracion, donde va a encontrar un caracter, empieza a contar
#otra vez.