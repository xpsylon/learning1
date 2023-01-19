#del ejercicio Programacion desde cero AR 10.1
#utilizamos la web pythontutor.com

def validar(email):
    caracterBuscado = '@'
    emailValido = False
    for c in email:
        if c == caracterBuscado:
            emailValido = True
            break
    return emailValido #retorna True o False

#programa principal (ambito global)
direccion = input('Tu email: ')
if validar(direccion): #llama a la funcion, la chequea, duevuelve True o False y en base
    #a eso seria if emailValido True o False
    print('Direccion valida')
else:
    print('Direccion invalida')
    
