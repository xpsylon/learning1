#Solicitar al usuario que ingrese numeros, los cuales se guardaran en una
#lista. Finalizar al ingresar el numero 0, el cual no puede guardarse.

numero = int(input('Numero: '))
lista = []
while numero != 0:
    lista.append(numero)
    numero = int(input('Otro: '))

#A continuacion, solicitar al usuario que ingrese un numero y, si el numero esta en
#la lista, eliminar su primera ocurrencia. Mostar mensaje si no es posible eliminar.

num_borrar = int(input('Numero a eliminar: '))
if num_borrar in lista:
    lista.remove(num_borrar)
else:
    print('El numero', num_borrar, 'no se encuentra en la lista')

#Imprimir la sumatoria de todos los numeros de la lista.
sumatoria = 0
for elemento in lista:
    sumatoria += elemento
print('Sumatoria lista:', sumatoria)

#Solicitar al usuario otro numero y crear una lista con los elementos de la lista original
#que sean menores al numero dado. Imprimir esta nueva lista, iterando por ella.
num_mayor = int(input('Ingrese otro numero: '))
lista_menor = []
for valor in lista:
    if valor < num_mayor:
        lista_menor.append(valor)
print('Lista menores:', lista_menor)
        
    
