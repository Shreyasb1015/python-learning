from stack import Stack

s=Stack()

choice=0
while choice <5:
    print("Stack operations")
    print("1.push")
    print("2.pop")
    print("3.Search")
    print("4.peek")
    print("5.exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        ele=int(input("Enter the element: "))
        s.push(ele)
        s.printstack()
    elif choice==2:
        s.pop()
    elif choice==3:
        s.search()
    elif choice==4:
        s.peek()
    elif choice==5:
        break