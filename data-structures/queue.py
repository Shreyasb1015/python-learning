l1=[]
l1.append('a')
l1.append('b')
l1.append('c')

choice=0

while choice <4:
    print("Queue operations")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Search")
    print("4.Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        ele=input("Enter your element ")
        l1.append(ele)
        print(l1)
    elif choice==2:
        try:
            l1.pop(0)
            print(l1)
        except  IndexError:
              print("Queue has no element to to dequeue")
    elif choice==3:
        element=input("enter element ")
        try:
            pos=l1.index(element)
            print(f"element found at position {pos} ")
        except ValueError:
            print('element not found')
    elif choice==4:
        break