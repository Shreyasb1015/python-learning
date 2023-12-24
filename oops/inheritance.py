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


# Case where child class's constructor takes more no of arguments than base class'c constructor.


class Person1(object):
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
 
    def display(self):
        print(self.name)
        print(self.idnumber)
 
# child class
class Employee1(Person1):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        
        # invoking the __init__ of the parent class
        Person1.__init__(self, name, idnumber)
 
# creation of an object variable or an instance
a = Employee1('Rahul', 886012, 200000, "Intern")
 
# calling a function of the class Person using its instance
a.display()


#Super() function -->

# The super() function is a built-in function that returns the objects that represent the parent class. 
# It allows to access the parent class’s methods and attributes in the child class.

# parent class
class Person3():
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def display(self):
    print(self.name, self.age)
 
# child class
class Student(Person3):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("Rahul", age)
 
  def displayInfo(self):
    print(self.sName, self.sAge)
 
obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()

## Above all examples are of single inheritance.

