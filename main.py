# crea campo input nombre con texto predefinido COMO TE LLAMAS.
#input es una funcion
nombre = input('Como te llamas?')

#print nombre. no hay que formatear xq son 2 strings
print('Hola ' + nombre)

#pregunta la edad. Campo preedifinido con str// hay que convertirlo a int
edad = int(input('Cual es tu edad?'))

#guardo en una variable el valor true de 18 o mas anios
mayor_de_edad = edad >= 18

#si es hijo de duenio INPUT
pregunta_hijo_duenio = input('Sos hijo del duenio?')
respuesta_hijo_duenio = pregunta_hijo_duenio == ' si'

if mayor_de_edad or respuesta_hijo_duenio:
    print('Pues, pase Ud.!')
else:
    print('Es menor de edad')
    print('Se me retira inmediatamente!')

