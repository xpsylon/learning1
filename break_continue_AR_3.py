#OPCION CON ELSE Y BREAK (SIN CONTINUE)
frase = input('Frase: ')
letra = input('Letra para buscar su posicion: ')
i = 0 #counter

while i != len(frase): #mientras el len de la frase sea distinto de i
    if letra != frase[i]: #comienza en frase[0]
        print('Letra no encontrada en la posicion:', i)
        i += 1
    else:
        print('Letra encontrada en la posicion:', i)
        break #si no hay break, aunque la encuentre vuelve al loop.
print('Bye')


        

        
