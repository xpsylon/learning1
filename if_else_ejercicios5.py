#PRACTICAS INGLES

fecha = input('Ingrese la fecha actual en formato: dia, DD/MM: ')
fecha = fecha.lower()

#hay que extraer de fecha sus distintas partes:
dia_semana = fecha[0:fecha.find(',')] #desde la primera letra del dia semana hasta el substring ',' (excluido) va a extraer el dia de la semana.
dia_numero = int(fecha[fecha.find(' '):fecha.find('/')])
mes = int(fecha[-2:]) #los dos ultimos caracteres del string. y los convierto a int

#condiciones 1
if dia_semana not in ('lunesmartesmiercolesjuevesviernes'):
    print('Dia de la semana erroneo')
elif dia_numero > 31:
    print('Dia erroneo')
elif mes > 12:
    print('Mes erroneo')
else:
    print(fecha)

#condiciones 2
if dia_semana in ('lunesmartesmiercoles'):
    aprobados = int(input('Cantidad de aprobados?: '))
    desaprobados = int(input('Cantidad de desaprobados?: '))
    porciento_aprobados = aprobados / (aprobados + desaprobados) * 100
    print(porciento_aprobados)
elif dia_semana == 'jueves':
    porciento_asistencia = float(input('Ingrese el porcentaje de asistencia: '))
    if porciento_asistencia > 50:
        print('Asistio la mayoria')
    else:
        print('No asistio la mayoria')
elif dia_semana == 'viernes':
    if dia_numero == 1 and (mes == 1 or 7):
        print('Comienzo de nuevo ciclo')
        q_alumnos_nuevo_ciclo = int(input('Cantidad alumnos nuevo ciclo: '))
        arancel_alumno = float(input('Arancel por alumno EUR: '))
        ingreso_total = arancel_alumno * q_alumnos_nuevo_ciclo
        print(f'Ingreso total nuevo ciclo {ingreso_total} EUR')
    else:
        print('Inscripciones solo 01/01 y 01/07')
else:
    print('Sin novedades para la fecha')

print('Bye')
