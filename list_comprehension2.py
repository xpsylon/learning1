#LIST COMPREHENSION
#it is a language construct. It is used to create a new list based on an existing list.

#[<expression 'for' item 'in' list 'if' <conditional>]

#for creating the new list, we need any iterable. Now we will use range(). Range is a special kind of iterator called
#generator
print([x for x in range(1, 10)])

#this would be the same as:
print(list(range(1, 10)))

#now we will use the conditional 'if':
print([x for x in range (1, 10) if x % 2 == 0])
#means [expression(x) 'for' item (x) 'in' iterable(range) 'if' conditional(x par)]

#expression can be anything that is a valid python code:

print([x + 4 for x in [10, 20]]) #itera en la lista sumando 4 a los dos items

def funzione(param):
    return (param + 5) / 2
#funcion que devuelve el argumento + 5 dividido 2
m = [funzione(arg) for arg in range(11, 25, 2)]
#funzione(arg) es la expresion. arg es el argumento del parametro param.
#luego se itera del 0 al 8 sumando 5 (excl) y dividiendo por 2 en cada iteracion.

def pitorro(a, b, c):
    return a, b, c

listola = ['huevo', 15, False]

#nested list comprehensions:
#the expression can be another list comprehension as well:
sarasa = [[t for t in range(3)] for s in range(5)]










