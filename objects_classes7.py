class Carrera:
    def __init__(self, nombre):
        self.nombreCar = nombre
        self.materiasCar = []
        #en vez de lista vamos a usar mejor un diccionario que sea cargado
        #con el metodo agregarMateria(self, materia, codigo)
        self.materiasCar2 = {}

#creamos metodo propio para poder agregar materias al diccionario de manera facil.
#la variable self.MateriasCar tiene que tener el mismo nombre que el diccionario.
        
    def agregarMateria(self, materia, codigo):
        self.materiasCar2[codigo] = materia                  

class Materia:
    def __init__(self, nombre, profesor):
        self.nombreMat = nombre
        self.profesorMat = profesor

<<<<<<< HEAD
#instancias con sus argumentos.
ing = Carrera('Ingenieria')
=======

#CREO INSTANCIAS:
ing = Carrera('Ingenieria') #de clase Carrera...

#de clase Materia
>>>>>>> 1b75bde9817659bdeb1615128211115ab902c623
algebra = Materia('Algebra', 'Ricardo Quinteros')
fisica = Materia('Fisica', 'Javier La Porte')
quimica = Materia('Quimica', 'Lorena Rios')

tarot = Materia('Tarot', 'Tu Sam')  #TEST

print(ing)

<<<<<<< HEAD
#agrego materias con un Id a la lista en forma de tuplas (id, instancia)
#append() no es metodo de diccionario
ing.materiasCar.append((134, algebra))                           
ing.materiasCar.append((408, fisica))
ing.materiasCar.append((290, quimica))
=======
#agrego materias con un Id a la lista en forma de tuplas
#ing.materiasCar.append((134, algebra))         #append() no es metodo de diccionario
#ing.materiasCar.append((408, fisica))
>>>>>>> 1b75bde9817659bdeb1615128211115ab902c623
print(ing.materiasCar)
print(len(ing.materiasCar))

#usamos metodo agregarMateria a la lista: agregarMateria(self, materia, codigo) . Preponer la instancia (ing)
ing.agregarMateria('fisica', 311)#para que se lea key and value, value = string
ing.agregarMateria(algebra, 101)
ing.agregarMateria(quimica, 102)

#TEST agregado al diccionario directamente sin usar el metodo agregarMateria
ing.materiasCar2[615] = 'tarot'

#ahora volvemos a imprimir luego del agregado de materias
print(ing.materiasCar2)
