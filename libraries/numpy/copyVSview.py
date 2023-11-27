#The main difference between a copy and view of an array is that the copy is a new array
# and the view is just a view of the original array.

#The copy owns the data and any changes made to the copy will not affect original array 
# Any changes made to the original array will not affect the copy.

#The view does not own the data and any changes made to the view will affect the original array.
# Any changes made to the original array will affect the view.

import numpy as np

arr=np.array([1,2,3,4,5])

#Making the copy of array -->
x=arr.copy()
print(x)
print(arr)

#Now making changes in the array 
arr[0]=42
print(x)            #Copy will not be affected by the changes in the array
print(arr)


#Making the view of array
arr2=np.array([9,8,7,6,5])

y=arr2.view()

print(arr2)
print(y)

#Making changes in the array
arr2[0]=17

print(arr2)
print(y)      #View will be affected by the changes in the array

#Now making changes in the view -->

y[0]=90
print(y)
print(arr2) #The original array will also be affected if we change the contents of view

#Copies own the data whereas view doesn't own the data.

#To check this,every NumPy array has the attribute base that returns None if the array owns the data.
#Otherwise, the base  attribute refers to the original object.

arr3=np.array([3,4,5,6,7])
v=arr3.copy()
w=arr3.view()

print(v.base)
print(w.base)