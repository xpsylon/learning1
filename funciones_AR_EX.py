#Ejercicio de funcion erroneo usando variables globales dentro de la funcion:
#Determinar cual es la salida en pantalla si se ingresan x=6, y=7?
def coordenadaZ(x, y):
    x += 10
    y += 15
    return x + y
#programa principal:
x = int(input('Coordenada eje x: '))
y = int(input('Coordenada eje y: '))

for i in range(3):
    z = coordenadaZ(x, y) #guarda el retorno de la funcion en una variable sin
    #usarlo luego.
    x += 1
    y += 1
print(x,' . ', y)
#Ahora lo mejoramos introduciendo variables locales:
def coordenadaC(a, b):
    a += 10
    b += 15
    return a + b

x = int(input('Coordenada eje x: '))
y = int(input('Coordenada eje y: '))

for i in range(3):
    c = coordenadaC(x, y)
    x += 1
    y += 1
print(x,' , ', y)

    
