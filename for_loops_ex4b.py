numerosPositivos = 0
numerosNegativos = 0
cantidadPositivos = 0
#Las tres variables arrancan en 0

for i in range(6): #itera 5 veces pidiendo los numeros
    num = int(input('Numero entero: '))
    if num >= 0:
        cantidadPositivos += 1
        numerosPositivos += num
    else:
        numerosNegativos += num

print(numerosNegativos)
print(numerosPositivos/cantidadPositivos)


        
        
