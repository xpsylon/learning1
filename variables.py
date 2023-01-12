#VARIABLES STORE VALUES AND THE VALUES ARE CHANGEABLE
#you dont need to assign a type of value to the variable

x = 2               #assigning a value to variable
print(x + 3)

x = 9               #changing the value of the same variable
print(x + 3)

y = 3               #assigning a value to another variable
print(y)
print(x + y)

x = ('queso')       #can even change the type on the same variable
print(x)
x = 9
print(x + y)

 #UNDERSCORE replaces last result. Just working on REPL

# STRING VARIABLES
name = 'javier'
print(name)
print(name + ' la porte')

#FETCHING AN INDEX VALUE
print(name[2])      #prints index number 2 using javier as an array
print(name[-1])     #negative numbers count from backwards
print(name[0:2])    #print from 0 to 2 (excluded)
print(name[1:])     #print from 1 till the end
print(name[:4])     #print from the beginnig till 4(excluded)

# name[0:3] = 'gab'
# will output error. strings are unmutable

#but you can (outputs gabier)
print('gab'+ name[3:])

#IN BUILD FUNCTION (len) lenght
print(len(name))











