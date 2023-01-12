def f(a, b, *data): #not forcing because * is in just for the last argument
    print(a, b, data) #will print data as a tuple
f(1,2,3,'conejo')

def pepe(*, a, b): #forcing a, b to be keyword arguments
    print(a, b)

#pepe(1, 2)# will output error 'takes 0 positional arguments, but 2 were given.
pepe(a='lolo', b=2)

#USING * (lists) and ** (dictionaries) for FUNCTION ARGUMENTS
def diccio (a, b,): #el # de parametros tiene que coincidir con el # de keywords del dict. (2)
    print(a, b)

args = {'a': 25, 'b': 'tocateja'} #creamos diccionario. keywords (2)
diccio(**args) #lo introducimos como argumento de la funcion.

def lista(a, b, c): 
    print(a, b, c)

args1 = ['papa', 105, True] #creamos lista
lista(*args1) #la introducimos como argumento en la funcion






    
