#5
#Generar e imprimir una nueva lista que contenga como elementos a tuplas,
#cada una compuesta por un numero de la lista original y la cantidad de veces
#que aparece en ella.

#Repetimos lista original:
numero = int(input('Numero: '))
lista = []
while numero != 0:
    lista.append(numero)
    numero = int(input('Otro: '))
print(lista)

lista_veces = []
for elemento in lista:
    tupleta = (elemento, lista.count(elemento))
    if tupleta not in lista_veces:    
        lista_veces.append(tupleta)
print(lista_veces)


