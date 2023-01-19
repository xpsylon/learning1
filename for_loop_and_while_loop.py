#FOR LOOP ITERATES OVER THE INDIVIDUAL ELEMENTS OF THE OBJECT YOU FEED
#An iterable is an object in Python that can return its members one at a time.
for carta in 'Holas':
    print(carta)                            #carta: variable interna del loop

#So we know that a for-loop can loop over iterable objects. By returning its members one by one, making it available
# in a variable (in the above example it’s the variable carta), you can loop over each element of an iterable
# with a for-statement.

#for <variable> in <iterable>
# ...do something with variable

#con listas:
mi_lista = [4, 'conejos', True]

#looping over the list:
for item in mi_lista:
    print(item)

print(mi_lista[0])

#WHILE LOOP:
#while <expression evaluates to True>:
#...do something

#You should read this as: “while this expression evaluates to True
#keep doing the stuff below”.
i = 1
while i <= 10:
    print(i)
    i += 2                              #same as i = i + 2

#with  keyword BREAK: stops the loop even if condition is still TRUE
i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i += 1

#With the CONTINUE keyword we can stop the current iteration, and continue with the next:
i = 1
while i < 8:
    i += 1
    if i == 5:
        continue
    print(i)                            #print despues de CONTINUE, sino se hace infinite LOOP

#With the else statement we can run a block of code once when the condition no longer is true:
a = 1
while a < 10:
    print(a)
    a += 1
else:                                   #check that ELSE is same level as WHILE
    print('ya llego a los 10')





