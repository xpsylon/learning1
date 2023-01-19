#creating a tuple:
mis_numeros = (1, 2, 3)
#en la tupla los parentesis redondos son opcionales:
lo_mismo = 1, 2, 3
print(type(lo_mismo))
print(type(mis_numeros))
texto = ('hola', 'carlos')
tambien = 'hola', 'jose'
print(tambien)
print(type(tambien))

#convertir lista en tupla:
print(tuple([0, 2, 4]))

#cuando es tupla y cuando numero individual:
t = (1)
print(t)
t2 = (1, )
print(t2)

#unpacking multiple lists into a tuple:
l1 = [1, 2, 3, 3]
l2 = [4, 5, 6]
tuplinga = (*l1, *l2) #el asterisco unpacks the list into individual elements.
print(tuplinga)
print(type(tuplinga))

#multiple assignment for tuples:
persona = ('javier', 59, True)
name, age, registered = persona #unpacks the tuple into single variables

#multiple values return:
def get_user_by_id(userid):
    #fetch user from database
    return name, age

#name, age = get_user_by_id(x)

#indexed access: 
my_mixed_tuple = 'Hello', 123, True

#append to a tuple directly is not possible (data unmutable). you can just create a
#new tuple out of the old one and add new elements.
t1 = (1, 2, 3)
t = (*t1, 'extra', 'items')

#get tuple length
tupleta = 1, 2, 3, 'trinitotolueno'
len(tupleta)

#TUPLE vs. SET
#the main difference is tuple can have duplicates and sets dont

#converting tuple to list:
tuplin = 1, 2, 3
list(tuplin)

#converting by unpacking:
listin = [*tuplin]

#...and adding:
listin = [*tuplin, 'carozo', False]

#converting tuple to set:
tuplin1 = 'rocamora', 1452, True

settt = (set(tuplin1))

#...and by unpacking (and adding)
sett2 = {*tuplin, 870}

#convert tuple to string:
tupla3 = (10, 25, 487)
str(tupla3)













