#Construye un programa que, al recibir como datos el peso, la altura y el genero
#de N personas que pertenecen a un estado de un pais, obtenga el promedio del
#del peso y el de la altura, tanto de la poblacion masculina como de la femenina.

#ERRORES:
#si algun genero == 0, ZeroDivisionError.
#necesita un check para genero M o F



check = True

while check == True:
    n = int(input('Cantidad personas a ingresar: '))
    g_masc = 0 #PONERLAS DENTRO DEL PRIMER IF...
    g_fem = 0
    h_masc = 0
    h_fem = 0
    k_masc = 0
    k_fem = 0

    if n > 0:
        check = False
        print('OK')
        
        for i in range(n):
            h = int(input('Altura cms: '))
            k = int(input('Peso kgs: '))

#check_g tiene que ir despues de la altura y peso para q solo se repita el input de genero           
            check_g = True
            while check_g == True:
                genero = input('Genero (M) (F): ')
                genero = genero.lower()
                        
                if genero == 'm':
                    check_g = False
                    g_masc += 1
                    h_masc += h
                    k_masc += k

                elif genero == 'f':
                    check_g = False
                    g_fem += 1
                    h_fem += h
                    k_fem += k

                else:
                        print('El genero es incorrecto. Reintroduzcalo...')
        #inicializamos variables avg_ con valor 0 para que se impriman aun con g_ a 02
        avg_h_masc = 0
        avg_k_masc = 0
        if g_masc > 0:        
            avg_h_masc = h_masc / g_masc
            avg_k_masc = k_masc / g_masc
        
        avg_h_fem = 0
        avg_k_fem = 0
        if g_fem > 0:
            avg_h_fem = h_fem / g_fem
            avg_k_fem = k_fem / g_fem

        print('Promedio altura masculina:', avg_h_masc)
        print('Promedio altura femenina:', avg_h_fem)
        print('Promedio peso masculino:', avg_k_masc)
        print('Promedio peso femenino:', avg_k_fem)

    else:
        print('Numero incorrecto. Reingreselo...')






        




