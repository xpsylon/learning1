#Escribe un programa que, al recibir como dato un numero entero positivo N, calcule
#el resultado de la siguiente serie:

#1 + (1/2) + (1/3) + (1/4) + ....+ (1/N)

#Si el usuario escribe un numero incorrecto, el programa no se ejecuta y pregunta de nuevo
#por la informacion hasta que el dato ingresado sea correcto.

contador = 0 # variable donde se iran sumando los parciales por vuelta
check = True # para while-loop se vuelva a ejecutar hasta que se ingrese un num. correcto

while check == True:
    n = int(input('Numero: '))
    if n > 0:
        check = False #si se ingresa num. correcto, check pasa a ser False
        print('Numero ingresado correcto!')
        for i in range(1, n +1):
            print(1/i)
            contador += 1/i
            print('Contador por vuelta:', contador)
        print('Sumatoria:', contador)
       
    else:
        print('Numero ingresado incorrecto')
