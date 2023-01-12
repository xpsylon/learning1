#Escribe un programa que, al recibir como dato un numero entero N, obtenga el resultado
#de la siguiente serie:
#1^1 - 2^2  + 3^3 -...(+-) N^N
#Si el usuario escribe un numero incorrecto, el programa no se ejecuta.
#En cambio, pregunta de nuevo por la informacion hasta que el dato sea correcto.
check = True
while check == True:

    n = int(input('Numero entero: '))
    counter = 0
    if n > 0:
        check = False

        for i in range(1, n+1):
            i **= i
            print(i)
            if i % 2 == 0:
                counter -= i
            else:
                counter += i
        print('Resultado final:', counter)
    else:
        print('Ingrese un numero mayor que 0...')
    
