#1
#Solicitar al usuario que ingrese numeros, los cuales se guardaran en una
#lista. Finalizar al ingresar el numero 0, el cual no puede guardarse.

numero = int(input('Numero: '))
lista = []
while numero != 0:
    lista.append(numero)
    numero = int(input('Otro: '))

#2
#A continuacion, solicitar al usuario que ingrese un numero y, si el numero esta en
#la lista, eliminar su primera ocurrencia. Mostar mensaje si no es posible eliminar.

num_borrar = int(input('Numero a eliminar: '))
if num_borrar in lista:
    lista.remove(num_borrar)
else:
    print('El numero', num_borrar, 'no se encuentra en la lista')

#3
#Imprimir la sumatoria de todos los numeros de la lista. SIN FUNCION:
##sumatoria = 0
##for elemento in lista:
##    sumatoria += elemento
##print('Sumatoria lista:', sumatoria)

#VERSION FUNCION:
from funciones_AR import *

print('Sumatoria', sumatoria(lista))

#4
#Solicitar al usuario otro numero y crear una lista con los elementos de la lista original
#que sean menores al numero dado. Imprimir esta nueva lista, iterando por ella.
num_mayor = int(input('Ingrese otro numero: '))
for n in numeros_menores(lista, num_mayor):
    print(n)

#5
#Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta
#por un numero de la lista original y la cantidad de veces que aparece en ella.
print('Frecuencias')
for cada_tupla in frecuencia_numero_lista(lista):
    #accediendo a las partes de cada tupla (5,2):
    print('El numero',cada_tupla[0], 'aparece', cada_tupla[1], 'veces')


        
    
