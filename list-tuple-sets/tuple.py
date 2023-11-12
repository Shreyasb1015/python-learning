
#Tuples are same as of list in python
#One basic difference  between list and tuple=>
#    List are mutable and tuples are immutable

list_1=['History','Physics','CompSci']
list_2=list_1

print(list_1)
print(list_2)

list_1[0]='Art'
#If we change the value of list_1 ,it will also change the value of 0th index of list_2
print(list_1)
print(list_2)



#Immutable
tuple_1=('History','Physics','CompSci')
tuple_2=tuple_1
print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'Art'  # type: ignore
#print(tuple_1)
#print(tuple_2)

#The above 3 lines will generate errors,as tuple dont support item assignment coz they are immutable.
#Hence ,some methods like append(),reverse() can not be applied on tuples.
#tuples can be used when we want the collection of data ,through which can loop in and access the elements and doesnt involve changing of elements.

