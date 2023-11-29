# Reshaping means changing the shape of an array.

# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

import numpy as np

#Reshaping the array from 1D to 2D

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr)

#To reshape the array we  can use arrayname.reshape().

newarr=arr.reshape(4,3)
#This means  that the outermost dimension will have 4 arrays, each with 3 elements
print(newarr)



#Reshaping the array from 1D to 3D

newarr=arr.reshape(2,3,2)

#This means that the outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements

print(newarr)

#Ques is that can we reshape into any shape ?
#Ans -->Yes, as long as the elements required for reshaping are equal in both shapes.
#For e.g ,The below program will give me error. -->

#arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

#newarr = arr.reshape(3, 3)  
# coz there are total 8 elements and you are specifying dimensions and elements such that they will have 9 elements.This is not allowed.


#Unknown Dimensions -->

#You are allowed to have one "unknown" dimension.

#Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

#Pass -1 as the value, and NumPy will calculate this number for you.

#Converting 1D array with 8 elements to 3D array with 2x2 elements.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

#Note: We can not pass -1 to more than one dimension.



#Flattening the arrays  ----->

#Flattening array means converting a multidimensional array into a 1D array.

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)

#There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc.


