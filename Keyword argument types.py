#lesson 35 Navin Reddy
#KEYWORDED VARIABLE LENGTH ARGUMENTS

#when we have to pass an unknown amount of keywords (key-value pair) we use **:
def person(name, **data): #parameters name and unknown amount of keywords in data
    print(name)
    print(data) #will be a dictionary

#person('javier', 59, 'buenos aires', 666999666) #will output 'takes 1 POSITIONAL argument but 4 were given.
#it HAS to be keywords with **

person('javier', age=59, city='buenos aires', tel=666999666)

def person2(name, **data): #parameters name and unknown amount of keywords in data
    print(name)
    #for llave, valor in data: #we have to add DICT METHOD .items
    for llave, valor in data.items():
        print(llave, valor)

person2('javier', age=59, city='buenos aires', tel=666999666)


        



