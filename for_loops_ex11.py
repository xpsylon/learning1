#Un numero N es primo si es mayor que 1 y los unicos enteros positivos que lo dividen son 1 y N.
#Construye un programa que lea un numero entero positivo N y escriba todos los numeros
#primos menores a dicho numero.

#Si el usuario escribe un numero incorrecto el programa no se ejecuta. En cambio pregunta
#de nuevo por la informacion hasta que el dato ingresado sea correcto.

check = True
while check: #mismo que check == True

    n = int(input('Numero entero positivo: '))

    if n > 0:
        check = False
        print('Numero valido')

        for i in range(2,n): #los primos son mayores a 1.
            esPrimo = True #variable bool dentro del for-loop
            creciente = 2 #variable que se va a ir incrementando. Divisor de i

            #mientras divisor menor q dividendo en cada loop
            #while se ejecuta mientras esPrimo sea True y divisor < dividendo
            while esPrimo == True and creciente < i:
                if i % creciente == 0: #si es divisible (division exacta)
                    esPrimo = False #no es primo. El while no se ejecuta
                else:
                    creciente += 1 #si no es divisible con el primer divisor
                    #ir aumentando en 1 por cada loop (por cada i)
                    #aqui solo varia creciente, i se mantiene igual
            if esPrimo: #si esPrimo es True al final de while (en cada iteracion de i)
                print(i, 'es primo') #imprime los numeros primos menores a n
                
    else:
        print('Numero incorrecto. Reingreselo')
