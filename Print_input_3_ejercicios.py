#GASTO COMBUSTIBLE MOTO:
km_litro = float(input('Cuantos kms. puede hacer su moto con 1 litro?: '))
tanque_litros = float(input('Cuantos litros tiene el tanque?: '))
ruta_kms = float(input('Cuantos kms tiene la ruta?: '))

litros_ruta = ruta_kms / km_litro
num_tanques = litros_ruta / tanque_litros

print('Va a necesitar', num_tanques, 'tanques')    
