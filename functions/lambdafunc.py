
##Python Lambda Functions are anonymous functions means that the function is without a name.
## As we already know the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. 

##Sytax : lambda arguments: expression
#This function can have any number of arguments but only one expression, which is evaluated and returned.

str='Shreyas'
upper=lambda string:string.upper()

print(upper(str))

#Condition Checking Using Python lambda function

format_numeric=lambda num: f"{num:,}" if isinstance(num,int) else f'{num:.2f}'

print(format_numeric(1000000))
print(format_numeric(1000000.1234))

#Difference between lambda func and def func

def cube(num):
    return num*num*num

lambda_cube=lambda num:num*num*num

print(cube(3))
print(lambda_cube(3))

##Python Lambda Function with List Comprehension
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())
    

#Python lambda with if and else

max=lambda x,y:x if x>y else y

print(max(10,20))

#The filter() function in Python takes in a function and a list as arguments. This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True.

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))
 
print(adults)

#using lambda func with map func
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(map(lambda x: x*2, li))
print(final_list)