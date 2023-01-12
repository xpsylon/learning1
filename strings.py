#BOOLEANS
print(not True)
print(True and False)
print(False or True)
print(4<5)

#----------------------------------------------------------
#FOR LOOP AND WHILE LOOP
#outputs the string in vertical
#iterable object
for letter in 'Raskamussi':
    print(letter)

#FOR LOOPS IN LISTS
# lists are similar to arrays but contain many types of data
#list example:
#con x le estamos dando nombre a los items de my_list. Puede ser cualquier nombre
# Las listas se crean usando block quotes separados por comas
my_list= [1, 'jose', 'stravinski']
for x in my_list:
    print(x)

#print just one item from the list
#Recordar que el primer item siempre es 0
print (my_list[2])

#Acceso a los distintos items de una lista
my_list2 = [1, 2, 'Hola nabo', ['a', 'b']]
print (my_list2[0]) #imprime el primer item de la lista
print (my_list2 [3][1]) # imprime el item 3 subitem 1
print (my_list2 [2][0]) # imprime el item 2 subitem 0

#----------------------------------------------------------
#PHYTON WHILE LOOP
#while expresion is TRUE, do something

i = 1           # i igual a 1
while i <=8:    # mientras i sea menor o igual a 8
    print(i)    # imprime i
    i = i + 1   # i es AHORA igual a i + 1 y LOOP.....

# SI LLEGAMOS A TENER UN INFINITE LOOP CORTAMOS CON ctrl + c

#----------------------------------------------------------
#PRINT A RAW STRING
print('c:\docs\navin') # \n will add new line. so we avoid it with r (raw string)
print(r'c:\docs\navin')












