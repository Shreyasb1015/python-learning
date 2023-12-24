#Python has a particular method called __str__(). that is used to define how a class object should be represented as a string.
#When a class object is used to create a string using the built-in functions print() and str(), the __str__() function is automatically used.

class Company:
    def __init__(self, name, company):
        self.name = name
        self.company = company
 
    def __str__(self):
        return f"My name is {self.name} and I work in {self.company}."
 
 
my_obj = Company("John", "Amazon")
print(my_obj)