
#Functions are created using def keyword.
#If we dont want to dfine the body of func,we can use the keyword pass to skip the definition of function


def hello_func():
    pass

print(hello_func())
#Above line will give the output as None

def hello():
    print('Hello!!')


hello()   ##This is function calling

def return_func():
    return 'Good Morning!'

message=return_func()
print(message)

#We can pass arguments in the func  =>

def arg_func(message):
    print(message)
    

arg_func('It is parameterized function')

#We can also have default arguments ,i.e if arguments are not passed,default values are used.

def default_func(name,message='Hello'):
    print(message+ name)
    

default_func('Shreyas')

#Basic program using function =>

month_days=[0,31,28,31,30,31,30,31,31,31,30,31]

def is_leap(year):
    return year% 4== 0 and (year % 100 !=0 or year % 400 == 0)


def days_in_month(year,month):
    if not 1<=month <=12:
        return 'Invalid Month'
    if month ==2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2020))

print(days_in_month(2017,3))