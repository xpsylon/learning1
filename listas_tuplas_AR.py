listita = [104, 'hola', 0.8, True, [1,2,3]]
listona = ['peron', 105, 'Taras Bulba', False]
pep = list('palabra')
grax = list()
rango = list(range(500,3))

for elemento in listona:
    print(elemento)
for i in range(len(listona)):
    #iteradora por rango de la longitud
    print(i)
#for i in len(listona):
    #da error xq len es 4. entonces int no puede ser iterable.
    print(i)
#con while i arranca con counter=0 y va iterando mientras el valor de i sea menor a
# len(listita), 4 en este caso. lista[i]...indice imprime el valor que corresponde a ese
#indice
i = 0
while i < len(listita):
    print(listita[i])
    i += 1




