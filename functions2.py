#A compelling Python feature is the ability to provide default values for the parameters
def welcome(nombre='tonto', lugar='Mijas'):
    print('Hola', nombre, 'bienvenido a', lugar)

welcome()
welcome(nombre='javier')
welcome(lugar='Anfibia del Sur')
welcome(nombre='Javier', lugar='Anfibia del Sur')
welcome('Angueto', 'Kurulia')                               #this one will override parameters and values

