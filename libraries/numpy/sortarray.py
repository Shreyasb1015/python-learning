#Sorting means putting elements in an ordered sequence.

#Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.

#The NumPy ndarray object has a function called sort(), that will sort a specified array.

import numpy as np

arr=np.array([9,8,7,6,5])

print(np.sort(arr))

#This method returns a copy of the array, leaving the original array unchanged.

#We can also sort arrays of strings, or any other data type:

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

#Sorting 2D array -->

#If you use the sort() method on a 2-D array, both arrays will be sorted:


arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))