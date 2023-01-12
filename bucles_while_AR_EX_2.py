#Crear un programa que solicite el ingreso de numeros enteros positivos, hasta que el usuario
#ingrese el 0. Por cada numero informar cuantos digitos pares y cuantos impares tiene.
#Al final, informar la cantidad de digitos pares y de digitos impares leidos en total.

total_pares = 0
total_impares = 0
numero = int(input('Ingrese un numero positivo (0 para terminar): '))

while numero != 0:
    if numero < 0:
        print('Ingrese un numero MAYOR a 0!: ')
    else:
        if numero % 2 == 0:
            total_pares += 1
        else:
            total_impares +=1       
    numero = int(input('Ingrese otro numero positivo (0 para terminar): '))
print('El numero de pares es', total_pares, 'y de impares', total_impares)
        
