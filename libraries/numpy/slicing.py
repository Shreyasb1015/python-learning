#Slicing in python means taking elements from one given index to another given index.
#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].

#If we don't pass start its considered 0

#If we don't pass end its considered length of array in that dimension

#If we don't pass step its considered 1
import numpy as np;

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

#Note -->The result includes the start index, but excludes the end index.

#For slicing elements from index 4 to end -->
print(arr[4:])

#For slicing elements from beginning to index 4 -->
print(arr[:4])

#Negative slicing -->

#Use the minus operator to refer to an index from the end:
#To Slice from the index 3 from the end to index 1 from the end: -->

print(arr[-3:-1])

#Step -->

# We use the step value to determine the step of the slicing:
# To Return every other element from index 1 to index 5:-->

print(arr[1:5:2])

#To Return every other element from the entire array:
print(arr[::2])

#Slicing 2-D arrays -->
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

#From the second element, slicing elements from index 1 to index 4 (not included):

print(arr[1,1:4])

# From both elements, to get index 2:
print(arr[0:2,2])

#From both elements, slicing index 1 to index 4 (not included), this will return a 2-D array:

print(arr[0:2,1:4])
