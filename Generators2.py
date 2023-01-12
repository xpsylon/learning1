#YIELD FROM:
#simplificar el codigo de los generadores cuando usamos bucles anidados.



#con * delante del parametro significa que recibe nro indeterminado de argumentos
#en forma de tupla.
def devuelve_ciudades(*ciudades):
    for i in ciudades: #loop
        yield i #devolucion generador (uno a uno)

mis_ciudades = devuelve_ciudades('Berlin', 'Madrid', 'Buenos Aires', 'Kiev') #funcion asignada a variable para
#poder iterar.

print(next(mis_ciudades)) #BUILT IN FUNCTION NEXT. Mismo que mis_ciudades.__next__()

#ahora necesitamos crear un for-loop anidado para recibir solo parte de cada string.

def devuelve_ciudades1(*ciudades1):
    for i in ciudades1:#loop
        for sub_i in i: #sub loop
            yield sub_i #devolucion generador (uno a uno)

mis_ciudades1 = devuelve_ciudades1('Berlin', 'Madrid', 'Buenos Aires', 'Kiev')
print(next(mis_ciudades1))

#ahora lo mismo que en el for-loop anidado, pero usando YIELD FROM:
def devuelve_ciudades2(*ciudades2):
    for i in ciudades2: #loop
        yield from i#devolucion generador (uno a uno)

mis_ciudades2 = devuelve_ciudades2('Berlin', 'Madrid', 'Buenos Aires', 'Kiev')


#EJERCICIO CON INPUT:

c1 = input('Ciudad1: ')
c2 = input('Ciudad2: ')

def devuelve_ciudades3(c1, c2):
    for i in c1, c2: #loop
        #print(i) #devolucion generador (uno a un

print(devuelve_ciudades3(c1, c2))










