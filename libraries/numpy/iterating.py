#Iterating means going through elements one by one.
import numpy as np


#Iterating elements of 1D array -->

arr=np.array([1,2,3,4,5])

for x in arr:
    print(x)
    

#Iterating 2-D Arrays -->

arr = np.array([[1, 2, 3], [4, 5, 6]])
#In a 2-D array it will go through all the rows.

for x in arr:
  print(x)
  
#If we iterate on a n-D array it will go through n-1th dimension one by one.

#Iterating on each scalar element of the 2-D array:-->

for x in arr:
    for y in x:
        print(y)
        
#Iterating 3-D Arrays  --->

#In a 3-D array it will go through all the 2-D arrays.

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)
  
#Iterating over the scalars in 3D array

for x in arr:
    for y in x:
        for z in y:
            print(z)
    

#Iterating Arrays Using nditer()   --->

#The function nditer() is a helping function that can be used from very basic to very advanced iterations. 
# It solves some basic issues which we face in iteration.

#In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.
#To avoid it ,we use nditer().

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)
    
#We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
#NumPy does not change the data type of the element in-place (where the element is in array) .
# So it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
  
#Iterating through every scalar element of the 2D array skipping 1 element:

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)
  
  
#Enumerated Iteration Using ndenumerate() --->

#Enumeration means mentioning sequence number of somethings one by one.
#Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

arr = np.array([1, 2, 3])

for idx,x in np.ndenumerate(arr):
    print(idx,x)
    
#Enumerate on following 2D array's elements:

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx,x in np.ndenumerate(arr):
    print(idx,x)