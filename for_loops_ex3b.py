#SUCESION DE FIBONACCI
#Crear un algoritmo qie muestre los primeros 10 numeros de la sucesion de Fibonacci.
#Dicha sucesion comienza con los numeros 0 y 1 y, a partir de estos, cada elemento
#es la suma de los dos numeros anteriores en la secuencia:
num1 = 0 #variables con los dos primeros numeros de la sucesion.
num2 = 1
print(num1) #los imprimimos y ya tenemos 8 de los 10...
print(num2)

for i in range(8): # la i va a iterar por el 0 al 7, los 8 numeros que faltan
    num3 = num1 + num2 # a partir del 3 numero la secuencia empieza a ser la
    #suma de los 2 anteriores
    print(num3) #imprimimos el 3er numero
    #ahora los numeros se mueven un lugar a la derecha, para seguir con la secuencia
    num1 = num2
    num2 = num3
    
