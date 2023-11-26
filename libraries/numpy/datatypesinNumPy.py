#NumPy has some extra data types, 
# Refer to data types with one character, like i for integers, u for unsigned integers etc.

#Below is a list of all data types in NumPy and the characters used to represent them.

#i - integer
#b - boolean
#u - unsigned integer
#f - float
#c - complex float
#m - timedelta
#M - datetime
#O - object
#S - string
#U - unicode string
#V - fixed chunk of memory for other type ( void )

import numpy as np

#The NumPy array object has a property called dtype that returns the data type of the array -->
arr=np.array([1,2,3,4,5])

print(arr.dtype)

arr=np.array(['apple','mango','orange'])
print(arr.dtype)

#Creating arrays with defined data types 

#We use the array() function to create arrays.
# This function can take an optional argument: dtype that allows us to define the expected data type of the array elements:

#For e.g -->To create an array with data type string:

arr=np.array([1,2,3,4],dtype='S')

print(arr)
print(arr.dtype)

#For i, u, f, S and U we can define size as well.

arr = np.array([1, 2, 3, 4], dtype='i4')
#This creates numpy array with data type 4 bytes integer.
print(arr.dtype)

#If a type is given in which elements can't be casted then NumPy will raise a ValueError.

#Converting Data Type on Existing Arrays

#The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
#The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

arr=np.array([1.1,2.3,4.5])

newarr=arr.astype('i')        #Converting the type to integer

print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)