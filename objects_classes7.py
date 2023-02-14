class Carrera:
    def __init__(self, nombre):
        self.nombreCar = nombre
        #self.materiasCar = []                              #cambiamos de lista a diccionario
        self.materiasCar = {}

#creamos metodo propio para poder agregar materias al diccionario de manera facil
    def agregarMateria(self, materia, codigo):
        self.materiasCar[codigo] = materia                  #la variable self.MateriasCar tiene que tener el mismo nombre que el diccionario

class Materia:
    def __init__(self, nombre, profesor):
        self.nombreMat = nombre
        self.profesorMat = profesor


#CREO INSTANCIAS:
ing = Carrera('Ingenieria') #de clase Carrera...

#de clase Materia
algebra = Materia('Algebra', 'Ricardo Quinteros')
fisica = Materia('Fisica', 'Javier La Porte')
quimica = Materia('Quimica', 'Lorena Rios')

tarot = Materia('Tarot', 'Tu Sam')  #TEST

print(ing)

#agrego materias con un Id a la lista en forma de tuplas
#ing.materiasCar.append((134, algebra))         #append() no es metodo de diccionario
#ing.materiasCar.append((408, fisica))
print(ing.materiasCar)
print(len(ing.materiasCar))

#usamos metodo agregarMateria a la lista: agregarMateria(self, materia, codigo) . Preponer la instancia (ing)
ing.agregarMateria('fisica', 311)                       #para que se lea key and value, value = string
ing.agregarMateria(algebra, 101)
ing.agregarMateria(quimica, 102)

ing.materiasCar[615] = 'tarot'    #TEST agregado al diccionario directamente sin usar el metodo agregarMateria

#ahora volvemos a imprimir luego del agregado de materias
print(ing.materiasCar)
