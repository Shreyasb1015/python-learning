#Array indexing is the same as accessing an array element.

#You can access an array element by referring to its index number.

#The indexes in NumPy arrays start with 0.

import numpy as np
arr2=np.array([1,2,3,4])
#To get element 3 from above matrix ,we use -->
print(arr2[2])

#Accessing 2-D array elements -->
#To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
arr = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])

#To get element 50 form the above array ,we can do -->
print(arr[1, 0])

#Accessing 3-D array elements -->
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

#To Access the third element of the second array of the first array we can do -->
print(arr[0,1,2])

#we can use negative indexing, to access array from the end.

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# To Print the last element from the 2nd dim:
print(arr[1,-1])