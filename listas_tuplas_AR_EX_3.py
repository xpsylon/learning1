#test concatenando en vez de append:

lista = []
num = int(input('Numero: '))

while num != 0:
    lista += [num]
    num = int(input('Otro: '))
print(lista)

#con append:
numero1 = int(input('Numero: '))
lista1 = []
while numero1 != 0:
    lista1.append(numero1)
    numero1 = int(input('Otro: '))
print(lista1)
    
