#we create a function for division, where the numerator has to be always bigger than the divisor,
#regardless in which order you put the arguments in the function.
def div(a, b): #creating division function
    if a < b: # if numerator smaller than divisor
        a, b = b, a # then swap the order
    c = a / b
    print(c)

#div(3, 5)

#if we are calling a function from a module, and we want to add this conditional (if), we have to use DECORATORS,
#which basically is a function inside a function (just possible in python)

#esta seria la funcion guardada en el modulo:
def dividir(a, b):
    c = a / b
    print(c)


def smart_div(pipola): #creamos nueva funcion con funcion interna
    def interna(a, b): #funcion interna con mismos parametros a funcion guardada en modulo.
        if a < b:
            a, b = b, a
        return pipola(a, b)
    return interna

dividir1 = smart_div(dividir)
dividir1(2, 4)

#STRUCTURE OF DECORATORS:
#def funcion_decoreador(funcion):
    #def funcion_interna():
        #codigo funcion interna
    #return funcion interna (devuelve la funcion interna A LA FUNCION DECORADORA.Se podria agregar un return a la
    #funcion interna tambien




























































