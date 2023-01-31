#Dado el siguiente diccionario:
E = { 1:"a", "prueba":[1,2,3,5], (4,5):3}

#¿Es el 1 un elemento de E?
#no, los elementos solo pueden ser pares formados por clave:valor

# ¿Cuántos elementos tiene E?
#3 elementos(pares)

#Por qué da error la instrucción E[0]?
#porque no hay ninguna clave 0

#¿Qué retorna la instrucción 1 in E.values()?
#False

#¿Qué retorna E["prueba"][2] y por qué?
#Retorna 3, indice lista valor[2]

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
cadena = input('Escriba algo: ')
ocurrencias = {}
for i in cadena[:51]:
    ocurrencias[i]= cadena.count(i)
print(ocurrencias)
