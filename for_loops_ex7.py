#Escribe un programa que, al recibir como dato un numero entero positivo N, calcule
#el resultado de la siguiente serie:

#1 / (1/2) * (1/3) / (1/4) * ....(*/) (1/N)

#Si el usuario escribe un numero incorrecto, el programa no se ejecuta y pregunta de nuevo
#por la informacion hasta que el dato ingresado sea correcto.

check = True
while check == True:
    n = int(input('Numero entero positivo: '))
    counter = 1
    if n > 0:
        check = False
        print('Numero correcto')
        for i in range(2, n+1):
            print('counter', counter) #solo para chequeo, no necesario.
            print(1/i) #solo para chequeo, no necesario.
            if i % 2 == 0: #si i es par....
                counter /= 1/i
            else:
                counter *= 1/ i
        print('Factor:', counter)
            


    else:
        print('Numero incorrecto. Ingreselo nuevamente')
