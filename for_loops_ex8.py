#Construye un programa que, al recibir como datos N numeros naturales, determine cuantos de ellos son positivos, negativos o nulos.
#Si el usuario escribe un numero incorrecto, el programa no se ejecuta. En cambio, pregunta de nuevo por la informacion hasta que
#el dato ingresado sea correcto.

check = True
while check == True: #esto es para chequear SOLO  a q...

    q = int(input('Cantidad de numeros: '))

    if q > 0:
        check = False
        print('Numero correcto')

        counter_pos = 0 #la declaracion de los contadores va FUERA del loop
        counter_neg = 0
        counter_null = 0

        for i in range(q):
            n = int(input('Numero natural: '))

            if n > 0:
                print('Numero positivo')
                counter_pos += 1
                
            elif n == 0:
                print('Numero nulo')
                counter_null += 1

            else:
                print('Numero negativo')
                counter_neg += 1
    else:
        print('Numero incorrecto, reingreselo...')        
            
print('Numeros positivos:', counter_pos)
print('Numeros negativos:', counter_neg)
print('Numeros nulos:', counter_null)

