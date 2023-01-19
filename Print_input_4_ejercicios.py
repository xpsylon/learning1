#PROBLEMA ESTADIO EMPRESARIO ENTRADAS:

#constantes:
AFORO_M2 = 4
PORCENTAJE_GRADAS = 0.2
ENTRADAS_ESPECIALES = 0.3
ENTRADAS_COMUNES = 0.7

#datos
metros_estadio = float(input('Metros estadio: m2 '))
publico_gradas = int(input('Aforo gradas: '))
espacio_escenario_porciento = float(input('Porcentaje escenario: '))

#calculos espacio
metros_gradas = metros_estadio * PORCENTAJE_GRADAS
metros_escenario = metros_estadio * (espacio_escenario_porciento / 100)
metros_disponibles = metros_estadio - metros_gradas - metros_escenario
aforo_publico = (metros_disponibles * AFORO_M2) + publico_gradas
publico_especiales = aforo_publico * ENTRADAS_ESPECIALES
publico_comunes = aforo_publico * ENTRADAS_COMUNES

#test
print('Capacidad publico:', int(aforo_publico))

#precios
precio_entrada_especial = int(input('Precio entrada especial: EUR '))
precio_entrada_comun = int(input('Precio entrada comun: EUR '))

#facturacion
facturacion = int((publico_especiales * precio_entrada_especial)) + int((publico_comunes * precio_entrada_comun))
print('Facturacion total: EUR', facturacion)







