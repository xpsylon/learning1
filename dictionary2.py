#CREATING A DICTIONARY
telefonos = {'Javier': '666999666', 'Asia': 645454545}
vacio =  {} #will create an empty dict. if you want to create an empty set, you have to use:
vacio2 = set()

#adding key-value pairs to a dict.:
telefonos['Maria'] = '741414141'

#deleting key-value pair. with del() PYTHON built in FUNCTION:
#just input the key inside the del():
del(telefonos['Javier'])

#Retrieving single values from a dictionary using DICT METHOD .get():
config = {'host': 'example.org'}
config.get('port', 80) #will output 80, though this key-value pair is not saved in the dictionary.
config.get('host') #will output example.org. with .get you have always to input the key to get the value as an output
config.get('schema') #blank output. key not in dict

#Overwriting dict entries simply assign a new value to the key:
telefonos['Maria'] = '8585858585'

#Retrieving values by key:
telefonos['Maria']

#using KEYWORDS try...except instead of .get for retrieving a single value:
try:
    telefonos['Jose']
except:
    print('Jose is not here')
#great synthax!
#love python!

#Valid dict values: you can put any data type in a dictionary. Even nested dictionaries, lists, tuples.
diccio1 = {'subdiccio': {'blanco': True}, 'listita': [100, 205, 310]}
diccio1['subdiccio']['blanco'] #for getting value from subdict always input key
diccio1['listita'][1] #for lists inside dict, list name and index number

runners = {1000: 'Javier', 1001: 'Sofia', 1002: 'Martin'}
runners[1001]

#Creating dictionary using dict() PYTHON build in FUNCTION
#builds a dictionary from a list of key-value pairs (tuples)
diccio2 = dict([('Louie', 'capo'), ('Jacko', 'canario'), ('Tito', 'vodeville')])

#DICTIONARY COMPREHENSIONS
diccio3 = {x: x**2 for x in (2, 4, 6)}
# diccio = {key: expresion FOR key IN (values)}

#using .fromkeys DICT METHOD.
#can provide keys without values while creating dictionary.
#first we have to issue a list or a tuple
nombres = ('javier', 'asia', 'sofia', 'martin')
numeros = dict.fromkeys(nombres, ) #same as:
numeros = dict.fromkeys(nombres, None)

#checking if a key exists in a dictionary:
#you check with the 'in' and 'not in' KEYWORDS
'javier' in nombres # True
'carlos' in nombres # False
'vanina' in nombres # False
'vanina' not in nombres # True

#the len() in a dictionary returns the number of the key-value pairs.
len(numeros) # 4

#DICTIONARY METHODS .keys() and .values()
edades = {'javier': 59, 'asia': 51, 'sofia': 16, 'martin': 30}
edades.keys() #dict_keys(['javier', 'asia', 'sofia', 'martin'])
edades.values() #dict_values([59, 51, 16, 30])

#you can save them in a variable as well
nombres1 = edades.keys()
anios = edades.values()

#looping through .values():
for anios in anios:
    print(anios)

#looping through keys:
for nombres1 in nombres1:
    print(nombres1)

#.items()
#returns a list containing a tuple for each key-value pair. Returns an iterable object which you can
#loop with a for-loop.
#if you for-loop through a dict, you will get just the keys as returns and not the values

edades.items()
#dict_items([('javier', 59), ('asia', 51), ('sofia', 16), ('martin', 30)])

for x, y in edades.items():
    print(x, ':', y)

#ESTOY ENTENDIENDO LAS PUTAS FOR-LOOPS!

#returning lists from the keys (just) with the built in PYTHON FUNCTIONS list() and sorted().
#it doesnt work with the values
print(list(edades))
print(sorted(edades))

#MERGING DICTIONARIES
#from Python 3.9 on you can use:
#merged = dict1 | dict2
#for Python 3.8 use:
diccio4 = {'a': 1, 'b': 2}
diccio5 = {'b': 3, 'c': 4}
merge = {**diccio4, **diccio5}
print(merge)
#whenever a key 'k' is present in both dicts, only diccio5[k] will be kept
merge2 = {**diccio5, **diccio4}
print(merge2)

#COMPARING DICTIONARIES
#you just need to use the == operator
diccio6 = {'a': 1, 'b': 2, 'c': 'jose'}
diccio7 = {'a': 1, 'b': 2, 'c': 'jose'}
diccio6 == diccio7 #True

#dictioanries with same content but in different order are == True as well:
diccio8 = {'ema': 1005, 'jorge': 'perro', 500: False}
diccio9 = {500: False, 'ema': 1005, 'jorge': 'perro'}
diccio8 == diccio9 #True
