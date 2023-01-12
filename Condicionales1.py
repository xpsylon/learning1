#condicionales basicos:
print('Evaluacion de alumnos')
nota_alumno = int(input('Nota alumno: ')) #hay que poner int(input) xq todo python considera str todo lo que se introduce en input.

def evaluacion(nota):
    valoracion = 'aprobado'
    if nota < 5:
        valoracion = 'suspenso'
    return valoracion

print(evaluacion(nota_alumno))

a = int(input('valor de a: '))
b = int(input('valor de b: '))
if b > a:
    print('b is bigger than a' )
elif a == b:
    print('a and b are equal' )
else:
    print('a is bigger than b')

print('Verificacion de acceso')

    

    




