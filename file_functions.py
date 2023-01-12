def suma_digitos(num):
    sumadigitos = 0
    while num != 0:
        digito = num % 10
        sumadigitos += digito
        num = num // 10
    return sumadigitos