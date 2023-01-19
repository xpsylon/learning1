#DECORADORES CON INPUT DE NUMEROS
#pildoras informaticas #74

def funcion_decoradora(funcion_parametro): #funcion decoradora con el parametro de la funcion a decorar
    def funcion_interior(): #funcion interior
        print('Vamos a realizar un calculo') #mensaje 1
        funcion_parametro() #llamado a la funcion que se quiere decorar
        print('Calculo terminado!') #mensaje 2
    return funcion_interior #de funcion_decoradora

@funcion_decoradora
def suma():
    num1 = int(input('primer numero '))
    num2 = int(input('otro numero '))
    a = num1 + num2
    print(a)

suma()

@funcion_decoradora
def resta():
    num1 = int(input('primer numero '))
    num2 = int(input('segundo numero '))
    a = num1 - num2
    print(a)

resta()
    
        
