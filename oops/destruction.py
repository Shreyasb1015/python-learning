### We have __del__() in python which is used as destructor.
#It is called when all references to the object have been deleted i.e when an object is garbage collected. 
#Destructors are called when an object gets destroyed.
# In Python, destructors are not needed as much as in C++ because Python has a garbage collector that handles memory management automatically.

class A:
    def __init__(self, bb):
        self.b = bb
  
class B:
    def __init__(self):
        self.a = A(self)
    def __del__(self):
        print("die")
  
def fun():
    b = B()
  
fun()