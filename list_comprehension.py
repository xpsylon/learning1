#LIST COMPREHENSION
#List comprehension offers a shorter syntax when you want to create a new list
#based on the values of an existing list.

#Example:
#Based on a list of fruits, you want a new list, containing only the fruits
#with the letter "a" in the name.

#without list comprehension:
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [] #creating new empty list

for x in fruits:
    if 'a' in x:
        newlist.append(x)

#with list comprehension:
newlist2 = [x for x in fruits if 'e' in x]

#the default syntax:
#newlist = [expression for item in iterable if condition == True]
#the return value is a newlist. the original one remains unchanged.

