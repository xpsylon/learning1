#CADENA FIND:
#da la posicion del caracter que demos como parametro. Si es una palabra, da la posicion de la primera letra de
#dicha palabra.
#seria el opuesto a string[x] 

cadena = 'programacion en python'
print(cadena.find('g')) #3
print(cadena.find('en')) #13
# si introducimos un caracter que no existe, devuelve -1
print(cadena.find('j')) #-1

#esto ultimo se puede utilizar eventualmente para comparar:
print(cadena.find('l') == -1) #devuelve True

#INCLUSION DE CADENA:
#cadena1 'in' cadena2: devuelve bool
print('prog' in cadena) #True
print('tele' in cadena) #False

#upper and lower:
cadena.upper()
cadena.lower()

#title: pone la primera letra de cada palabra en mayuscula:
cadena.title()

#capitalize: pone la primera letra de la primera palabra en mayuscula:
cadena.capitalize()

#strip: elimina los espacios al principio y al final, no los del medio:
a = '    cara de     cartonero      '
print(a.strip())

#count: devuelve cuantas veces una subcadena aparece en una cadena:
print(cadena.count('p')) # devuelve 2
print(cadena.count('on')) # devuelve 2

#replace: reemplaza una cadena por otra:
#cadena.replace('cadena1', 'cadena2')
print(cadena.replace('python', 'nivel Dios'))
#se utiliza muy bien por ejemplo para reemplazar caracteres especiales (ñ, ó, ä) por caracteres universales.




