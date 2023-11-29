
#The shape of an array is the number of elements in each dimension.

#NumPy arrays have an attribute called shape.
#It returns a tuple with each index having the number of corresponding elements.

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)
#The example above returns (2, 4). 
#It means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.

#Creating an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 
# And verifying that last dimension has value 4:

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)