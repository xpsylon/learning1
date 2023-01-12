#similar al ejercicio anterior, solo que agregandole una seleccion (if):
positivos = 0 #variable cantidad de positivos
total = 0 #variable suma de positivos
n = int(input('Numero (0 para terminar): '))
while n != 0: #mientras input distinto de 0
    if n > 0: #si mayor que 0
        positivos += 1
        total += n
    n = int(input('Numero (0 para terminar): '))
print('Suma de positivos:', total)
print('Cantidad de positivos', positivos)


