#Construye un programa que calcule el MCD (maximo comun divisor) entre dos
#numeros naturales. El MCD es el natural mas grande que divide a ambos.

#Si el usuario introduce un numero incorrecto el programa no se ejecuta y
#pide la reintroduccion de numeros validos.

check = True

while check:

    n1 = int(input('Primer numero natural: '))
    n2 = int(input('Segundo numero natural: '))

    mcd = False
    
    if n1 > 0 and n2 > 0 and n1 != n2:
        check = False
        print('OK')

        if n1 > n2:
            n1, n2 = n2, n1
            print(n1, n2)

        i = n1 #variable iteradora toma valor n1 xq el mcd no puede ser menor a
        #el.
#while not mcd es lo mismo que while mcd == False
        while not mcd and i >= 1: #se corta cuando mcd True
            if n1 % i == 0 and n2 % i == 0: #primera iteracion i = n1
                mcd = True
                print('El MCD de', n1, 'y', n2, 'es:', i)
                
            else:
                i -= 1# pasa aqui si if no es cierto. mcd continua false y
                #sigue el while
                
    else:
        if n1 == n2:
            print('Los numeros son IGUALES. Reintroduzcalos.')

        else:
            print('Numeros no VALIDOS. Reintroduzcalos.')

        
