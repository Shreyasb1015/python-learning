
cs_courses={'History','Physics','Maths','CompSci'}

print(cs_courses)

#sets are defined using { }.

#If we repetatively print the above line..it will alwasy give me different order of elements.
#That's coz, sets don't really care about orders.
#They are useful to find whether a element is in set or not.
#It is  also useful to remove duplicate values,as sets can store the duplicate values.

#For e.g =>

cs_courses={'History','Physics','Maths','CompSci','Art','Maths'}
print(cs_courses)
#The above line gives me output ,in which Maths element is present only once.

#To check if specific element is present in set or not,we do =>

print('Maths' in cs_courses)

art_courses={'Art','History','Machine learning','Python'}

#To get the common elements of 2 sets we use set1name.intersection(set2name)

print(cs_courses.intersection(art_courses))

#To get the different elements of form 2 sets we use set1name.differnce(set2name)
#It will give me the elements from set1 that are not common to set2.

print(cs_courses.difference(art_courses))

#We can also combine two sets using set1name.union(set2name)
print(cs_courses.union(art_courses))
