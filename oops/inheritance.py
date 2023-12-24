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

### Multiple Inheritance

class Base1():
    
    def __init__(self):
        self.str1="Cricket"
        print("I am base class 1")

class Base2():
    
    def __init__(self):
        self.str2="Kabbadi"
        print("I am base class 2")
        
class ChildClass(Base1,Base2):
    
    def __init__(self):
        
        Base1.__init__(self)
        Base2.__init__(self)
        print("I am child class")
        
        
    def printStrs(self):
        print(self.str1, self.str2)
        

c=ChildClass()
c.printStrs()


#Multilevel Inheritance  


class Base(object):
 
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
 
# Inherited or Sub class (Note Person in bracket)
class Child(Base):
 
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
 
    # To get name
    def getAge(self):
        return self.age
 
# Inherited or Sub class (Note Person in bracket)
 
 
class GrandChild(Child):
 
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
 
    # To get address
    def getAddress(self):
        return self.address
 
 
# Driver code
g = GrandChild("Shreyas", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())

###We don’t always want the instance variables of the parent class to be inherited by the child class .
# we can make some of the instance variables of the parent class private, which won’t be available to the child class. 

#In Python inheritance, we can make an instance variable private by adding double underscores before its name.

