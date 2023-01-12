#difference between iterable and iterator:
#iterable is an object, that one can iterate over. When passed to iter() method.
#iter() returns an iterator object. Object has to be iterable (lists, tuples, dicts)
#next() returns the next item in an iterable.

#next('bananas') will output error. first we have to convert the string to an iterator using iter(), saving it in
#a variable
gorila = 'bananas' #guardo string en variable
gorila1 = iter(gorila) # returns an iterator object (variable gorila1)
print(next(gorila1)) # iterating through string
print(next(gorila1))
print(next(gorila1))
print(next(gorila1))
print(next(gorila1))
print(next(gorila1))
print(next(gorila1))

#function for checking if object is iterable or not:
def checar(objeto):
    try:
        iter(objeto) #instruccion: tratar de convertir objeto a iterador
        return True # todo ok
    except TypeError: # si no se puede convertir a iterador, aviso de TypeError
        return False

#iterating through list with 'for-loop':
for item in [48, [25, 'stevie'], (25, 'stevie'), True, {'b': 105}, 'kaugummi', 12.8]:
    print(item, 'es iterable: ', checar(item))

mi_iterable = range(1, 5)
mi_iterador = mi_iterable.__iter__()#same as iter(mi_iterable)
print(mi_iterador.__next__()) #same as next(mi_iterador)

#iterators in for-loops:
#loops r e q u i r e an iterable
palabra = 'perraco'
for letra in palabra:
      print(letra)

listonga = ['anana', 'gloria', 25]
for items in listonga:
    print(items)

#iterators in comprehensions:
camilo_sesto = [pom for pom in 'Rosa de los Vientos']

barro = [tip for tip in ['carro', 'anana', 'serpiente'] if 'n' in tip]

#iterate dictionary keys:
diccio = {'nombre': 'javier', 'edad': 59, 'pais': 'AR'}
diccio1 = iter(diccio) #asi itera un key por vez, para iteracion total hay que hacer una for-loop.
for llave in diccio:
    print(llave)   #iteracion de keys

#iterate dictionary values:
for valor in diccio.values(): #lo mismo que iteracion normal de dict, pero usando dict method .values()
    print(valor)

#iterate dictionary keys AND values:
#use items()
#with for-loop
for llave, valor in diccio.items():
    print(llave,':', valor)

#with comprehension:
print({llave: valor for llave, valor in diccio.items()})

#converting iterator to list, set or tuple:
list(range(1, 11))

#building an own iterator:
class NumeroPar: #creamos clase
    ultimo = 0 #variable valor salida 0

    def __iter__(self): #creamos iterador para esta clase(todas sus instancias tendran iterador)
        return self
    def __next__(self): #funcion para que itere al proximo item
        self.ultimo += 2 #  tomando valor salida variable 0, incrementar de a 2
        if self.ultimo > 8: # si pasa de 8
            raise StopIteration # paramos iteracion
        return self.ultimo # devuelve el ultimo numero

numero_par = NumeroPar() # creamos instancia

for num in numero_par: # for-loop para iterar por la instancia
    print(num)


















































    









































      
