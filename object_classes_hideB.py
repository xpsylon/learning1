
class Carrera:
    def __init__(self, nombre):
        self.nombreCar = nombre
        self.materiaCar = {}

class Materia:
    def __init__(self, nombre, profesor, fecha):
        self.nombreMat = nombre
        self.profesorMat = profesor
        #no puede ser anterior a 2006
        self._fechaInicioDictado = fecha                         

#atributo que sera enmascarado dentro de @property
#funcion built in para ocultar la parte set. reemplaza metodo getters.
#metodo mismo nombre que atributo fecha inicio en clase Materia.
#DECORATOR
#Para validar la fecha antes de pasarla
#guion bajo convierte el atributo en privado (invisible)

#@property es el metodo getter de python que permite acceder a atributos
#privados
        
    @property #decorador                                        
    def fechaInicioDictado(self):
        #print de test para comprobar que el atributo primero pasa por aqui:
        print('hola')
        return self._fechaInicioDictado

#decorador setter
#metodo mismo nombre pero bajo decorador setter.
#permite modificar atributos privados
    @fechaInicioDictado.setter 
    def fechaInicioDictado(self, fecha): 
        if fecha < 2006:
            self._fechaInicioDictado = 2006
        else:
            self._fechaInicioDictado = fecha


ing = Carrera('Ingenieria')
#hay que agregar argumento fecha al parametro que se agrego en el _init_ de Materia
algebra = Materia('Algebra', 'Ricardo Quinteros', 2010)
fisica = Materia('Fisica', 'Javier La Porte', 2006)
quimica = Materia('Quimica', 'Lorena Rios', 2003)

print(algebra.fechaInicioDictado)
print(fisica.fechaInicioDictado)
print(quimica.fechaInicioDictado)


