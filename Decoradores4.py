#DECORADORES CON PARAMETROS
#pildoras informaticas #74

#funcion con dos parametros:
def funcion_decoradora(funcion_parametro): #funcion decoradora con el parametro de la funcion a decorar
    def funcion_interior(num1, num2): #funcion interior con dos parametros
        print('Vamos a realizar un calculo') #mensaje 1
        funcion_parametro(num1, num2) #llamado a la funcion que se quiere decorar, tambien necesita dos parametros
        print('Calculo terminado!') #mensaje 2
    return funcion_interior #de funcion_decoradora

@funcion_decoradora
def suma(num1, num2): #esta es la funcion que PIDE o NO parametros al ser llamada
    a = num1 + num2
    print(a)

suma(58, 27)

@funcion_decoradora
def resta(num1, num2): #esta es la funcion que PIDE o NO parametros al ser llamada
    a = num1 - num2
    print(a)

resta(100, 48)

@funcion_decoradora
def potencia(base, exp): #esta es la funcion que PIDE o NO parametros al ser llamada
    a = base ** exp
    print(a)

potencia(8, 4)
    
        
