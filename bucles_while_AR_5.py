pares = 0
n = int(input('Numero (-1 para terminar el programa): ' ))

while n != -1: #se ejecuta mientras no se ingrese -1
    if n % 2 == 0: #si n es par
        pares += 1 #se va sumando 1 a la variable pares
    suma = 0 #inicializacion de variable
    while n != 0:
        digito = n % 10 #ultimo digito de n
        suma += digito #se agrega a suma para sumar los digitos
        n = n // 10 #division sin resto para quitar el ultimo digito
    print('Suma de sus digitos:', suma)
    n = int(input('Otro numero (-1 para terminar el programa): '))
print('Se ingresaron', pares, 'numeros pares')
