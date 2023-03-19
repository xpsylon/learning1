#creamos dos funciones muy simples:
def suma(a, b):
    c = a + b
    print(c)

def resta(e, f):
    g = e - f
    print(g)


#VERSION SUPER SIMPLE SIN PARAMETROS
#creamos funcion decoradora con su funcion parametro:
def funcion_decoradora(funcion_parametro):
    def funcion_interior(): # funcion interior
        #codigo interno funcion_interior:
        print('Vamos a realizar un calculo') #mensaje 1
        funcion_parametro() #llamamos a la funcion parametro (suma o resta)
        print('Hemos terminado el calculo') #mensaje 2
    return funcion_interior #return de la funcion DECORADORA (check indentation)

#creamos variantes de las funciones suma y resta para usar con la funcion_decoradora y comparar las diferencias:
@funcion_decoradora
def suma1():
    c = 14 + 88
    print(c)

suma1()

@funcion_decoradora
def resta1():
    g = 1005 - 888
    print(g)

resta1()

    




