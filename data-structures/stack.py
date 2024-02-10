class Stack():

    def __init__(self):
        self.s=[]
    
    def push(self,ele):
        self.s.append(ele)
    
    def pop(self):
        try:
            self.s.pop()
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
          return (self.s[-1])
        except ValueError:
            print('Stack is empty')
            return None
    
    def reversestack(self):
       reversed_stack=list(reversed(self.s))
       print(reversed_stack)

    def printstack(self):
        print(self.s)
        
    def isEmpty(self):
        return len(self.s) == 0
    