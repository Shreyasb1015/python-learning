## Revision of numpy

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)

arr2=np.array([1,2,3,4,5,6],dtype='i')
print(arr2)

#Creating an array full of zeros
arr3=np.zeros((3,4))
print(arr3)

#Creating an array full of ones
arr4=np.ones((3,4))
print(arr4)

#Creating an array with random values
arr5=np.random.random((3,4))
print(arr5)

#Creating an array of random integers
arr6=np.random.randint(0,10,(3,4))
print(arr6)

#Creating an array with a range of elements with step size
arr7=np.arange(0,10,2)
print(arr7)

#Creating empty array
arr8=np.empty((3,4))
print(arr8)

#Creating an array with evenly spaced values with number of samples
arr9=np.linspace(0,10,5)
print(arr9)

#Saving and loading array on disk in binary format
#np.save('my_array',arr9)
#np.load('my_array.npy')

# Checking the shape of the array
print(arr9.shape)

#Checkking the length of array
print(len(arr5))

#Checking the number of dimensions
print(arr6.ndim)

#Checking the data type of array
print(arr6.dtype)

#Converting the data type of array
arr10=arr6.astype('f')

#Aritheatic operations on array

#Addition

print(np.add(arr6,arr10))

#Subtraction
print(np.subtract(arr6,arr10))

#Multiplication
print(np.multiply(arr6,arr10))

#division
print(np.divide(arr6,arr10))

#Exponentiation
print(np.exp(arr6))

#Sqaure root
print(np.sqrt(arr6))

#Sine
print(np.sin(arr6))

#Cosine
print(np.cos(arr6))

#Logarithm
print(np.log(arr6))

#Dot product
#print(np.dot(arr6,arr10))

#Aggregation functions

#Sum
print(arr6.sum())

#Minimum
print(arr6.min())

#Maximum
print(arr6.max())

#Mean
print(arr6.mean())

#Median
print(np.median(arr6))

#Correlation coefficient
print(np.corrcoef(arr6))

#Standard deviation
print(np.std(arr6))

#Sorting array
print(np.sort(arr6))
#Sorting with axis
print(np.sort(arr6,axis=1))

#Changing the shape of array
print(arr6.reshape(2,6))

#Resizing the array
print(np.resize(arr6,(2,6)))


#Appending the array
print(np.append(arr6,arr10))

#Inserting the array
print(np.insert(arr6,1,5))

#Deleting the array
print(np.delete(arr6,1))

#Concatenating the array
print(np.concatenate((arr6,arr10),axis=1))