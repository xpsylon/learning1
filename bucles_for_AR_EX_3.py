#FIBONACCI

#primeros dos numeros de la sucesion. son fijos y los imprimimos
fibo1 = 0
fibo2 = 1
print(fibo1)
print(fibo2)

for i in range(8): #los 8 numeros que faltan
    fibo3 = fibo1 + fibo2
    print(fibo3)
    #moviendo un espacio a la derecha
    fibo1 = fibo2
    fibo2 = fibo3

positivos = 0
negativos = 0
count_pos = 0
promedio_positivos = 0


for i in range (6):
    numero = int(input('Numero: '))
    if numero < 0:
        negativos += numero
    else:
        count_pos += 1
        positivos += numero
        if positivos > 0:
            promedio_positivos = positivos / count_pos
        
print(count_pos)
print('Sumatoria negativos', negativos)
print('Sumatoria positivos', positivos)
print('Promedio positivos', promedio_positivos)



