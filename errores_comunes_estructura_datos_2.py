#funcion que carga datos en un diccionario, la clave es el dni.
def cargarDatos(diccionario):
    dni = int(input('DNI: '))
    while dni != 0:
        nombre = input('Nombre: ')
        domicilio = input('Domicilio: ')
        telefono = int(input('Telefono: '))
        diccionario[dni] = [nombre, domicilio, telefono] #crea dicc a partir de
        #las variables, usando dni como clave, valor es resto de datos como lista.
        dni = int(input('Otro DNI: '))
    return diccionario

#esta siguiente funcion va a dar error, ya que usa variables locales de la
#funcion cargarDatos
def imprimirDatos(diccionario): #el diccionario si que se le pasa xq ya va a
    #estar creado por la funcion anterior
    for clave, valor in diccionario.items():
        #print(dni, nombre, domicilio, telefono)
        #lo arreglamos asi:
        print(clave, valor)

clientes = {44299132:['Gaston Quinteros', 'Los Tilos 412', 58211972],
            38110223:['Valeria Gimenez', 'Almendros 192', 59912834],
            27918006:['Diego Linares', 'Las Fresias 881', 51288390]}
clientes = cargarDatos(clientes) #llama a funcion pisando anterior valor de
#clientes
imprimirDatos(clientes)
    
