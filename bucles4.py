#CONTINUE, PASS Y ELSE
#continue: ignora la instruccion dentro del bucle que contiene esta palabra y pasa a la siguiente
#pass: para mantener una clase o un bucle vacio a la espera de su programacion. Devuelve Null
#else: uso similar en los bucles y en los condicionales.

#continue:
palabra = input('Introduce una palabra que contenga la letra S: ')

for letra in palabra:
    if letra == 's':
        continue
    print(letra)

#contar letras y no caracteres. con len() solo podemos contar los caracteres de un string. para poder contar
#solo las letras habria que proceder asi:

frase = input('Introduce una frase ')
contador = 0

for letra in frase:
    if letra == ' ':
        continue
    contador += 1

print(contador)

#else no es estrictamente necesario con un bucle for. hay que leerlo con cuidado en este caso, pues tendemos a
#leerlo como el else de un if.
email = input('Introduce tu mail, por favor: ')

for i in email: # itera por mail introducido
    if i == '@': #si...
        arroba = True # se crea una variable booleana arroba con valor inicial True
        break #  y se sale de la iteracion for
else: # una vez que termina de iterar y no encuentra @, arroba pasa a ser False
    arroba = False
print(arroba)








 
