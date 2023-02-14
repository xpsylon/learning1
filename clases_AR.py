class Vehiculo:
    speed = 0
    started = False
    def __init__(self, marca, modelo, anio):
        self.marca1 = marca
        self.modelo1 = modelo
        self.anio1 = anio
        self.dictio = {}

    def agregarCoche(self, codigo, marca, modelo, anio):
        self.dictio[codigo] = (marca, modelo, anio)
        self.dictio.update
        return self.dictio


coche1 = Vehiculo('', '', 0)

codigo = int(input('Codigo: '))
while codigo != 0:
    brand = input('Marca: ')
    model = input('Modelo: ')
    year = int(input('Año: '))
    codigo = int(input('Codigo: '))
    coche1.agregarCoche(codigo, brand, model, year)
