#FECHA NACIMIENTO
dia = input('Ingresa el dia de tu nacimiento: ')
mes = input('Ingresa el mes de tu nacimiento: ')
anio = input('Ingresa el año de tu nacimiento: ')

fecha = dia + '/' + mes + '/' + anio
print(fecha)

fecha1 = int(input('Ingresa la fecha de tu nacimiento en formato DDMMYYYY: '))
anio1 = fecha1 % 10000
dia1 = fecha1 // 1000000
mes1 = (fecha1 // 10000) % 100
print(str(dia1) + '/' + str(mes1) + '/' + str(anio1))

fecha2 = input('Ingresa la fecha de tu nacimiento en formato DDMMYYYY: ')
dia2 = fecha2[:2]
mes2 = fecha2[2:4]
anio2 = fecha2[4:8]
print(dia2 + '/' + mes2 + '/' + anio2)
