#When working with classes in Python, the term “self” refers to the instance of the class that is currently being used. 
# It is customary to use “self” as the first parameter in instance methods of a class. 
# Whenever you call a method of an object created from a class, the object is automatically passed as the first argument using the “self” parameter. 
# This enables you to modify the object’s properties and execute tasks unique to that particular instance.

class Number():
    
    def __init__(self,value):
        self.value=value
        
    def print_value(self):
        print(self.value)
        

obj1=Number(17)
obj1.print_value()

#When working with classes,it’s important to understand that in Python, a class constructor is a special method named __init__ .
# It gets called when you create an instance (object) of a class.
#This method is used to initialize the attributes of the object.

class Subject:
    
    def __init__(self,attr1,attr2):
        self.attr1=attr1
        self.attr2=attr2
        


obj=Subject('Maths','Science')
print(obj.attr1)
print(obj.attr2)
