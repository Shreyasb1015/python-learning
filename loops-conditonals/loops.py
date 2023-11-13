
nums=[1,2,3,4,5]

#For loop =>

for num in nums:
    print(num)
    
#Using break statment

for num in nums:
    if num==3:
        print('Found!')
        break
    print(num)
    
#To skip specific iteration ,we can use  continue keyword
for num in nums:
    if num==3:
        print('Found!')
        continue
    print(num)
#Using nested for loop

for num in nums:
    for letter in'abc':
        print(num,letter)
        
#We can also run the loop till a specified range

for i in range(10):
    print(i)

#We can also specify the start and end for the range()
#start is inclusive ,whereas end is exclusive ,i.e if end=11,it will print till 10
for i in range(1,11):
    print(i)
    
x=5
while x<10:
    print(x)
    x=x+1