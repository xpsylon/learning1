#A CONSTRUCTOR is a function that is created automatically when an object is created. It can accept arguments like a normal function

#---------WE CREATE A NEW CLASS OVERRIDING INIT METHOD (CONSTRUCTOR)----------
#It is the same as when we were creating the Car class, but instead of creating variables after default constructor,
#we override the _INIT_ method
class Ship:
    def __init__(self, started1 = False, speed1 = 0):       # INIT taking new parameters
        self.started1 = started1
        self.speed1 = speed1                                #aca no es = self.speed1 xq estamos en la def de INIT

    def arrancar(self):
        self.started1 = True
        print('Arrancamos')

    def acelerar(self, aclr):
        if self.started1:                   #Si true
            self.speed1  = self.speed1 + aclr
            print('Tsiuuuuuu')
        else:
            print('Arrancalo primero, papa!')

    def parar(self):
        self.speed1 = 0

#----CREAMOS varios OBJETOS (INSTANCIAS) con distintos parametros
barco1 = Ship()
barco2 = Ship()
barco3 = Ship()


print(barco1.speed1)
barco1.arrancar()
print(barco1.speed1)

barco2.acelerar(95)
print(barco2.speed1)

print(barco3.speed1)








