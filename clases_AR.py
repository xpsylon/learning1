class Vehiculo:
    speed = 0
    started = False
    def __init__(self, marca, modelo, anio):
        self.marca1 = marca
        self.modelo1 = modelo
        self.anio1 = anio
        self.dictio = {}

    def startVehicle(self):
        self.started = True
        print('Arrancamos')

    def acelerarVehicle(self, aceleracion):
        if self.started:
            self.speed += aceleracion
            print(self.speed)
        else:
            print('Arranque primero el coche, bobo!')

coche1 = Vehiculo('VW', 'Golf', 2012)
coche1.dictio.update({'brand':coche1.marca1, 'model':coche1.modelo1, 'year':coche1.anio1})




    
        
    
    
