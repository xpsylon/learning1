#print string con variable numerica
for i in range(4):
    print('variable', i) #opcion con ','. funciona bien

for i in range(4):
    print('variable {i}') #funciona mal
    
for i in range(4):
    print(f'variable {i}') #funciona bien

#for i in range(4):
#    print('variable' + i) #funciona mal.

for i in range(4):
    print('variable ' + str(i)) #funciona bien

#otra manera de chequeo basico de mail:

valido = False

email = input('Introduce tu email: ')

for i in range(len(email)): #con len convierte el email a valores numericos, a lo que se le aplica un range()
    #if i == '@': #error porque i ahora son valores numericos
    if email[i] == '@': # si alguno de los index es igual a arroba
        valido = True

if valido:
    print('mail valido')
else:
    print('mail incorrecto')




    
