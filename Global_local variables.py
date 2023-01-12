#GLOBAL VARIABLES CAN BE REACHED ANYWHERE even inside the function
#LOCAL VARIABLES by the other hand ONLY WORK INSIDE THE FUNCTION 

a = 22 #global variable

def algo():
    a = 10 #local variable
    print('local', a)

print('global', a) #prints global
algo() #prints local

#now we delete the local variable and we will use the global variable inside the function.

b = 524 #global variable

def algo2():
    print(b) #we print the global variable inside the function

algo2()

n = 88

def algo3():
    global n #we add global n if we want to change the value of the global
    #variable from inside the function.
    n = 12
    print('local', n)

algo3() 

print('global', n)# will output 12 because will be printed AFTER function
#execution

#using the global variable inside the function without defining a local one:
j = 'GLOBAL'

def texto():
    print(j)

texto()

#now we need to use a local and global variable in the same function:

x = 11 #first value

def algo4():
    global x
    x = 22 # changes global to 22
    print('tito', x) #prints 22
    x = 33 #changes global value to 33
    print('lila', x) # prints 33

algo4() #calls function
print('pepe', x) #prints global value 33 again

#if we want to have a local and a global variable inside the function with the same name we need to use the
#globals() function

d = 'bananas'
e = 115
print(id(d))

def algo5():
    d = 'manzanas' #local d
    x = globals()['d'] #global d
    print('IN', d) #prints local d
    print(e) #prints e (global)
    print(x) # prints global d through x
    globals()['d'] = 'peras' #changes global d to peras
    print(id(x)) #will show same as id d (global)
    

algo5()
print('OUT', d) #prints global d (peras)



















































