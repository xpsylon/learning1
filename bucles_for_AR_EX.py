#Escribir un programa que muestre la sumatoria de todos los numeros entre el
#0 y el 100.
#Que modificacion habria que hacer si ahora solo se deben sumar los numeros que
#sean multiplos de 3?

sumatoria = 0
for i in range (101):
    sumatoria += i
print(sumatoria)

sumatoria1 = 0
for i in range (101):
    if i % 3 == 0:
        sumatoria1 += i
print(sumatoria1)
 
