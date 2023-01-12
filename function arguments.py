#lesson 33 Navin Reddy
def update(x): #define the function with parameter x
    x = 8 #updating x value to 8
    print(x)

update(10) #calling the function with an argument of 10 for parameter x.
#but later in the function the variable will be updated to 8 (x=8). so it will print 8

#now we pass an value through an internal variable:
def update1(x):
    print(id(x)) #9801536
    x = 8 #*
    print('x =', x)
    print(id(x)) #9801472// after changing x to 8 changes the address

a = 10
update1(a) #will print x = 8, *updated value inside the function

print('a =', a) # will print a = 10, external variable value.
print(id(a))#9801536

#pass by value. copia. passes the value itself
#pass by reference. cambia la referencia. passes the address where that value is stored.

#now we do the same with mutable objects like a list:
def update2(lista):
    print(lista)
    print(id(lista))
    lista[0] = 66
    print(lista)
    print(id(lista)) #here wont change the address hence list is a mutable object

lista = [10, 25, 48]
update2(lista)
print(id(lista))
     

