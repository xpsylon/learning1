#VARIABLES HAVE ADDRESSES, WHICH YOU CAN CALL WITH id()
#if a variable is equal to another one, a = b, they will get the same address
num = 6
id(num)
print(id(num))

name = 'javier'
id(name)
print(id(name))

a = 11
b = a
print(id(a))                                        # a and b have same address
print(id(b))

id(11)                                              # adressess are related to the object, not to the variable. same address as a and b
id('javier')                                        # same address as name

a = 10                                              # now i change the value of a. Though b doesnt change
id(a)                                                  # automatically as well, its value is still 10. so now they will have different addresses
id(b)

#an address not tagged by any variable is ready for GARBAGE COLLECTION

#constant names are written with CAPITAL LETTERS

PI = 3.1416                                         #PI is a constant
print(a * PI)

type(a)                                             #find out variuable type

