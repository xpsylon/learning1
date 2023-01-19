#DIFFERENT WAYS OF CREATING SETS
#1-normal way through {}
set1 = {'jose', 25, True, 25} #doesnt allow duplicates, so it will not take the last 25

#2-using set() function:
set2 = set() #creating empty set with set() PYTHON FUNCTION
set2.add(2) #adding argument to empty set. just allows one argument.
set2.add('javier')

#3-using the SET METHOD .update. You can use another set or any iterable object like LIST, RANGE or TUPLE
set4 = set() #creating empty set with PYTHON FUNCTION set()
set4.update(range(5)) #updating (adding) from 0 to 5 (excluded). using RANGE
set4.update(['jose', False]) #doesnt allow to add True. Has to be iterable. using LIST
set4.update(('wolfskin', 478)) #using TUPLE
set4.update({'pantera', 'rosa'}) #using SET. Random output.

#converting any iterable (LIST, TUPLE, RANGE) object into set with PYTHON FUNCTION set()
lista14 = ['pierre', True, 125]
set(lista14) #conversion not saved, original list remains untouched

#set comprehension:
#newset = [expression for item in iterable if condition == True]
setIterarString = {x for x in 'Hola, que tal?' if x not in ', ?'}
#crear lista setIterarString
#iterando x en 'Hola que tal'
#siempre que no haya ', y ?'

#DEDUPLICATE A LIST: just convert it to a set
#set(list)

#SET to LIST:
#list(set)

#SET en castellano es CONJUNTO (diagrama de Venn)

#WHY WOULD YOU NEED SETS
#Remove duplicates from a list
#Perform membership testing(is an elemnt present in this set of unique elements)
#ALSO
#Finding difference between two sets
#Union: combining sets and only keeping unique elements
#Intersection: which elements are present in both sets
#Finding subsets and supersets

#MATHEMATICAL PYTHON SET OPERATIONS
#Finding difference between two sets:
    #means finding the elements that you find in JUST one set
    #we use the - (substractor operator)
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
A - B #will output 1,2
B - A #will output 6,7

#Finding the symetric difference:
    #the elements which are either in A or B but not in both
A^B #will output 1, 2, 6, 7

#Finding the intersecion: the common elements
A & B #will output 3, 4, 5

#Subsets and supersets:
#If A is a subset from B, means that all elements of A are present in B. However A may be smaller than B
#Though if A would have an element which is not present in B, A would not be a subset of B.
#We check subsets with the < operator

#If B is a superset of A, means that B has all elements of A but may have also extra elements.
#We check supersets with the > operator

C = {1, 2, 3}
D = {1, 2, 3, 4, 5}
E = {1, 2, 3, 10}

C < D #will output True
E < D #will output False
D > C #will output True
D > E #will output False (10 not in D)

#also:
C < C #False
C <= C #True
C >= C #True

#Union:
#We add two sets together and we keep just the elements which are unique
C | D #outputs 1, 2, 3, 4, 5

#NAMED SET METHODS
#Allmost all set operations have named equivalents like issubset().
#The main advantage of these last ones is that you can use them for all iterable elements, not just for sets.

#SETS CANNOT BE INDEXED because they no order, they are random




























































