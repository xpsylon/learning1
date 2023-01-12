#-------CLASS COMPUTER -------------
class Computer:

#OVERRIDE _INIT_
    def __init__(self):
        print('in init')                      #will be printed by any call of an object belonging to class Computer

#FUNCTION (METHOD) DEFINITION
    def config(self):
        print('16 TB')

#INSTANCE (OBJECT) OF CLASS COMPUTER
com1 = Computer()
com2 = Computer()

#FUNCTION CALL
#config()                    # not defined error, add class
#Computer.config(self)        # self not defined, add object
#Computer.config(com1)

#---FUNCTION CALL 2nd WAY (LIKE IN 1st FILE)
com1.config()
com2.config()

#means config is method from object COM1 and com1 is instance (object) from class COMPUTER
# this will pass argument com1 to parameter self

#--ANOTHER TEST---
#a = 5
#print(a.bit_length())
#print(type(a))


