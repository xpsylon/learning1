suma = 0
n = int(input('Numero positivo: '))

#cualquier numero ingresado menor a 10 cortara el bucle luego de 1 vuelta.
while n != 0:
    digito = n % 10 #resto numero ingresado dividido 10. ultimo digito de n...
    print(digito)
    suma += digito #se incrementa con el resto anterior
    print(suma)
    n = n // 10 #n toma valor n dividido 10 cociente sin resto
    print(n)

print('Suma de los digitos: ', suma)
