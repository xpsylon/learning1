#DECORATOR ONCE AGAIN
def imp_arg(func_par):
    def func_int(the_number):
        print('Argument for', func_par.__name__, 'is', the_number)
        return func_par(the_number) #not strictly necessary.
    return func_int

@imp_arg
def mas_uno(x):
    return x + 1
mas_uno(10)

#ANONYMOUS FUNCTIONS (LAMBDA)
#Sometimes naming a function is not worthy, because you will use it just one time. In this case, Python offers the
#Lambda functions

#we assign KEYWORD lambda function to a variable:
add_one = lambda x: x + 1

#map():returns the specified iterator with the specified function applied to each item
#syntax: map(function, iterables)

numbers = [1, 2, 3, 4] #lista
times_two = map(lambda x: x * 2, numbers)#variable = map(lambda function, iterable)

	

