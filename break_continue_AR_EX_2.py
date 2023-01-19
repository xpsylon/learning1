#Imprimir anios bisiestos y multiplos de 10 en un rango dado por usuario.

anio1 = int(input('Ingrese un anio: '))
anio2 = int(input('Ingrese otro anio: '))

#if anio2 > anio1:
for i in range(anio1, (anio2+1)):
    if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0) and i % 10 == 0:
        print(i)
            
        
print('Bye')

#Usando el codigo mas limpio con continue:

anioInicial = int(input('Año inicial: '))
anioFinal = int(input('Año final: '))

for i in range(anioInicial, anioFinal + 1):
    if not i % 10 == 0:
        continue
    if not i % 4 == 0:
        continue
    if not i % 100 == 0 or i % 400 == 0:
        print(i)
            
