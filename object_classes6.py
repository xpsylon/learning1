#vamos a trabajar con super _init_ para tomar el constructor de la clase padre sin sobrescribirlo.
#la clase Empleado PODRIA ser una clase abstracta, si no queremos que se instancie ningun objeto de la clase Empleado, sino solo de sus Subclases.
class Empleado:
    def __init__(self, nombre, edad, legajo, sueldo):
        self.nombre1 = nombre
        self.edad1 = edad
        self.legajo1 = legajo
        self.sueldoBase = sueldo

    def calcularSueldo(self, descuentos, bonos): #Este metodo lo heredan tanto la clase AgenteViajes como Tripulante
        return self.sueldoBase - descuentos + bonos


class AgenteViajes(Empleado):
    def __init__(self, nombre, edad, legajo, sueldo, mostrador):        #parametros totales que toma la clase hija, se agrega parametro mostrador.
        self.numeroMostrador = mostrador                                #parametro mostrador se guarda en variable propia de objeto
        super().__init__(nombre, edad, legajo, sueldo)                  #funcion built in super: parametros que van a pasar a la clase padre


javier = AgenteViajes('Javier', 59, 'B105',5500, 5)
print(javier.numeroMostrador)
print(javier.sueldoBase)
print(javier.edad1)
print(javier.calcularSueldo(150, 386))

class Tripulante(Empleado):                                             #esta clase hija solo tiene el _init_ de la clase padre
    def mostrarRenovacionLicencia(self):                                      #metodo especifico de esta clase hija
        if self.edad1 > 50:
            print('Renovar cada 6 meses')
        else:
            print('Renovar cada anio')

lucas = Tripulante('Lucas', 35, 'A506', 6000)
print(lucas.mostrarRenovacionLicencia())
print(lucas.calcularSueldo(350, 586))



