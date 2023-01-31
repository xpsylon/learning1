##VERSION PROFESORA
##Escribir un programa que procese strings ingresados por el usuario.
##La lectura finaliza cuando se hayan procesado 50 strings.
##Al finalizar, informar la cantidad total de ocurrencias de cada carácter,
##en todos los strings ingresados. Ejemplo:
##"r": 5
##"%": 3
##"a": 8
##"9": 1
##¿Cómo se podrían informar las ocurrencias de las letras del alfabeto
##únicamente, incluyendo el valor 0 para las letras que no aparecieron?

#crear diccionario contador
contador = {}
#para que contabilice solo las letras del alfabeto:
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
#para que cada letra (clave) arranque con cantidad (valor) 0:
for letra in alfabeto:
    contador[letra] = 0
#iteracion de x veces:
for i in range(3):
    #leer cadena
    cadena = input('Cadena de caracteres: ')
    cadena = cadena.lower()
    #iteracion por cadena
    for j in cadena:
        if j in alfabeto:
        #se suma 1 a la cantidad (valor) de la clave
            contador[j] += 1
for x, y in contador.items():
    print(x,':',y)
