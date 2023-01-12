#FUNCION DECORADORA CON PARAMETROS *ARGS y *KWARGS
#pildoras informaticas #74

def funcion_decoradora(funcion_parametro):
    def funcion_interior(**kwargs): #KEYWORD ARGUMENTS
        print('Calculamos...')
        funcion_parametro(**kwargs) #KEYWORD ARGUMENTS
        print('Listo!')
    return funcion_interior

#si usamos funcion decoradora, esta debe estar definida ANTES de la funcion a decorar.
@funcion_decoradora
def suma(a, b, c): 
    c = a + b + c
    print(c)

suma(a=10, b=16, c=48)

@funcion_decoradora
def resta(subst1, subst2):
    c = subst1 - subst2
    print(c)

resta(subst1= 10, subst2 = 2)


    
def funcion_decoradora1(funcion_parametro):
    def funcion_interior(*args): #POSITIONAL ARGUMENTS
        print('Calculamos...')
        funcion_parametro(*args) #POSITIONAL ARGUMENTS
        print('Listo!')
    return funcion_interior

#si usamos funcion decoradora, esta debe estar definida ANTES de la funcion a decorar.
@funcion_decoradora1
def suma(a, b, c): 
    c = a + b + c
    print(c)

suma(10, 16, 48)

@funcion_decoradora1
def resta(d, e):
    f = d - e
    print(f)

resta(87, 9)

@funcion_decoradora1
def potencia(base, exp):
    print(pow(base, exp))

potencia(2,8)

#Arguments lesson Pyhton Land
def f (*,a, b):
    print(a, b)
f(a=10, b=20)

















































    
