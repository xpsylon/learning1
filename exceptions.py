#PYTHON EXCEPTIONS (TRY EXCEPT)
#Exception handling is the process of identifying and responding to errors in a program.
#We learn how to deal with errors using the KEYWORDS 'try' and 'except'.

#CATCHING EXCEPTIONS WITH TRY EXCEPT
#When an exception occurs when we are inside the 'try' block, the code in the 'except' block will be executed.

#EXAMPLE
#we cant divide by zero:
try:
    2 / 0
except ZeroDivisionError:
    print('No se divide por 0, tonto!')
#same code without 'try' and 'exception'
#print(2/0)

#OPEN FILES
#we use the PYTHON FUNCTION open().
#open() takes two parameters, filename and mode (r-read, a-append, w-write, x-create)
#files have their read() method
kiko = open('testa.txt')
print(kiko.read())

#adding the 'with' and 'as' KEYWORDS for keeping the code inside just a block in case of exceptions (errors)
with open('testa.txt') as kiko:
    pepo = kiko.read()

print(pepo)
#In this example, the with-statement makes sure the file is closed, even if an exception occurs.
#That’s because Python closes the resource automatically as soon as we step out of the scope of this with-statement.
#Due to this automatic close, you can not use the file (called 'kiko' in our case) outside of the with-statement.
#If you want to use it again, you have to open it again.

with open('testa2.txt') as f:
    f.read()

print(f) #here is wrong because we are using the file outside the 'with' statement. so we need to create the
#variable as we did in the case before.

with open('testa2.txt') as f:
    archivo = f.read()

print(archivo)

#so now we catch the IO Error while opening a file:
try:
    with open('casio.txt') as lola:
        archivo1 = lola.read()
except IOError as tam:
    print('Habemus errorus!', tam)#el parametro 'tam' de la variable imprime el IOError en la respuesta.
    #si quitamos 'tam' solo imprime 'Habemus errorus'

#now we will write an existing file:
try:
    with open('testa2.txt', 'w') as javier: #write 'w' argument.
        javier.write('el amor no lo reflejo')
except IOError as pep:
    print('no existe', pep) #output no writable

#Adding the 'finally' and 'else' blocks:
#'finally' block will be executed regardless an exception occurs or not.

try:
    jack = open('testa2.txt', 'a')
    jack.write('\nporque el tiempo pasa')

except IOError as ana:
    print('Hay un puto error', ana)

finally:
    print('Cerrando archivos...')
    jack.close()

#the 'else' block executes only when no exception occurs. why not to add this directly to the 'try' block?.
#good question....


#dont use blank 'except' codes:
#try:
    #...
#except:
    #print('bananas')

#USE:
#try:
    #...
#except print('bananas')

#In python you always ask for forgiveness ('except') instead of permision ('if' ...'then'):

import json

usuario_jassone = '{"name": "PutoJoey", "age": "85"}'
este_pibe =  json.loads(usuario_jassone)

try:
    print(este_pibe['name'])
    print(este_pibe['age' ])
    print(este_pibe['address'])

except KeyError as simp:
    print("Falta esta clave:", simp)

#CREATING USER CUSTOM EXCEPTIONS:
#All built-in exceptions are derived from the Exception class. So if you want to create an own exception, it has
#to be subclass from this class:

#creamos clase:
class UserNotFoundError(Exception):
    pass

#USUARIO NONE
#creamos funcion con parametro id_usuario.
def buscar_usuario(id_usuario):
    #deberia buscar de alguna base de datos.
    #para que funcione esto sin base de datos, we set it to None.
    usuario = None #variable con valor None
    if usuario == None:
        raise UserNotFoundError(f'Numero de usuario {id_usuario} no encontrado')#con raise forzamos la excepcion
    else:
        print(usuario)

#creamos lista:
usuarios = [123, 452, 528]
for id_usuario in usuarios:
    try:
        buscar_usuario(id_usuario)        
    except UserNotFoundError as horror:
        print('oh God!', horror)

#USUARIO = ID_USUARIO

#creamos funcion con parametro id_usuario.
def buscar_usuario(id_usuario):
    #deberia buscar de alguna base de datos.
    #para que funcione esto sin base de datos, we set it to None.
    usuario = id_usuario #variable con valor None
    if usuario == None:
        raise UserNotFoundError(f'Numero de usuario {id_usuario} no encontrado')#con raise forzamos la excepcion
    else:
        print(usuario)

#creamos lista:
usuarios = [123, 452, 528]
for id_usuario in usuarios:
    try:
        buscar_usuario(id_usuario)        
    except UserNotFoundError as horror:
        print('oh God!', horror)






    


    






















































    
