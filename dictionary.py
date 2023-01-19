#DICTIONARIES ARE SIMILAR TO LIST, TUPLES AND SETS
#They use {}
#They have keys and each key has a value
#You fetch the value by inputting its key

from fileinput import close


diccio = {1:'blanco', 2:'negro', 3:'rojo', 4:'azul'}                #create dictionary
print(diccio)                                                       #prints outputs the list with a space between key and value
print(diccio[4])                                                    #if you input a key which doesnt exist will output an error/ like diccio[5]

diccio.get(5)                                                       #if you use the function get though key is missing will not output error
#print(diccio[5])
print(diccio.get(5))                                                #with get you use () for the indexation
print(diccio.get(5, 'not found'))                                   #if the key is not there will output not found

#we will do a dictionary with DICT out of two lists and put them together with ZIP
nombres = ['javier', 'asia', 'sofia', 'martin']
progs = ['python', 'php', 'java', 'html']

datos = dict(zip(nombres, progs))
print(datos)                                                        #prints the dictionary with {}
print(datos['javier'])                                              #input key outputs value. here 'phyton'

datos['mama']= 'css'                                                #adding a new key and value to the dictionary
print(datos)

del datos ['asia']                                                  #will remove the key and its value
print(datos)

#creating a dictionary with lists and a subdictionary inside
paises = {'es': 'madrid', 'de': 'berlin', 'uk': ['london', 'glasgow'], 'us': {'mass': 'boston', 'cal': 'la'}}
print(paises)
print(paises['es'])                                                 #printing value of 'es': madrid
print(paises['uk'] [0])                                             #printing first value of 'uk': london
print(paises ['us'])                                                #outputs whole 'us' subdictionary
print(paises['us'] ['cal'])                                         #outputs 2nd subvalue of value 'us'. Cannot be indexed because it is not a list


print(diccio.keys())                                                #prints the keys of variable diccio



