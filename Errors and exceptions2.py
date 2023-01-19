a = 15
b = int(input('enter first number '))

try:
    print('resource open')
    print(a/b)
    c = int(input('please enter second number '))
    print(c)

except ZeroDivisionError as msg1:
    print('you cant divide by zero //', msg1)

except ValueError as msg2:
    print('incorrect input //', msg2)

except Exception as msg3:
    print('general error! //', msg3)

finally:
    print('resource closed')
    
