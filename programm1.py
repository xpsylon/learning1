# LITTLE PROGRAMM

# --------------DEFINICION FUNCION-------------
def hola(name):
    if name == '':  # si name vacio
        print('Pone tu nombre')  # output
    else:
        print('que tal')  # print que tal?
        for letra in name:  # for loop iterancia
            print(letra)  # print for loop


# ---------------------------------------------

# -------------INPUT AND FUNCTION CALL---------
name = input('tu nombre ')  # ask for INPUT and assigns it to a variable
hola(name)  # function call


# -------------EXERCISE INFINITE LOOP----------def jelou(nombre):
    while nombre:
        print('hola', nombre)


nombre = input('tu nombre')
#jelou(nombre)                          #function call is commented out
