from file_functions import *
numeroMayorSumatoriaDigitos = 0 #la sumatoria mayor 
cantidadNumerosSumMenorDiez = 0

numero = int(input('Numero: '))

while numero >= 0:
    #guardamos retorno funcion en variable para no llamar tantas veces a la funcion (recursos):
    sumatoriaDigitos = suma_digitos(numero)
    if sumatoriaDigitos > numeroMayorSumatoriaDigitos:
        numeroMayorSumatoriaDigitos = sumatoriaDigitos
        numeroMayor = numero #el numero con mayor sumatoria
    if sumatoriaDigitos < 10:
        cantidadNumerosSumMenorDiez += 1
    numero = int(input('Otro numero: '))
print('El numero de mayor sumatoria es', numeroMayor, 'y su sumatoria es', numeroMayorSumatoriaDigitos)
print('Hay', cantidadNumerosSumMenorDiez, 'numeros con sumatorias menores a 10')
