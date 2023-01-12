#Modules are the ideal way to group and organize code, while packages are collections of Python modules
#If you create a single Python file to perform some tasks, that’s called a script. If you create a Python file to store
#functions, classes, and other definitions, that’s called a module. We use modules by importing from them, using the Python import statement

#You can import a Python module by using Python’s import keyword. We usually place module imports at the top of a script,
#but we don’t have to. E.g., sometimes you want to dynamically decide if you need to import a module,
#especially when that module takes up a lot of memory or other resources.

#now we will import a module:

import my_module
my_module.mi_funcion()

#We can also import specific parts of a module, like a function, variable, or class. To do so, use the following syntax:
#from my_module import my_function, my_variable

#for making the module name shorter for typing it over and over again, you can import it as an alias:
import my_module as m
m.mi_funcion()

from my_module2 import saludo
saludo()