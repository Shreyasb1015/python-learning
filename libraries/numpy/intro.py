import numpy as np

#numpy is used for working with arrays.It is short form for "Numerical Python"
#It also has functions for working in domain of linear algebra, fourier transform, and matrices.

#In Python we have lists that serve the purpose of arrays, but they are slow to process.
#NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
#The array object in NumPy is called ndarray.

#NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

# For creating array with numpy,use array().

arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))

#To check the version of numpy ..u can use np.__version__()
print(np.__version__)

#Dimensions ==>

# 0-D Array-->0-D arrays, or Scalars, are the elements in an array.

arr2=np.array(32)
print(arr2)

#1D array --> An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

arr3=np.array([1,2,3])
print(arr3)

#2D array --> An array that has 1-D arrays as its elements is called a 2-D array.
#These are often used to represent matrix or 2nd order tensors.NumPy has a whole sub module dedicated towards matrix operations called numpy.mat

arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr4)

#3D array -->An array that has 2-D arrays (matrices) as its elements is called 3-D array.
#These are often used to represent a 3rd order tensor.

arr5=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr5)

# NumPy Arrays provides the 'ndim' attribute that returns an integer that tells us how many dimensions the array have.
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)
print(arr5.ndim)


#High dimensional arrays -->An array can have any number of dimensions.
#When the array is created, you can define the number of dimensions by using the ndmin argument.

arr6=np.array([1,2,3,4],ndmin=5)
print(arr6)

#In the above array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, 
# the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.

