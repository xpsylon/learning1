#ATRIBUTOS: Nombre, Edad, Alimentos Favoritos
#METODOS: _init_(), verEtapaDeVida(), esAlimentoFavorito()
#CONSTANTE: ESPECIE
class Gato:
    ESPECIE = 'mamifero'

    def __init__(self, nombre, edad):                           #nombre y edad se inicializan como parametros
        self.nombre1 = nombre                                   #variable = parametro
        self.edad1 = edad
        self.alimentos = []                                     #variable que va a ser lista, return valor alimento
                                                                #se inicializa como lista vacia

    def verEtapadeVida(self):
        if self.edad1 > 1:
            print(self.nombre1, "es adulto")
        else:
            print(self.nombre1, 'es cachorro')

    def esAlimentoFavorito(self, alimento):                     #en este metodo (funcion) creamos parametro alimento para que itere en self.alimentos.
        return alimento in self.alimentos                       #To exit a function and return a value True or False

el_gato1 = Gato('TopCat', 1)
print(el_gato1.nombre1)
print(el_gato1.edad1)

el_gato1.raza = 'Siames'                                        #podemos agregar un atributo de forma dinamica a nivel instancia.
print(el_gato1.raza)

el_gato2 = Gato('Jinx', 2)                                      #2da instancia objeto clase Gato
print(el_gato2.nombre1)
print(el_gato2.edad1)

#APPEND (list method) to alimentos
el_gato1.alimentos.append('leche')                              #agregamos alimentos a la lista vacia alimentos con metodo append
el_gato1.alimentos.append('pescado')
print(el_gato1.alimentos)

#different way we create list for el_gato2.alimentos
el_gato2.alimentos = ['carne', 'whisky']                        #aqui directamente llenamos la lista
print(el_gato2.alimentos)

el_gato3 = Gato('Santini', 1)                                   #3ra instancia clase Gato
el_gato3.verEtapadeVida()                                       #llamamos metodo verEtapaDeVida (print incluido en la def)

el_gato2.esAlimentoFavorito('whisky')                           #no tiene print la funcion. devuelve True or False
print(el_gato3.esAlimentoFavorito('whisky'))                    #imprimimos

print(el_gato3.alimentos)                                       #no se creo lista alimentos para el_gato3, asi que output vacio
el_gato3.alimentos = ['pollo', 'ensalada']                      #llenamos lista alimentos de el_gato3
print(el_gato3.alimentos)                                       #y la imprimimos

print(el_gato3.ESPECIE)                                         #imprimo la ESPECIE (constante de clase)
print(el_gato1.ESPECIE)

print(Gato.ESPECIE)                                             #tambien me da el valor de la constante (o atributo de clase) sin necesidad de crear instancia
