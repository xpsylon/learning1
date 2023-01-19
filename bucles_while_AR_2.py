#buscar el mayor numero ingresado:
mayor = -1
n = int(input('Numero positivo: '))

while n >= 0: #la condicion de corte es que n sea negativo
    if n > mayor: #arrancaria con n = 1 xq si es 0 no hay bucle y mayor es = -1
        mayor = n # mayor toma el valor de n si el ultimo input de n es > q mayor
    n = int(input('Otro numero positivo: '))

print('Mayor numero ingresado:', mayor)
