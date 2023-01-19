#Procesar montos compras de un cliente. Corta bucle con 0.

suma_montos = 0
monto = int(input('Ingrese el primer monto, ingrese 0 para parar: '))


while monto != 0:
    if monto < 0:
        print('Monto no valido')
    else:
        suma_montos += monto
    monto = int(input('Ingrese otro numero, ingrese 0 para parar: '))
if suma_montos > 1000:
    suma_montos *= 0.9
    
print('Monto a pagar', suma_montos)

    
