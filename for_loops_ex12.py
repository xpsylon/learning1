#Construye un programa que, al recibir como datos dos numeros enteros
#positivos, obtenga e imprima todos los numeros primos gemelos comprendidos
#entre dichos numeros.
#Los primos gemelos son una pareja de numeros primos con una diferencia
#entre si de exactamente dos. El 3 y el 5 son primos gemelos.

#Si el usuario escribe un numero incorrecto, el programa no se ejecuta.
#En cambio, pregunta de nuevo por la informacion hasta que el dato
#ingresado sea correcto.

check = True
while check:

    n1 = int(input('Numero entero positivo: '))
    n2 = int(input('Otro numero entero positivo: '))


    if n1 > 0 and n2 > 0:
        check = False
        print('Numeros correctos')
        for i in range(n1, n2+1):
            #start values:
            esPrimo = True
            creciente = 2 #divisor de i
            while esPrimo and creciente < i:
                if i % creciente == 0:
                    esPrimo = False
                else:
                    creciente += 1
            if esPrimo:
                print(i)


    else:
        print('Numeros no validos. Reingreselos...')
