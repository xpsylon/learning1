#Cargar todos los datos en la misma lista cuando deberian ser diferentes:
def cargarMercaderias(mercaderias):
    articulo = [] #arrancamos con una lista vacia para luego ser usada como valor
    #del diccionario.
    codigo = int(input('Codigo: ')) #sera la clave del diccionario
    while codigo != 0:
        descripcion = input('Descripcion: ')
        articulo.append(descripcion) #lo agregamos a la lista articulo
        rubro = input('Rubro: ')
        articulo.append(rubro) #idem
        #creamos diccionario usando codigo como clave y la lista articulo como valor.
        mercaderias[codigo] = articulo
        codigo = int(input('Otro codigo: ')) #recarga codigo y sigue loop
    return mercaderias #diccionario

#MANERA CORRECTA
def cargarMercaderias(mercaderias):
    #articulo = [] #arrancamos con una lista vacia para luego ser usada como valor
    #del diccionario.
    codigo = int(input('Codigo: ')) #sera la clave del diccionario
    while codigo != 0:
        descripcion = input('Descripcion: ')
        #articulo.append(descripcion) #lo agregamos a la lista articulo
        rubro = input('Rubro: ')
        #articulo.append(rubro) #idem
        #creamos diccionario usando codigo como clave y la lista articulo como valor.
        mercaderias[codigo] = [descripcion, rubro]
        codigo = int(input('Otro codigo: ')) #recarga codigo y sigue loop
    return mercaderias #diccionario

productos = {} #dicc vacio
productos = cargarMercaderias(productos) #llama a la funcion y carga los datos
#impresion:
for clave, valor in productos.items():
    print(clave, '-Descripcion:', valor[0], '-Rubros:', valor[1])
#al agregarse valores en cada iteracion SIEMPRE va a imprimir los primeros dos
#[0] y [1]
    
