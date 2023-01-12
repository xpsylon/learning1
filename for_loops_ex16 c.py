#ejercicio mensajes 7.2 Bucles anidados Programacion desde Cero
#mismo que en for_loops_ex16, pero para 5 mensajes:

#esta primera parte permanece igual, no itera:
abc = 'abcdefghijklmnopqrstuvwxyz'
#en el ejercicio original la q de espacios es = para todos los msgs...
pos_letter = int(input('Cantidad de espacios a desplazar: '))
#en el ejercicio anterior lo hicimos con while y counter.
#la solucion original es con for in range...

for i in range(5): #itera 5 veces del 0 al 4
    print('Mensaje', i + 1)
    mensaje = input('Introduce tu mensaje: ')
    msg_cript = '' #arranca vacio para ser llenado con la iteracion

    #Iteracion por alfabeto:
    for j in mensaje:
        if j in abc:
            posicion_alfabeto = abc.find(j)#encontramos la posicion de cada letra en el abc
            #ahora la desplazamos y encontramos nueva posicion numerica con formula dada
            #por si pasamos la z...
            pos_cript = (posicion_alfabeto + pos_letter) % 26
            #letra correspondiente a nueva posicion numerica:
            #la guardamos en el msg_cript
            msg_cript += abc[pos_cript]
        else:
            #caso de otros caracteres se agregan invariables a msg_cript
            msg_cript += j
    print(msg_cript)
        
        
        

            
