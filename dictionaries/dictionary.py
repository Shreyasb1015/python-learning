
#Dictionary is the collection of data in the format of key-value pairs.
student={ 'name':'Shreyas','age':'19','courses':['Maths','CompSci']}

print(student)

#To get the specific value ,we can access it using its key  and [ ]

print(student['name'])

#We can also use key as the int number and then access it using that integer number =>
student_2={ 1:'Shreyas',2:'Maths'}
print(student_2[2])

#We can also get the specific value by using dictionaryname.get() which takes the value as argument.

print(student.get('age'))

#To add the value ,we can do =>

student['hobby']='Cricket'

#The above line will search if there is existing key called 'hobby'.If yes ,then it will update that value,else will insert the new key-value pair.

print(student)

#We can use dictionaryname.update() to either add a new key value pair or to update if any.
#It takes a dictionary as argument ,which conatins all the key-values pair that we want to add or update.

student.update({'name':'Sachin','age':'50','Country':'India'})
print(student)

#To delete specific value from the dictionary,we can use del keyword and can specify the key of value that must be deleted.
del student['Country']
print(student)

#We can also use dictionaryname.pop() to delete the value in dictionary.It returns the value that was popped.
#We need to pass key as argument

pop_elem=student.pop('age')
print(student)

#To get the number of keys in the dictionary,we can use len()

print(len(student))

#To get all the keys in dictionary we can use dictionaryname.keys()

print(student.keys())


#To get all the values in dictionary we can use dictionaryname.values()

print(student.values())

#To get all the key-value pairs in dictionary we can use dictionaryname.items()
print(student.items())

#To loop through the key and values of dictionary ,we can do =>

for key,values in student.items():
    print(key,values)