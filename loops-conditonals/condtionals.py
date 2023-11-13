
#Basic implementation idea =>

if True:
    print('Condition is true')

if False:
    print('Condition is false')
    
#Testing for the variables:

language='Python'

if language=='Python':
    print('You are on right path')
    
#COMPARISONS =>
#Equal         ==
#Not equal     !=
#Greater than   >
#Smaller than   <
#Greater than or equal to   >=
#Smaller than or equal to   <=
#Object Identity     is

#If else block

if language=='Python':
    print('You are on right path')
else:
    print('You are on wrong path')
    
language='Java'

#Else if block
if language=='Python':
    print('You are on right path')
elif language=='Java':
    print('You are on good path')
else:
    print('You are on wrong path')
    
#To implement two or more test cases according to the condition,we can use keyword => and,or ,not

user='Admin'
logged_in=True

if user=='Admin' and logged_in:
    print('Login successfully!!!')
else:
    print('Fail')
    
if not logged_in:
    print('Hi!!')
else:
    print('Hello')
    
# keyword 'is' is used to check if two objects have same id,i.e two objects are same objects in the memory

a=[1,2,3]
b=[1,2,3]

print(a==b)
#Above line will print true

print(a is b)
#Above line will print false ,as the  2 objects don't have same id.

#But if i do b=a and then print(a is b),it will give  true ,coz now 2 objects are same objects in memory.

#False Values:
   #False
   #None
   #Zero of any numeric type
   #Any empty sequence .for e.g '',{},[]
   #Any empty mapping .for e.g {}
   
condition=None

if condition:
    print('Yess!')
else:
    print('No!!')

    


