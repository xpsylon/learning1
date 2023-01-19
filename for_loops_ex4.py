#SUCESION DE FIBONACCI:
#La sucesion comienza con los numeros 0 y 1 y, a partir de ahi, cada elemento es la suma
#de los dos numeros anteriores de la secuencia.
#0,1,1,2,3,5,8,13,21,34,55

#imprimir los 10 primeros numeros de la sucesion de fibonacci:

#sabemos que los 2 primeros numeros son 0 y 1
n1 = 0
n2 = 1
#asi que los imprimimos:
print(n1)
print(n2)

#ahora buscamos los 8 restantes:
for i in range(8): #la iteracion va del 0 al 7
    n3 = n1 + n2 #en la primera iteracion buscamos el tercer numero (suma de los 2 anteriores)
    print(n3) #y lo imprimimos...
    #ahora la secuencia se mueve un lugar a la derecha...
    n1 = n2
    n2 = n3
    #y se vuelve a iterar...
    
