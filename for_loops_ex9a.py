#Construye un programa que, al recibir como datos el peso, la altura y el genero
#de N personas que pertenecen a un estado de un pais, obtenga el promedio del
#del peso y el de la altura, tanto de la poblacion masculina como de la femenina.

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
            genero = input('Genero (M) (F): ')
            genero = genero.lower()
            h = int(input('Altura cms: '))
            k = int(input('Peso kgs: '))
                        
            if genero == 'm':
                g_masc += 1
                h_masc += h
                k_masc += k

            elif genero == 'f':
                g_fem += 1
                h_fem += h
                k_fem += k

            else:
                    print('El genero es incorrecto. Reintroduzcalo...')
        
        avg_h_masc = h_masc / g_masc
        avg_k_masc = k_masc / g_masc
        avg_h_fem = h_fem / g_fem
        avg_k_fem = k_fem / g_fem

        print('Promedio altura masculina:', avg_h_masc)
        print('Promedio altura femenina:', avg_h_fem)
        print('Promedio peso masculino:', avg_k_masc)
        print('Promedio peso femenino:', avg_k_fem)

    else:
        print('Numero incorrecto. Reingreselo...')






        




