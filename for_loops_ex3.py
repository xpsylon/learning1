#FACTORIAL
#El factorial de un numero se obtiene multiplicando todos los numeros enteros
#positivos que hay entre el 1 y ese numero.
#El factorial de 0 es 1.

numero = int(input('Numero entero positivo: '))
factorial = 1 #contador arranca en 1 xq factorial 0 es 1

if numero != 0: # porque factorial de 0 es 1.
    for i in range(1, numero + 1): # numero + 1 xq el range incluye el num. anterior.
        print('#', i)
        factorial = factorial * i
        print('Factorial vuelta:', factorial)

print('Factorial total', factorial)



 
