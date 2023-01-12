#LIST ARE SIMILAR TO ARRAYS BUT ACCEPTING DIFFRENT KIND OF DATA TYPES
#Use [] for creating list, separing items by the comma
names = ['javier', 'asia', 'sofia', 'martin']
numbs = [12, 26, 32, 45, 57, 66, 78]

#You can create a LIST including LISTS inside
varios = [names, numbs]
print(varios)
print(names)
print(numbs)

#LISTS ARE MUTABLE

numbs.append(101)               #adds the number to the end of the list
print(numbs)

numbs.insert(2,30)              #adds number in between list. first argument is position, second is value
print(numbs)

numbs.remove(45)                #removes the value from the list
print(numbs)

numbs.pop(1)                    #removes the index number (position) from the list
print(numbs)

numbs.pop()                     #when we dont pass argument to pop will remove the last one. STACK. LAST IN FIRST OUT. PUSH POP
print(numbs)

del numbs [2:]                  #to delete more values at once. Begin index value to end index value (lists positions)
print(numbs)

numbs.extend([40, 18, 65])      #adds more values at the same time. Use brackets and square brackets. Square brackets are for multiple values
print(numbs)

numbs.sort()                    #sorts the list
print(numbs)

# SOME IN BUILD FUNCTIONS
min(numbs)                      #smallest number from list
max(numbs)                      #highest number from list
print(min(numbs))
print(max(numbs))
sum(numbs)                      #addition of all lists values
print(sum(numbs))
