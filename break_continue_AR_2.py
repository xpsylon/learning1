#OPCION CON CONTINUE Y BREAK (SIN ELSE):
frase = input('Frase: ')
letra = input('Letra para buscar su posicion: ')
i = 0 #counter

while i != len(frase): #mientras el len de la frase sea distinto de i
    if letra != frase[i]: #comienza en frase[0]
        print('Letra no encontrada en la posicion:', i)
        i += 1
        continue #vuelve al ppio del bucle. se puede reemplazar con un else
    print('Letra encontrada en la posicion:', i)#cuando se encuentra la letra
    break #rompe el bucle
print('Bye')



        

        
