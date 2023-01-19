#concatenacion de operadores de comparacion.
#para evitar una edad negativa se puede poner asi:

edad = int(input('Edad: '))

if 0 < edad < 100: # si 0 menor que edad y edad menor que 100...correcto. va evaluando de izquierda a derecha.
    print('Edad correcta')

else:
    print('Edad incorrecta')

#evaluacion salarios empleados empresa:

#PYTHON NO DEJA CONCATENAR DISTINTOS TIPOS DE DATOS:
salario_presidente = int(input('Introduce salario presidente: '))
#print('Salario presidente: ' + salario_presidente)
#TypeError: can only concatenate str (not "int") to str

#print('Salario presidente:', salario_presidente)
#pero si ponemos ',' en vez de ,+, funciona bien

print('Salario presidente: ' + str(salario_presidente))

salario_director = int(input('Introduce salario director: '))
print('Salario director: ' + str(salario_director))

salario_jefe_area = int(input('Introduce salario jefe area: '))
print('Salario jefe area: ' + str(salario_jefe_area))

salario_administrativo = int(input('Introduce salario administrativo: '))
print('Salario administrativo: ' + str(salario_administrativo))

#concatenamos los operadores de comparacion:
if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print('Empresa funciona')
else:
    print('Delirio total')





    


           
 
