#funcion generador construye un objeto iterable a traves de yield. Luego extrae el primer valor y queda en suspension
#(suspension de estado) hasta que se llama al siguiente valor a traves de __next__
#SINTAXIS GENERADOR
#def generaNumeros():
#   yield numeros

#funcion numeros pares:
def generaPares(limite):
    numero = 1
    lista_pares = []
    while numero < limite:
        lista_pares.append(numero * 2)
        numero += 1
    return lista_pares

#generador numeros pares:
def generaPares2(limite):
    numero1 = 1
    #aqui no va lista, ya que debe generar los numeros 1 a 1:
    while numero1 < limite:
        yield numero1 * 2
        numero1 += 1
#creamos variable para poder iterar (las funciones no son iterables):
devuelvePares = generaPares2(10)

#creamos for loop para iterar:
for i in devuelvePares:
    print(i)

#GENERATORS NAVIN REDDY #62


def topten():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5 #instead of return for generator functions
    

values = topten() #asignar la funcion a variable para poder iterar
#metodo __next__ () a la variable:
print(values.__next__()) # each next will return  ONE yield each time

#with a for-loop:
for i in values:
    print(i)

def cuadrado():
    num = 1
    while num <= 10:
        sq = num * num
        num += 1
        yield sq #devolver el cuadrado
    

valores = cuadrado()
#AS A LOOP:
#for i in valores:
    #print(i)
#ONE BY ONE:
#print(valores.__next__())

#se usan los generadores cuando tenemos que pedir una gran cantidad de datos, p.ej de una database. no queremos
#pedirlos todos a la vez para no cargar la memoria. los pedimos uno a uno a traves de un generador.




    
    

    
