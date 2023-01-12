#Programa que solicite ingreso cantidad indeterminada de numeros mayores que 1, finalizando
#cuando se reciba un 0.
#Imprimir la cantidad de numeros primos ingresados.
count_primos = 0
numero = int(input('Numero: '))

while numero != 0: #con 0 corta el programa
    esPrimo = True #arrancamos suponiendo que los numeros son primos
    for i in range(2, numero): #iteramos entre 2 y numero-1
        if numero % i == 0: #si hay algun divisor con resto exacto
            esPrimo = False
            print(numero, 'no es primo')
            break #rompemos la iteracion for
    if esPrimo: #no paso a False durante la iteracion for
        count_primos += 1
        print(numero, 'es primo')
         
    numero = int(input('Otro numero: ')) #ingresar numeros hasta que usuario corte con 0
print('Ha ingresado', count_primos, 'numeros primos')
print('Bye')

