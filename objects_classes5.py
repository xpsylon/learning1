class Empleado:
    def __init__(self, nombre, edad, legajo, sueldo):
        self.nombre1 = nombre
        self.edad1 = edad
        self.legajo1 = legajo
        self.sueldoBase = sueldo

    def calcularSueldo(self, descuentos, bonos):
        return self.sueldoBase - descuentos + bonos

class AgenteVentas(Empleado):                                                     #clase hija de Empleado (inheritance)
    def __init__(self, mostrador):                                                #overwriting _init_ from clase padre Empleado.
        self.numeroMostrador = mostrador

pedro = AgenteVentas(1)
print(pedro.numeroMostrador)
print(pedro.nombre1)                                                              #no tiene atributo nombre1 xq sobrescribio el _init_ de clase padre

