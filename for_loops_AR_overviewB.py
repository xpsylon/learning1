contador = 0
frase = input('Frase: ')

for vocal in frase:
    if vocal in 'aeiou':
        contador += 1
print('la cantidad de vocales es', contador)
