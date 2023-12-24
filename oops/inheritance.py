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
 

#Another example

class Player():
    
    def __init__(self,name):
        self.name=name
    
    def getName(self):
        return self.name
        
    def isPlayer(self):
        return False
    
        
class Sportsman(Player):
    
    def isPlayer(self):
        return True
    
#Creating object of parent class
p=Player("Rohit")
print(p.getName(),p.isPlayer())

#Creating object of child class
s=Sportsman("Rohit")
print(s.getName(),s.isPlayer())

#In Python, every class inherits from a built-in basic class called ‘object’ i.e class Classname(object)
