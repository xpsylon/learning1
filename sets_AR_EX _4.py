##Suponer una lista con datos de las compras hechas por clientes de una empresa a lo
##largo de un mes, la cual contiene tuplas con información de cada venta:
##(cliente, día del mes, monto, domicilio del cliente).
##

##Ejemplo: [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699,
##"Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
##("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]



##Escribir una función que reciba como parámetro una lista con el formato mencionado
##anteriormente y retorne los domicilios de cada cliente al cual se le debe enviar una
##factura de compra. Notar que cada cliente puede haber hecho más de una compra en el mes,
##por lo que la función debe retornar una estructura que contenga cada domicilio una sola vez.

compras = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699,
"Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]

def Domicilios(datos_clientes):
    direccion_cliente = set()
    for domicilio in datos_clientes:
        direccion_cliente.add(domicilio[3])
    return direccion_cliente

print(Domicilios(compras))
        
    

