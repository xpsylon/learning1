q_iteraciones = int(input('Ingrese la cantidad de numeros a sumar: '))
total = 0

for i in range(q_iteraciones):
    num = int(input('Ingrese un numero: '))
    total += num
print('El total es', total, 'y se sumaron', q_iteraciones, 'numeros')

frase = input('Frase: ')
total_vocal = 0
for i in 'aeiou':
    if i in frase:
        total_vocal += 1
        i += i
        print(i)
print(i)
    
