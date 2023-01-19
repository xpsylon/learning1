#los bucles sirven para repetir lineas de codigo de manera eficiente.
#1-bucles determinados: FOR
#-bucles indeterminados: WHILE

#bucles for:
#por convencion la variable lleva la letra i.

for i in ['fio', 2, 3, 4]: #imprime la cantidad de veces como elementos tenga la lista.
    print('janis')

#para que imprima i (items de la lista):
for i in ['reloj', 48, True, 45j]:
    print(i)

#range() before python 3 was considered a function, since then it is considered an object type.

#for printing the loop in just one line we use the print parameter end=, which by default is set up to \n:
for i in ['Violencia', 'Sandwich', 3]:
    print('Fantasia', end = ' ')

kelly = (7, 1, 22)
print(kelly)

#probando de chequear direcciones de mail:

email = False #creamos variable booleana con valor inicial False

#ahora vamos a evaluar si el mail es correcto dependiendo de si lleva @ o no:

for i in 'xxx@psylongmail.com': #recorre email caracter a caracter
    if i == '@': # cuando llega a @, la variable se convierte en True. 
        email = True

if email == True: 
    print('email correcto')
else:
    print('email incorrecto')

#si queremos expresar que una variable booleana es igual a True, podemos poner solo la variable o sea:
#email == True o
#email

#con input:
email = False
miMail = input('Tu email...: ')

for i in miMail:
    if i == '@':
        email = True

if email:
    print('email correcto')
else:
    print('email incorrecto')

#ahora chequeamos ademas que el mail tenga un '.' aparte de la @. utilizamos un contador:

contador = 0 # arranca en cero...

miMail = input('Escriba su mail...: ')

for i in miMail: #itera...
    if i == '@' or i == '.': # si arroba OR punto
        contador += 1 #aumenta el contador en 1 (1 por @ y 1 por '.'

if contador == 2: # 1 arroba + 1 punto
    print('email OK!')
else:
    print('email falso!')

#bucle for con range:
for i in range(5):
    print(i)
























































        
















































        
    










