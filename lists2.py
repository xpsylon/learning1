#creating different types of lists:
listaNum = [1, 2, 3]
listaVacia = []

#lists can have any data type, including dictionary, tuples or other lists:
listaVarios = [1, 'Javier', {'age': 39}]
listaSublistas = [[], [], []]

#converting other data types into lists with the list() function:
list(range(1, 4)) #outputs [1, 2, 3]
#set to list:
list({1, 2, 2, 2, 3}) #set doesnt accept duplicates
#tuple to list:
list((1, 2, 2, 2, 3))

#accesing list elements with indexing:
listaIndex = ['javier', 2, 10, ('lex', 14)]
listaIndex[0]
#listaIndex[4] #out of range

#Get the last element of a list:
#In this case, we start counting at -1 instead of 0.:
listaNeg = [1, 2, 3]
listaNeg[-2] # outputs 2

#accesing nested lists elements:
listaNido = [['javier', 'asia'], [1, 2], [14, 252]]
listaNido[0][1] # asia
listaNido[2][1] # 252

#ADDING AND REMOVING ELEMENTS
#append(): list method
listita = [1, 2]
listita.append('javier') # va al ultimo lugar

#combine or merge two lists:
# add them together with the + operator. the original lists remain untouched
l1 = [1, 2]
l2 = [3, 4]
l3 = l1 + l2
# or add all elements from one list to the other with extend()
l1.extend(l2)

#pop items from list
# the pop() method removes and returns the LAST item by default unless you give an index argument
listis = [1, 2, 3, 4, 5, 6]
listis.pop() # removes 6
listis.pop(1) # removes 2

#for STACK use append() and pop() for adding and removing (the last element)

#using KEYWORD deL for deleting items (indexed parameter)
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = lista1
del(lista1[0])

#for removing specific values you use METHOD remove():
lista3 = [1, 2, 3, 4, 5, 6]
lista3.remove(5)

#to remove ALL items from a list, use the clear() METHOD
lista4 = [10, 11, 12, 13, 14, 15]
lista4.clear()

#for removing DUPLICATES, convert the list into a set:
lista5 = [1, 2, 2, 2, 3, 3, 4, 7, 10]
set(lista5) #like this wont be saved as a set, just a temporary output

set5 = (set(lista5))

#you can reconvert the set into list (not necesary though)
lista6 = set5 #still type set
lista7 = list(lista6)

#to replace an item, we just assign it a new value
lista8 = [4, 5, 6, 7, 8, 9]
lista8[0] = 205

#get list length: len() BUILT IN FUNCTION
lista9 = ['carlos', 2, 15, 0.25, True, {1: 'rojo', 2: 'verde'}]
len(lista9)

#count element occurrence in a list (how many times this element shows up in the list):
#count(): list method
lista10 = [1, 1, 2, 2, 2, 4, 5]
lista10.count(2) # output is 3

#check if an item is in the list (keyword IN):
#KEYWORD in can be used with KEYWORDS if and for
lista11 = [15, 'amor', 'yogur', 8, True]
if 'amor' in lista11:
    print('amor', 'AMOR', 'amor')

for jax in lista11:
    print(jax)

#find the index of an item in the list
lista12 = ['coche', True, 2, 5, {1:'us', 2:'pl'}]
lista12.index('coche')
lista12 = ['coche', False, 2, 5, {1:'us', 2:'pl'}]

lista13 = ['coche', 2, 5, 'us', 'pl']










































































