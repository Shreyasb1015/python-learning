class Stack():

    def _init_(self):
        self.s=[]
    
    def push(self,ele):
        self.s.append(ele)
    
    def pop(self):
        try:
            self.s.pop()
            print(self.s)
        except  IndexError:
            print("Stack has no element to pop")
    
    def search(self):
        element=int(input("enter element "))
        try:
            pos=self.s.index(element)
            print(f"element found at position {pos} ")
        except ValueError:
            print('element not found')
    
    def peek(self):
        try:
          print(self.s[-1])
        except ValueError:
            print('Stack is empty')
    
    def reversestack(self):
       reversed_stack=list(reversed(self.s))
       print(reversed_stack)

    def printstack(self):
            print(self.s)