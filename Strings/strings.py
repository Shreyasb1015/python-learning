
message='Hello World'
# In Python single quotes are used normally with strings(double quotes can also be used).
#Basically,double quotes are used when string contains a quote in itself.Hence to avoid the confusion,we use double quotes.For e.g:- message="I don't have ans".
print(message)

#To print multiline text, we use three double quotes at start and end.

messgae2="""Python is one of the
popular languages"""

print(messgae2)

#To get the length of String,we use len() which is bulit in function in python

print(len(message))

#To access the individual character of String, we use [] notation.

print(message[0])

# To access the range of words in String we can specify the range in[].
#Note: first index is inclusive and last index is not included in the range.

print(message[0:5])
#or it can be also print(message[:5]) ->same result
#This above method is called slicing.

#To print the String in lowercase ,we can use stringname.lower() and stringname.upper() for uppercase

print(message.lower())

#To get the number of occurence of specific character in the string,we can use stringname.count()..which takes character to be count as the argument.

print(message.count('l'))

#To replace the specific word or character in String,we use stringname.replace().
#It takes two arguments=> string to be replaced,string that should be inserted in existing string's place.

print(message.replace('World','Universe'))

name=" Shreyas"
greeting="Hello"

greet_msg=greeting+name
#This is called concatenation of Strings.
print(greet_msg)

#Uisng f-String format

print(f'{greeting}{name},Welcome to python!!!')

# Short tip => To get to know about all methods that can be used with string message.We can  do the following:
#This shows all the methods that we can apply to our string 
print(dir(message))

#To get lot more info about strings and its method ,we can do=>

print(help(str))
