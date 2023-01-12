#Leccion 10.1 funciones de Programacion desde 0 AR

from funciones_AR import *

mayor = 0

numPrimo = int(input('Ingrese un numero primo: '))

while primo(numPrimo): #retorna bool de la funcion
    print('La suma de sus digitos es', suma_digitos(numPrimo))
    digitoGlobal = int(input('Ingrese un digito: '))
    print('La frecuencia de', digitoGlobal, 'es de', frecuencia(digitoGlobal, numPrimo))
    if numPrimo > mayor:
          mayor = numPrimo
    numPrimo = int(input('Otro numero primo: '))
print('El numero mayor es:', mayor, 'y su factorial es', factorial(mayor))
    
