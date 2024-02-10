class Queue():

    def __init__(self):
        self.q=[]
    
    def enqueue(self):
        ele=input("Enter your element ")
        self.q.append(ele)
        print(self.q)
    def dequeue(self):
        try:
            self.q.pop(0)
            print(self.q)
        except  IndexError:
              print("Queue has no element to to dequeue")
    
    def search(self):
        element=input("enter element ")
        try:
            pos=self.q.index(element)
            print(f"element found at position {pos} ")
        except ValueError:
            print('element not found')
