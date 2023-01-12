#HOW TO OPEN FILES
#you use the built in PYTHON FUNCTION open()
#the basic parameter is: open('filename')

#you have to close the file after reading por freeing system resources:

#variable = open('file.txt')
#print(variable.read())
#variable.close()

catso = open('testa2.txt')
print(catso.read())
catso.close()

#USING 'with' with open() in python:
#if an exception occurs while python reads the file, the close() will never be reached and the software will
#carry on running. or maybe you just forget to close().
#use 'with' to keep the opened file just in the indented part of the code:
with open ('testa2.txt') as kiko:
    pepo = (kiko.read())

print(pepo)

