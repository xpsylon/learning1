def identificador(nombre, apellido, dni):
    ident_socio = nombre.strip() + str(len(apellido)) + str(dni[0:3])
    return ident_socio

def validar_dni(doc):
    digitos = 0
    while doc != 0:
        doc //= 10
        digitos += 1
    return digitos == 7 or digitos == 8       