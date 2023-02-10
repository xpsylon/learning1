#An object is a collection of data (variables)(attributes) and methods (functions) (behaviours) that operate on that data. Objects are defined by a Python class.
#Since objects are the building blocks of the Python language, it’s only logical that you can create objects yourself too.
#If you want to create your own type of object, you first need to define its methods and what data it can hold. This blueprint is called a class.
#A class is the blueprint for one or more objects.
class Car:                              #defining a class called Car
    speed = 0                           #variable int
    started = False                     #variable bool

# creating function with def inside the class. Here there are called methods
# When a function is part of an object or Python class, we call it a method.
# The self parameter is a reference to the current instance of the class, and
# is used to access variables that belongs to the class.

#------METHODS (FUNCTIONS) INSIDE THE CLASS----------------------------
    def start(self):
        self.started = True             #parameter self with variable started from the class
        print('Vehicle started, lets go')

    def increase_speed(self, acel):     #acel va a ser el paramatro para la velocidad, al dar el valor se vuelve argumento
        if self.started:                #si started True, entonces speed original 0 + argumento acel
            self.speed = self.speed + acel
            print('Vrooom!')
        else:
            print('You have to start the vehicle first')  #aqui else es started false

    def stop(self):
        self.speed = 0
        print('Parando')

#When we call a method on a Python object, Python automatically fills in the first variable, which we call self by convention.
#This first variable is a reference to the object itself, hence its name
#We can use this variable to reference other instance variables and functions of this object, like self.speed and self.start().

#So only inside the Python class definition, we use self to reference variables that are part of the instance.
#To modify the started variable that’s part of our class, we use self.started and not just started.
#By using self, it’s made abundantly clear that we are operating on a variable that’s part of this instance
#and not some other variable that is defined outside of the object and happens to have the same name.



#now we create an object named coche of class Car
coche = Car()
coche.increase_speed(10)

coche.start()

coche.increase_speed(40)

coche.stop()

#-----------CREATING OTHER INSTANCES (OBJECTS) FROM THE SAME CLASS

moto = Car()
print(id(coche))                        #asignacion numerica unica a objeto
print(id(moto))                         #asigncion numerica unica a objeto

moto.increase_speed(52)                 #wont work before start
moto.start()
print(moto.speed)                       #velocidad de salida 0
moto.increase_speed(160)                #paso argumento 160 a parametro acel
print(moto.speed)                       #output updated speed

avion = Car()                           #creamos nueva instancia (objeto)
avion.start()                           #arrancamos el avion
print(avion.speed)                      #chequeamos velocidad avion parado
avion.increase_speed(int(input('Acelere! ')))       #input. ponemos la velocidad que queremos
print(avion.speed)                                  #output velocidad avion volando





