numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
alfanum = numeros + [letras]
alfanum1 = numeros + letras

#En que posicion se encuentra x elemento en la lista: .index
alfanum.index(3)

#Modificar elemento: lista[pos] = nuevo valor
numeros[2] = 88
cuadrados = [1, 4, 9, 16, 25]
cubos = [1, 8, 27, 65, 125]
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
alfanum2 = cuadrados[0:3], letras[-3:]
alfanum3 = [cuadrados[0:3], letras[-3:]]


a, b = 0, 1
for i in range(10):
    print(a, end=',')
    a, b = b, a+b
pepardo = 'los ovos de peroun'
#lista paso -1 imprime lista al reves

alfanum4 = [numeros, letras]
#list.insert(posicion, elemento)
alfanum4.append(['paco', 101])









