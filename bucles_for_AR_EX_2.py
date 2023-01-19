#dado un numero, mostrar su factorial.
#El factorial se obtiene multiplicando todos los numeros enteros positivos
#que hay entre el 1 y ese numero.

factorial = 1

numero = int(input('Numero: '))

if numero != 0:
    for i in range (1, numero +1):
        factorial *= i
print(factorial)

