#We have three kind of errors in python:
    #1 compile time (syntactical errors)
        #like forgetting the : in a statement
    #2 logical
        #output errors due to bugs
    #3 run time
        #user input errors like dividing by 0

#lesson 63 Navin Reddy
a = 5 #statement 1 (normal: will not give error)
b = 2 #statement 2 (normal: will not give error)

print(a/b) #statement 3 (critical: may give error)

print('bye') #statement 4: to check if code runs until the end
print('----------------------')

c = 5
d = 0

#print(c/d) #outputs error. stops execution.

print('bye')

#we add 'try' 'except' block:
try: #try to execute this statement, which may give error (critical)
    print(c/d)
except Exception: #if it gives error i will handle it.
    print('you cant divide by zero')

print('----------------------')



e = 10
f = 0

try:
    print(e/f)
except Exception as e: #e is the representation of the error
    print('you cant divide by zero', e) #will be printed at the end of our message.
print('bye')

print('----------------------')


#we have to finish (close) the resources we are using, no matter if its after 'try' or 'except' block.
#we use 'finally'
g = 14
h = 5

try:
    print('resource open')
    print(g/h)
    print('resource closed') #here if the 'except' block would be executed, the resource would not be closed.

except Exception as e:
    print('you cant divide by zero')

print('bye')
print('----------------------')

g = 14
h = 0

try:
    print('resource open')
    print(g/h)

except Exception as e:
    print('you cant divide by zero')
    print('resource closed') #will not be closed if 'try' block is executed

print('bye')
print('----------------------')
#the solution is to add the 'finally' block:
g = 14
h = 0

try:
    print('resource open')
    print(g/h)

except Exception as e:
    print('you cant divide by zero')

finally:
    print('resource closed')

print('bye')
print('----------------------')
g = 14
h = 5

try:
    print('resource open')
    print(g/h)

except Exception as e:
    print('you cant divide by zero')

finally:
    print('resource closed')

print('bye')
print('----------------------')





