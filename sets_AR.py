conjunto = {1, 2, 3} #no random
conjunto_vacio = {} #crea un diccionario en vez de un set
conjunto_vacio1 = set() #set vacio
#conjunto_elementos = set('amorabieta', True, 108, 12.45) esto da error.
# el set() solo admite 1 argumento, q puede ser una lista o tupla.
conjunto_elementos = {'amorabieta', True, 108, 12.45} #random
conjunto_string = set('caribeano') #itera letra por letra de randomly
conjunto_range = set(range(6)) #no random
conjunto_lista = set([10, 20, 'perin', 45, 20]) #elimina el 2do 20. los numeros
#van sorted, el string random.
conjunto_lista1 = set([1, 2, 3, 4, 5]) #not random
conjunto_float = {1.3, 3.9, 2.6, 10.22} #not random
conjunto_float_int = {1, 3, 7, 2, 0.5, 27.2, 8.1}
set5 = {True, 12, 108, 45.2, 'banana'}
set5.add(False)
list(set5) #solo convierte en el primer output
iterar5 = {'los fatales'} #no itera, set no es iterable
iterar6 = {x for x in 'los fatales'} #iteracion comprehension por cadena
lista1 = ['viento', 12, True, 0.8, 'conejo']
itera7 = {x for x in (lista1)}
lista2 = ['ama', 'pepa', 'jose']
itera8 = {x for x in (lista2) if 'a' not in x}
itera9 = {x for x in 'los fatales' if x not in 'a'}
itera10 = {x for x in 'los fatales' if 'a' not in x}
setIterarString = {x for x in 'Hola, que tal?' if x not in ', ?'}
setIterarString1 = {x for x in 'Hola, que tal?' if ', ?' not in x}
itera11= {x for x in 'los fatales?' if x not in ' ?'}
itera12 = {x for x in 'los fatales?' if ' ?' not in x}
itera13= [x for x in 'los fatales?' if x not in ' ?']
itera14 = [x for x in 'los fatales?' if ' ?' not in x]

