def longLastWord(frase):
    palabra = ''
    while frase != '':
        frase = frase.strip()#hola jose bananas
        espacio = frase.find(' ')#retorna posicion
        if espacio != -1:
            frase = frase[espacio + 1:]
        else:
            palabra = frase
            frase = ''
    return palabra

        
    
