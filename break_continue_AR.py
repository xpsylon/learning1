while True:
    print('Opcion 1 - comenzar programa')
    print('Opcion 2 - imprimir listado')
    print('Opcion 3 - finalizar programa')

    opcion = int(input('Opcion elegida: '))
    if opcion == 1: #sigue ejecutando el bucle xq while sigue siendo True
        print('Comenzamos!')
    elif opcion == 2: #sigue ejecutando el bucle xq while sigue siendo True
        print('Listado: ')
        print('Nadia, Esteban, Mariela, Fernanda')
    elif opcion == 3: #rompe el bucle
        print('Hasta la proxima')
        break
    else: #sigue ejecutando el bucle xq while sigue siendo True
        print('Opcion incorrecta. Debe ingresar 1, 2 o 3')
        
            
