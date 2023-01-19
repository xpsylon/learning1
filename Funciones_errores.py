#Usar variables globales dentro de las funciones es un ERROR!
def primo(num):
    for i in range(2, num):
        if numero % 2 == 0:
            return False
    return True


#Programa principal:
numero = int(input('Numero: '))
if primo(numero):
    print('Es primo')
else:
    print('No es primo')