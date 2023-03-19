
class Carrera:
    def __init__(self, nombre):
        self.nombreCar = nombre
        self.__materiaCar = {} #diccionario oculto con doble underscore. Renombra el atributo

# creamos metodo propio para poder agregar materias al diccionario de manera facil
    def agregarMateria(self, materia, codigo):
        #debe ir oculta tambien con doble underscore. Renombrado interna y secretamente por python.
        #Solo se podria acceder a el a traves de un metodo que tenga getters y setters.
        self.__materiaCar[codigo] = materia  # la variable self.MateriasCar tiene que tener el mismo nombre que el diccionario


class Materia:
    def __init__(self, nombre, profesor, fecha):
        self.nombreMat = nombre
        self.profesorMat = profesor
        #no puede ser anterior a 2006
        self.fechaInicioDictado = fecha                         #atributo que sera enmascarado dentro de @property. 1

    @property #decorador                                        #funcion built in para ocultar la parte set. reemplaza metodo getters. DECORATOR
    def fechaInicioDictado(self):                               #metodo mismo nombre que atributo fecha inicio en clase Materia. Para validar la fecha antes de pasarla
        #print('prueba')                                         #imprime solo un output para demostrar que funciona. el resto esta oculto
        return self._fechaInicioDictado                         #guion bajo convierte el atributo en privado (invisible)

    @fechaInicioDictado.setter #decorador setter
    def fechaInicioDictado(self, fecha): #metodo mismo nombre pero bajo decorador setter.
        if fecha < 2006:
            self._fechaInicioDictado = 2006
        else:
            self._fechaInicioDictado = fecha


ing = Carrera('Ingenieria')
#hay que agregar argumento fecha al parametro que se agrego en el _init_ de Materia
algebra = Materia('Algebra', 'Ricardo Quinteros', 2010)
fisica = Materia('Fisica', 'Javier La Porte', 2006)
quimica = Materia('Quimica', 'Lorena Rios', 2003)

tarot = Materia('Tarot', 'Tu Sam', 2008)
ing.agregarMateria(tarot, 169)



print(algebra.fechaInicioDictado)
print(fisica.fechaInicioDictado)
print(quimica.fechaInicioDictado)
print(tarot.fechaInicioDictado)



