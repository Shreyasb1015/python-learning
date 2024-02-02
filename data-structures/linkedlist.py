l1=[]
l1.append("India")
l1.append("America")
l1.append("China")
print(l1)
choice=0
while choice<5:
    print("linked list operations")
    print("1.add element")
    print("2.remove element")
    print("3.replace element")
    print("4.search element")
    print("5.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        element=input("enter element")
        pos=int(input("position"))
        l1.insert(pos,element)
        print(l1)
    elif choice==2:
        try:
            element=input("enter element")
            l1.remove(element)
        except ValueError:
            print('element not found')
    elif choice==3:
        element=input("enter element")
        pos=int(input("at what position?"))
        l1.pop(pos)
        l1.insert(pos,element)
    elif choice==4:
        element=input("enter element")
        try:
            pos=l1.index(element)
            print("element found at position ",pos)
        except ValueError:
            print('element not found')
    elif choice ==5:
        break