#buscar el menor numero ingresado:
menor = -1
n = int(input('Numero: '))

while n != 0: #la condicion de corte es que n sea cero
    if n < menor: 
        menor = n 
    n = int(input('Otro numero: '))

print('Menor numero ingresado:', menor)
