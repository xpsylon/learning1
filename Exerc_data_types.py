saludo = 'holaa'
c = saludo[len(saludo)-1] # va a dar a: len saludo 5 -1: saludo[4]
e = 'z' + 'a' + 'paz'[0] # va a dar zap: z + a + p(paz[0]
x = e[0] == 'z' # va a dar True

edad = 16

#TABLAS DE VERDAD:
x = len('jugar') > 5 and len('jugar') < 10
print(x)
print('alto'[2] == 't'and x)
print((842913 % 10 != 3) and (len('jugar') == 3))
print(0 != 0 or 'a' < 'y')
print(True or int('50') >= 50)

edad = 20
es_cliente = False

print(not es_cliente and not edad < 18)
# not es_cliente : True
#edad < 18: False
#not False: True
#True and True: True

numero % 4 == 0 and numero < 0
km < 30000 and (mod >= 2015 and mod <= 2017)
porcentaje_completo > 30 and not miembro_agrupacion
#la supuesta variable porcentaje_completo guardaria valores del 1 al 100 (%) y miembro_agrupacion True o False.
#not miembro_agrupacion significa False, ya que la variable booleana sola, sin False o True, se presupone True.

es_invierno and not tiene_calefaccion and not esta_abrigada
#invierno: true, calefaccion not true, abrigada not true
es_invierno and not (tiene_calefaccion or esta_abrigada)
#true not (true or true)









