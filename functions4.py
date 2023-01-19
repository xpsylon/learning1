#there are two kind of functions:
#1-the ones which carry out a task
#2-the ones which return a value

#this is a task function:
def greet(name):
    print('Hola ' + name)

name = input('como te llamas? ')
greet(name)

#this is a return value function:
def add(x,y):
    z = x + y
    return z

x = int(input('enter a number '))
y = int(input('enter another number '))

result = add(x,y)
#here will not print the result, it is just saved

#now we will print it
print(result)

#with more arguments:
def add_sub(x,y):
    z = x + y
    w = x - y
    return z, w

x = int(input('enter a number '))
y = int(input('enter another number '))

suma, resta = add_sub(x,y)
#here will not print the result, it is just saved. will return values of z and w and save them in two variables:
#suma and resta.

#now we will print it
print(suma, resta)

