#creamos clase:
class UserNotFoundError(Exception):
    pass


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
usuario = 123
try:
    buscar_usuario(id_usuario)
except UserNotFoundError as horror:
    print('oh God!', horror)
