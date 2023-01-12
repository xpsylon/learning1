#BUCLE WHILE (indeterminado):
#while 'condicion':
    #cuerpo del bucle
#el cuerpo del bucle se repite mientras la condicion sea verdadera

import math

i = 1

while i <= 3:
    print('ejecucion #', i)
    i += 1
   
print('end loop')

#programa chequeo edad:
edad = int(input('Por favor introduce tu edad: '))

while edad < 5 or edad > 100:
    print('Tu edad es erronea. Vuelve a intentarlo')
    edad = int(input('Por favor reintroduce tu edad: '))

print(f'Tu edad es {edad} anios. Puedes pasar!')

#programa raiz cuadrada:
intro = 'programa de raiz cuadrada'
print(intro.upper())

numero = int(input('Introduce un numero: '))
            
contador = 0
while numero < 0:
    print('No se puede sacar raiz de numeros negativos')

    if contador == 2:
        print('Demasiados intentos. El programa finaliza')
        break
    numero = int(input('Introduce un numero POSITIVO: '))

    if numero < 0:
        print('Numero negativo!')
        contador += 1


#si no pones contador < 2, cuando sale del while luego de tres intentos fallidos, entra aqui para intentar sacar
#la raiz cuadrada de un numero negativo.

if contador < 2: 
    #print('La raiz cuadrada de', numero, 'es', math.sqrt(numero))
#seria mas elegante crear una variable para la solucion antes de imprimir:
    solucion = math.sqrt(numero)
    print('La raiz cuadrada de', numero, 'es', solucion)


                 
            
                 
    
    

