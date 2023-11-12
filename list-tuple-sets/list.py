
courses=['History','Maths','Physics']
print(courses)

#To get the length of list.. we will use len()
print(len(courses))

#To access the individual elements of list, we can use [] notation
print(courses[0])

#To access the last element of list..we can use[len()-1] or [-1] notation.
print(courses[-1])

#To get the range of elements ..we can use slicing where first argument is inclusive and second one is exclusive.
print(courses[0:2])


#   <=LIST METHODS =>   

#To insert the element at the end of list,we use listname.append().

courses.append('Computer Science')
print(courses)

#To insert the element at the specific location of list, we use listname.insert()
#It takes 2 arguments i.e first is index where it needs to be inserted and sceond is the element that we want to insert
# Note that => Inserting the element at the index where any previous element was stored,doesnt cause the old element to be replaced.
# It shifts all the elements towards right and insert new element at specified index.
courses.insert(1,'Geometry')
print(courses)

courses_2=['Art','Education']

#To add the one list to other => we use extend()
#It takes one argument i.e to be extended to the main list

courses.extend(courses_2)
print(courses)

#To remove the specific element we use ,listname.remove()
#It takes the element to be removed

courses.remove('Art')
print(courses)

#To remove the last element of list.. we can use listname.pop()
#It returns the value of last element that was popped

popped_value=courses.pop()

print(popped_value)
print(courses)

#To reverse the list ,we can use listname.reverse()

courses.reverse()
print(courses)

#To sort the list,we can use listname.sort()
#If list contains strings or characters, then it is sorted alphabetically
#If list conatins numbers,then it is sorted in ascending order.

numbers=[100,67,23,56,12,67,19,35,42]
numbers.sort()

courses.sort()
print(numbers)
print(courses)

#To sort our list in descending order ,we can pass an argument reverse=True inside the sort() .
numbers.sort(reverse=True)
print(numbers)

#To get the minimum value of element in the list,we can use min().We need to  pass our list in this method

print(min(numbers))

#To get the maximum value of element in the list,we can use max().We need to  pass our list in this method

print(max(numbers))

#To get the index of certain element , we use listname.index().It takes the element as argument.
index=courses.index('Maths')
print(index)

#To check if certain element is present in list..then we can do =>
#It returns true or false
print('Maths' in courses)

#Looing through list

for course in courses:
    print(course)
