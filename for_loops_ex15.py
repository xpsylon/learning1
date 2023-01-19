abc = 'abcdefghijklmnopqrstuvxyz'
msg = input('Mensaje: ')
cript = int(input('Numero encriptado: '))
msg_cript = ''
     
for i in msg:
    if i in abc:
        indice_msg = abc.find(i)
        clave_msg = indice_msg + cript
        msg_cript += abc[clave_msg]
print(msg_cript)
            
        
