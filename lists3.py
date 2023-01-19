#Loop over list elements
lista1 = [1, 2, 3, 4, 'jose']

for item in lista1:
    print(item)

#list to string:	
#you can convert almost everything to a string:

lista2 = lista1
str(lista2)

#sorting a list
#two options:
#1-use built in list METHOD .sort
#2-use built in python function sorted()

#.sort modifies the list itself and doesnt return anything
lista3 = [5, 7, 1, 9, 3, 3, 0]
lista3.sort()

#sort with .reverse list METHOD
lista3.reverse() #backwards
lista3.reverse() #and backwards again
lista4 = [10, 2, 7, 9, 12, 1, 6]
lista4.sort(reverse = True)

#using python built in function sorted():
#returns a NEW LIST with the result. lista5 remains untouched.
lista5 = [15, 2, 4, 25, 0, 38]
sorted(lista5)

#using sorted() and .reverse together:
sorted(lista5, reverse = True)

#different data typed cannot be sorted inside a list.
#sorting strings:
lista7 = ['hijo', 'jose', 'alfa', 'romeo', 'delta']
sorted(lista7)

#SLICING: for getting parts of a list
#my_list[start:stop:step). index positions. stop is excluded.
#stop and step are optional.
lista8 = ['jose', 5, 9, False, 58]
lista8[1:4:] #1 to 4 (excluded), step 1 (by default)
lista8[::2] #all elements, step 2

#slicing with negative indexation:
#a negative step is mandatory
lista9 = [1, 2, 3, 4, 5, 6, 7]
lista9[-1:-3:-1]

#REVERSING:
#3 ways of reversing lists:
    #1-LIST built in METHOD .reverse. changes the list itself.
    #2-slicing with negative step. original list remains untouched.
    #3-using PYTHON built in FUNCTION reversed(). returns a reversed iterator.

lista10 = [1, 2, 3, 4, 5, 6, 7]
lista10.reverse()

lista11 = [8, 9, 10, 11, 12, 13]
lista11[::-1]

lista12 = [14, 15, 16, 17, 18, 19]
l12rev = reversed(lista12)
print(list(l12rev))

#reversed iterator with for in function:
lista13 = [20, 21, 22, 23, 24, 25]
l13rev = reversed(lista13)
for item in l13rev:
    print(item)











































































































