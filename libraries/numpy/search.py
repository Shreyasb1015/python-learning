
#Searching Arrays --->

#We can search an array for a certain value, and return the indexes that get a match.

#To search an array, use the where() method.

import numpy as np

arr=np.array([1,2,3,4,5,6,7,4])

x=np.where(arr==4)

#It returns a tuple where index is 4.
print(x)

#To find the index where element is even -->

x=np.where(arr % 2==0 )

print(x)

#There is a method called searchsorted() which performs a binary search in the array.
# It returns the index where the specified value would be inserted to maintain the search order.

#Note -->The searchsorted() method is assumed to be used on sorted arrays.

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

#The above method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.

#By default the left most index is returned, but we can give side='right' to return the right most index instead.

x=np.searchsorted(arr,7,side='right')

print(x)

#To search for more than one value, use an array with the specified values. -->
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)

#The return value is an array: [1 2 3] containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order.


