#El siguiente programa deberia imprimir el numero 2 si se le ingresan como
#valores x=5, y=1 pero en su lugar imprime 5. Que hay que corregir?

def maximo(a,b):
    if x > y:
        return x
    else:
        return y
def minimo(a,b):
    if x < y:
        return x
    else:
        return y

#programa principal:
x = int(input('Un numero: '))
y = int(input('Otro numero: '))

print(maximo(x-3, minimo(x+2, y-5)))#minimo es uno de los argumentos de maximo
#resolver de adentro hacia afuera
#x=5
#y=1

#minimo(5+2, 1-5)
#minimo(7, -4)
#return -4

#maximo(5-3, -4)
#maximo(2, -4)
#El problema es que las funciones retornan el valor de entrada de las
#variables locales. Corregimos:
def maximo(a,b):
    if a > b:
        return a
    else:
        return b
def minimo(a,b):
    if a < b:
        return a
    else:
        return b

#programa principal:
x = int(input('Un numero: '))
y = int(input('Otro numero: '))

print(maximo(x-3, minimo(x+2, y-5)))
