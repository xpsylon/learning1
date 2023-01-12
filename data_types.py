#DATA TYPES
#   NONE
#   NUMERIC
#       int
#           you can convert float to int: int(a)
#       float
#           and int to float: float(a)
#       complex
#           num = 8+12j
#           and to variables into complex: c = complex (a, b)
#       bool
#           give a condition will output TRUE or FALSE
#           a>b FALSE
#           assign to a variable: bul = a>b
#           if you convert bool to int, False is 0 and True is 1
#   LIST
#       list = [2,3, 'bananas]
#   TUPLE
#       tuple = (2, 3, 'bananas')
#   SET
#       set = {2, 3, 'bananas'}
#   STRING
#   RANGE
#       range(10) input
#       range(0,10) output
#       list(range(10)) input
#       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] output lists with range
#       parameter range (start. end. step)
print(list(range(1, 15, 2)))

#   DICTIONARY
#       dictionary = {2:'jose', 4:'asia', 7:'enero'}
#       to every value we assign a key
#       all keys have to be unique
paises = {1:'es', 2:'ar', 3:'de', 4:'pl'}
print(type(paises))
print(paises.keys())
print(paises.values())
print(paises[4])                            #without get use []
print(paises.get(1))                        #with get use ()

#
#
#
#

