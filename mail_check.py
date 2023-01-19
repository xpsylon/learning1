contador = 0

miMail = input('Introduce tu mail...: ')

for i in miMail:
    if '@' and '.' in miMail:
        contador += 1

if contador >= 2:
    print('OK')
else:
    print('WRONG!!')
