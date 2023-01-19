#TYPES OF ARGUMENTS
#1-Position
#2-Keyword
#3-Default
#4-Variable Length

def add(a, b): #formal arguments
    c = a + b
    print(c)

add(5,6)#actual arguments

def person(name, age): #POSITION 1 name, position 2 age
    print(name, age)

person('javier', 59) #position 1 name, position 2 age
#you have to keep correct position when you call the function

#if you dont know the position, you can input as KEYWORD arguments:
def person1(name, age):
    print(name)
    print(age-5)

#person1(59, 'javier') #outputs error so then KEYWORD arguments:
person1(age=59, name='javier')

#now with a DEFAULT value in the parameter age:
def person2(name, age=18):
    print(name, age)

#if we dont input anything on age when calling the function, it will take the default.
#if we do input, will override the default one:

person2('javier') #outputs javier 1
person2('javier', 59) #outputs javier 59

#when we dont know how many arguments we will need, VARIABLE LENGTH:
def add2(a, *b): #a will take the values of the first argument and *b the rest (as a tuple)
    c = a + b
    print(c) #it means a will be an int and *b a tuple in case of more than one argument.
    

#add2(2, 7, 22, 4) #outputs error: not supported operand for int and tuple

def add3(a, *b):
    c = a #c starts taking the value of first argument (a)
    for i in b: #we need to loop through the tuple
        c += i
    print(c) #prints add
    print(a) #prints a(int)
    print(b) #prints b(tuple)

add3(2,7,22,4)

#if we use just ONE variable length argument, we can pass any kind of data:
def add4(*b):
    c = 0
    for lili in b:        
        c += lili
        print(c)

add4(40, 28, 17, 12)

def textito(*algo):
    for tito in algo:
       print(tito)
       print(type(algo))

textito('llave', 'pinguino')
    
























































