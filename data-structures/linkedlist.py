class LinkedList():
     
     def __init__(self):
          self.l1=[]
     
     def add(self):
          ele=input("Enter the element to be pushed: ")
          pos=int(input("position? "))
          self.l1.insert(pos,ele)
          print(self.l1)
     def remove(self):
        try:
            element=input("enter element ")
            self.l1.remove(element)
            print(self.l1)
        except ValueError:
            print("element not found")
     def replace(self):
        element=input("enter element ")
        pos=int(input("at what position? "))
        self.l1.pop(pos)
        self.l1.insert(pos,element)
        print(self.l1)
        
     def search(self):
            element=input("enter element ")
            try:
                pos=self.l1.index(element)
                print(f"element found at position {pos} ")
            except ValueError:
                print('element not found')
