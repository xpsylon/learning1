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











