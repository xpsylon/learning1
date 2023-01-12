#ejercicio mensajes 7.2 Bucles anidados Programacion desde Cero
abc = 'abcdefghijklmnopqrstuvwxyz'
mensaje = input('Introduce tu mensaje: ')
pos_letter = int(input('Cantidad de espacios a desplazar: '))#en el mensaje
msg_cript = '' #arranca vacio para ser llenado con la iteracion

#Iteracion por alfabeto:
for i in mensaje:
    if i in abc:
        posicion_alfabeto = abc.find(i)#encontramos la posicion de cada letra en el abc
        #ahora la desplazamos y encontramos nueva posicion numerica con formula dada
        #por si pasamos la z...
        pos_cript = (posicion_alfabeto + pos_letter) % 27
        #letra correspondiente a nueva posicion numerica:
        #la guardamos en el msg_cript
        msg_cript += abc[pos_cript]
    else:
        #caso de otros caracteres se agregan invariables a msg_cript
        msg_cript += i
print(msg_cript)
        
        
        

            
