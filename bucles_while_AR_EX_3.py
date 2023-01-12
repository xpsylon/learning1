#Crear un programa que solicite el ingreso de numeros enteros positivos, hasta que el usuario
#ingrese el 0. Por cada numero informar cuantos digitos pares y cuantos impares tiene.
#Al final, informar la cantidad de digitos pares y de digitos impares leidos en total.

total_pares = 0
total_impares = 0

numero = int(input('Ingrese un numero positivo (0 para terminar): '))

while numero != 0:
    dig_par = 0
    dig_odd = 0
    while numero != 0:
        digito = numero % 10
        if digito % 2 == 0:
            dig_par += 1
        else:
            dig_odd += 1
        numero = numero // 10
    print('Numero con', dig_par, 'digitos pares y', dig_odd, 'digitos impares')
    total_pares += dig_par
    total_impares += dig_odd
    numero = int(input('Ingrese OTRO numero positivo (0 para terminar): '))
print('Se ingresaron un total de', total_pares, 'digitos pares y', total_impares, 'digitos impares.')
    


    
    
