#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = []
newlist=[]

#Traditional way
for x in fruits:
  if "a" in x:
    newlist1.append(x)

print(newlist1)

#Using list comprehension

newlist=[x for x in fruits if 'a' in x]
print(newlist)

#Syntax --> newlist = [expression for item in iterable if condition == True]

newlist=[x for x in  fruits if x!='apple']
print(newlist)

#The iterable can be any iterable object, like a list, tuple, set etc.

#We can use the range() function to create an iterable:

numlist=[x for x in range(10)]
print(numlist)

#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list.
newlist = [x.upper() for x in fruits]

#To Set all values in the new list to 'hello':
newlist2=['hello' for x in fruits]
print(newlist2)

newlist = [x if x != "banana" else "orange" for x in fruits]
