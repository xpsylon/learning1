#La funcion INPUT toma str como data type predeterminado. Por eso hay que convertirlo al data type correspondiente

x = int(input('Primer numero, nabo! '))
y = int(input('Pone el otro! '))
z = x + y
print(z)
#----------------------------------------------------------
a = input('Enter a letter ')
print(a[0])                                                 #variante 1
#----------------------------------------------------------
b = input('Enter a letter ')[0]
print(b)                                                    #variante 2: input will fetch all inputs from user but will assign just first charachter to b
#----------------------------------------------------------
#function EVAL to test the input
c = eval(input('enter an expresion '))                       # function EVAL for fetching expressions
print(c)


