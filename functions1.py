# Python function is a named section of a program that performs a specific task and, optionally, returns a value
# There are a lot of built in functions in Python: PRINT, LEN, EVAL
# To create an own function we use DEF

def say_hi():  # keyword DEF defines a function. say_hi is function name. The two () means function doesnt accept any paramether. End with colon :
    print('Hi')  # Python uses indentation to distinguish blocks of code that belong together


say_hi()  # calling the function


# ----------------------------------------------------------
# Now we will allow to pass a parameter to the function
# A Python function can have parameters. The values we pass through these parameters are called arguments.
def say_hi(name):
    print('Hi', name)


say_hi('Javier')


# --------WITH MULTIPLE ARGUMENTS------------
def welcome(name, location):
    print('Hi', name, 'welcome to', location)


welcome('Javier', 'Mijas')


# ---------WITH RETURN VALUE-----------------
def sumar(a, b):  # defining the function with two parameters
    return a + b  # keyword RESULT for returning a value


resultado = sumar(8, 14)  # defining variable and calling function with given arguments
print(resultado)

# ------------CON INPUT VARIABLES-------------
a = int(input('Pone la a '))
b = int(input('Pone la b '))

resultado2 = sumar(a, b)
print(resultado2)


# -----------EMPTY RETURN STATEMENT-----------
def saludo_opt(name):  # definimos function con parametro name
    if name.startswith('x'):  # si empieza con x. STARTSWITH es un string method como UPPER or LOWER
        return  # no retorna nada. keyword RETURN vacio

    print('hola', name)  # otherwise....


saludo_opt('jose')  # function call with given argument


# -----------EMPTY RETURN ANOTHER OPTION-------
def saludo_opt2(name2):
    if name2.startswith('x'):
        pass
    else:
        print('te llamas ', name2)      #parametro o variable interna en la funcion


saludo_opt2(input('pone tu nombre '))           # con input
#--------------ERROR POR VARIABLE INTERNA-------
def hola(rta=None):
    print('Que tal', name)
    rta = 'si soy yo'

name = 'Javier'

hola()
#-------------AHORA VARIABLE EXTERNA------------
rta = 'Si soy yo'
print(rta)


