class Ejemplo:
    def __init__(self, parametro1, parametro2):
        self.atributo1 = parametro1
        self.atributo2 = parametro2

un_ejemplo = Ejemplo('un valor', 'otro valor')
print(un_ejemplo)
print(un_ejemplo.atributo1)
un_ejemplo.atributo3 = 125

print(un_ejemplo.atributo3)

