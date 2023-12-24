#Inheritance allows you to inherit the properties of a class, i.e., base class to another, i.e., derived class.


#Creating a Parent Class

class Person():
    
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def display(self):
        print(self.name,self.id)
        


emp=Person("Shreyas",10)
emp.display()
        

#Creating a child class

class Emp(Person):
    
    def Print(self):
        print("Emp class was called !")
        

Emp_details=Emp("Rohit",45)

Emp_details.display()

Emp_details.Print()
 
