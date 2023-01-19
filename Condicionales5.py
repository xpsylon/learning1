#vamos a utilizar los operadores AND y OR:
#AND: y ademas...
#OR: o si no...

#Programa de becas: evalua la distancia al centro de estudios, la cantidad de hermanos en el centro y el salario
#familiar anual.
#distancia > 40km
#hermanos > 2
#salario < 20000 eur

print('Programa de becas 2022') #introduccion al programa.

distancia = int(input('Introduce la distancia a la escuela en kms.: '))
print('Distancia a la escuela:', distancia, 'kms')

hermanos = int(input('Introduce el numero de hermanos que tienes en el centro: '))
print('Numero de hermanos en el centro:', hermanos)

salario = int(input('Salario anual bruto en euros: '))
print('Salario anual bruto', salario, 'euros')

#if distancia > 40 and hermanos > 2 and salario <= 20000:
#    print('Tienes derecho a beca')
#else:
#    print('Beca denegada')
# con AND tiene que cumplir absolutamente todas las condiciones para tener derecho a beca.

#ahora usamos OR para que si no se cumpliesen los dos primeros supuestos, de todos modos al tener un salario bajo,
#tendria derecho a beca:

if distancia > 40 and hermanos > 2 or salario <= 20000:
    print('Tienes derecho a beca')
else:
    print('Beca denegada')

#vamos a utilizar el operador IN para ver si esta presente en:
print('Asignaturas optativas año 2022') #titulo
print('Informatica grafica - Pruebas de software - Usabilidad y accesibilidad') #subtitulo

minuscula = input('Que asignatura deseas cursar?: ')
asignatura = minuscula.lower() #para concertir el input a minuscula y coincida con el if:

if asignatura in ('informatica grafica', 'pruebas de software', 'usabilidad y accesibilidad'):
    print('Asignatura elegida: ' + asignatura)
else:
    print('La asignatura elegida no se encuentra disponible')
    
    
    










 







