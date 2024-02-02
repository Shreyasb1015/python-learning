l1=[]
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
print(l1)
choice=0
while choice <4:
    print("Stack operations")
    print("1.push")
    print("2.pop")
    print("3.Search")
    print("4.exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        ele=int(input("Enter the element: "))
        l1.append(ele)
        print(l1)
    elif choice==2:
        try:
            l1.pop()
            print(l1)
        except IndexError:
            print("Stack is empty")
    elif choice==3:
        element=int(input("enter element "))
        try:
            pos=l1.index(element)
            print(f"element found at position {pos} ")
        except ValueError:
            print('element not found')
    elif choice==4:
        break